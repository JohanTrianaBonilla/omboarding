export default function CandidateForm({ formData, setFormData, onSubmit }) {
  return (
    <form onSubmit={onSubmit}>
      <label>Name:</label>
      <input
        value={formData.name}
        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
      />

      <label>Skills:</label>
      <input
        value={formData.skills}
        onChange={(e) => setFormData({ ...formData, skills: e.target.value })}
      />

      <label>Experience:</label>
      <input
        value={formData.experience}
        onChange={(e) =>
          setFormData({ ...formData, experience: e.target.value })
        }
      />

      <button type="submit">Save</button>
    </form>
  );
}
