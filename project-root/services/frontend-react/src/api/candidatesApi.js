import api from "./axiosClient";

export const getCandidates = () => api.get("/candidates/");
export const getCandidateById = (id) => api.get(`/candidates/${id}`);
export const createCandidate = (data) => api.post("/candidates/", data);
export const updateCandidate = (id, data) => api.put(`/candidates/${id}`, data);
export const deleteCandidate = (id) => api.delete(`/candidates/${id}`);
