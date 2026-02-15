import { useState, useEffect } from "react";
import { getCandidateById, updateCandidate } from "../api/candidatesApi";
import { useParams } from "react-router-dom";
import CandidateForm from "../components/CandidateForm";

export default function CandidateEdit() {
  const { id } = useParams();
  const [formData, setFormData] = useState({
    name: "",
    skills: "",
    experience: "",
  });

  useEffect(() => {
    const load = async () => {
      const res = await getCandidateById(id);
      setFormData(res.data);
    };
    load();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await updateCandidate(id, formData);
    window.location.href = "/";
  };

  return (
    <>
      <h1>Edit Candidate</h1>
      <CandidateForm
        formData={formData}
        setFormData={setFormData}
        onSubmit={handleSubmit}
      />
    </>
  );
}
