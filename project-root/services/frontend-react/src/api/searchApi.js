import axios from "./axiosClient";

export const semanticSearch = async (query) => {
  const res = await axios.post("/search/semantic-search", { query });
  return res.data.results;
};
