import React, { useState } from "react";
import { semanticSearch } from "../api/searchApi";


function Search() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const r = await semanticSearch(query);
    setResults(r);
  };

  return (
    <div>
      <h2>Buscar candidatos por texto</h2>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Escribe algo como 'desarrollador python'"
      />
      <button onClick={handleSearch}>Buscar</button>

      <ul>
        {results.map((r) => (
          <li key={r.candidate_id}>
            Candidate ID: {r.candidate_id} — Score: {r.score.toFixed(3)}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Search;
