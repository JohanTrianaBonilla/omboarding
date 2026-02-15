import { useState } from "react";
import CandidateForm from "../components/CandidateForm";
import { createCandidate } from "../api/candidatesApi";

export default function CandidateCreate() {
  const [formData, setFormData] = useState({
    name: "",
    skills: "",
    experience: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createCandidate(formData);
    window.location.href = "/";
  };

  return (
    <>
      <h1>Create Candidate</h1>
      <CandidateForm
        formData={formData}
        setFormData={setFormData}
        onSubmit={handleSubmit}
      />
    </>
  );
}
