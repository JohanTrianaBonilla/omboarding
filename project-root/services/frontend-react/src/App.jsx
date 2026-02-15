import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

import CandidateList from "./pages/CandidateList";
import CandidateCreate from "./pages/CandidateCreate";
import CandidateEdit from "./pages/CandidateEdit";
import Search from "./pages/Search";
import UploadPDF from "./pages/UploadPDF";

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<CandidateList />} />
        <Route path="/create" element={<CandidateCreate />} />
        <Route path="/edit/:id" element={<CandidateEdit />} />
        <Route path="/search" element={<Search />} />
        <Route path="/upload" element={<UploadPDF />} />
      </Routes>
    </BrowserRouter>
  );
}
