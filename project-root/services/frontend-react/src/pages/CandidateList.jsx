import { useEffect, useState } from "react";
import { getCandidates, deleteCandidate } from "../api/candidatesApi";

export default function CandidateList() {
  const [candidates, setCandidates] = useState([]);

  const loadData = async () => {
    const res = await getCandidates();
    setCandidates(res.data);
  };

  useEffect(() => {
    loadData();
  }, []);

  const handleDelete = async (id) => {
    await deleteCandidate(id);
    loadData();
  };

  return (
    <div>
      <h1>Candidates</h1>

      <a href="/create">➕ Create Candidate</a>

      <ul>
        {candidates.map((c) => (
          <li key={c.id}>
            {c.name} — {c.skills}
            {" "}
            <a href={`/edit/${c.id}`}>✏ Edit</a>
            {" "}
            <button onClick={() => handleDelete(c.id)}>🗑 Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
