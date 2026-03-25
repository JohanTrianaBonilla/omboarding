<script>
  import { onMount } from "svelte";

  const apiUrl = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

  let loading = true;
  let error = "";
  let candidates = [];
  let highlightedSkills = [];

  async function loadCandidates() {
    loading = true;
    error = "";

    try {
      const response = await fetch(`${apiUrl}/candidates/`);
      if (!response.ok) {
        throw new Error("No fue posible cargar candidatos");
      }

      candidates = await response.json();
      const skillBag = candidates
        .flatMap((candidate) => (candidate.skills || "").split(","))
        .map((skill) => skill.trim())
        .filter(Boolean);

      const counts = skillBag.reduce((acc, skill) => {
        acc[skill] = (acc[skill] || 0) + 1;
        return acc;
      }, {});

      highlightedSkills = Object.entries(counts)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5);
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  }

  onMount(loadCandidates);
</script>

<svelte:head>
  <title>Svelte Candidate Pulse</title>
</svelte:head>

<main class="shell">
  <section class="hero">
    <p class="eyebrow">Svelte Microfrontend</p>
    <h1>Candidate Pulse</h1>
    <p class="summary">
      Vista ligera para monitorear el pipeline de candidatos desde una app separada.
    </p>
    <button on:click={loadCandidates} disabled={loading}>
      {#if loading}Actualizando...{:else}Actualizar datos{/if}
    </button>
  </section>

  {#if error}
    <section class="card error">{error}</section>
  {:else}
    <section class="grid">
      <article class="card metric">
        <span>Total candidatos</span>
        <strong>{candidates.length}</strong>
      </article>

      <article class="card metric">
        <span>Con experiencia reportada</span>
        <strong>{candidates.filter((candidate) => candidate.experience !== null).length}</strong>
      </article>

      <article class="card">
        <h2>Skills detectadas</h2>
        {#if highlightedSkills.length}
          <ul>
            {#each highlightedSkills as [skill, count]}
              <li>
                <span>{skill}</span>
                <strong>{count}</strong>
              </li>
            {/each}
          </ul>
        {:else}
          <p>No hay skills registradas todavia.</p>
        {/if}
      </article>

      <article class="card">
        <h2>Ultimos candidatos</h2>
        {#if candidates.length}
          <ul>
            {#each candidates.slice(-5).reverse() as candidate}
              <li>
                <div>
                  <strong>{candidate.name}</strong>
                  <p>{candidate.skills || "Sin skills detectadas"}</p>
                </div>
                <span>{candidate.experience ?? "N/A"} anos</span>
              </li>
            {/each}
          </ul>
        {:else}
          <p>Aun no hay registros para mostrar.</p>
        {/if}
      </article>
    </section>
  {/if}
</main>

<style>
  :global(body) {
    margin: 0;
    font-family: "Segoe UI", sans-serif;
    background:
      radial-gradient(circle at top left, rgba(255, 196, 123, 0.35), transparent 32%),
      linear-gradient(160deg, #f6efe5 0%, #eef4ff 100%);
    color: #1f2a37;
  }

  .shell {
    min-height: 100vh;
    padding: 32px;
  }

  .hero {
    max-width: 640px;
    margin-bottom: 24px;
  }

  .eyebrow {
    margin: 0 0 8px;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    font-size: 0.75rem;
    color: #975a16;
  }

  h1 {
    margin: 0;
    font-size: clamp(2rem, 6vw, 4rem);
  }

  .summary {
    max-width: 52ch;
    color: #4a5568;
  }

  button {
    border: 0;
    border-radius: 999px;
    padding: 12px 18px;
    background: #1f2a37;
    color: white;
    cursor: pointer;
  }

  .grid {
    display: grid;
    gap: 16px;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  }

  .card {
    padding: 20px;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.84);
    backdrop-filter: blur(10px);
    box-shadow: 0 18px 60px rgba(31, 42, 55, 0.08);
  }

  .metric span {
    color: #52606d;
  }

  .metric strong {
    display: block;
    margin-top: 12px;
    font-size: 2.4rem;
  }

  h2 {
    margin-top: 0;
  }

  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  li {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid rgba(82, 96, 109, 0.14);
  }

  li:last-child {
    border-bottom: 0;
  }

  li p {
    margin: 4px 0 0;
    color: #52606d;
  }

  .error {
    color: #9b2c2c;
    border: 1px solid rgba(155, 44, 44, 0.2);
  }
</style>
