const svelteUrl = import.meta.env.VITE_SVELTE_MF_URL || "http://127.0.0.1:5174";

export default function Microfrontend() {
  return (
    <section style={styles.page}>
      <div style={styles.header}>
        <h1 style={styles.title}>Microfrontend Svelte</h1>
        <p style={styles.copy}>
          Este panel vive en una app separada y consume el mismo backend para mostrar
          un resumen operativo de candidatos.
        </p>
      </div>

      <iframe
        title="Svelte Microfrontend"
        src={svelteUrl}
        style={styles.frame}
      />
    </section>
  );
}

const styles = {
  page: {
    padding: "24px",
  },
  header: {
    marginBottom: "16px",
  },
  title: {
    margin: "0 0 8px",
  },
  copy: {
    margin: 0,
    color: "#445",
  },
  frame: {
    width: "100%",
    minHeight: "70vh",
    border: "1px solid #d6dbe4",
    borderRadius: "16px",
    background: "#fff",
  },
};
