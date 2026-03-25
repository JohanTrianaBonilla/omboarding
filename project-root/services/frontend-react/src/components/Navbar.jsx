import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={styles.nav}>
      <Link to="/" style={styles.link}>Lista de Candidatos</Link>
      <Link to="/create" style={styles.link}>Crear Candidato</Link>
      <Link to="/search" style={styles.link}>Busqueda Semantica</Link>
      <Link to="/upload" style={styles.link}>Subir PDF</Link>
      <Link to="/microfrontend" style={styles.link}>Svelte MF</Link>
    </nav>
  );
}

const styles = {
  nav: {
    display: "flex",
    gap: "20px",
    padding: "10px",
    background: "#eee",
    borderBottom: "1px solid #ccc",
  },
  link: {
    textDecoration: "none",
    fontWeight: "bold",
    color: "#333",
  },
};
