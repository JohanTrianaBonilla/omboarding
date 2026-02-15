import { useState } from "react";
import axios from "../api/axiosClient";

export default function UploadPDF() {
  const [file, setFile] = useState(null);
  const [msg, setMsg] = useState("");

  const upload = async () => {
    if (!file) {
      alert("Selecciona un PDF primero");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(
        "/files/upload-pdf",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );

      setMsg(`Candidato creado con ID ${res.data.candidate_id}`);
    } catch (err) {
      console.error(err);
      setMsg("Error subiendo PDF");
    }
  };

  return (
    <div>
      <h2>Subir hoja de vida (PDF)</h2>
      
      <input 
        type="file" 
        accept="application/pdf"
        onChange={e => setFile(e.target.files[0])}
      />

      <button onClick={upload}>Subir</button>

      <p>{msg}</p>
    </div>
  );
}
