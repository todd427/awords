import React, { useState, useEffect } from "react";

// Place your JSON in the same folder, or fetch from API
import memoriesTemplate from "./memories_template.json";

export default function MemoriesForm() {
  const [memories, setMemories] = useState([]);
  const [currentIdx, setCurrentIdx] = useState(0);

  useEffect(() => {
    setMemories(memoriesTemplate); // Could be fetch("/api/memories") in real app
  }, []);

  const handleAnswerChange = (e) => {
    const updated = [...memories];
    updated[currentIdx].answer = e.target.value;
    setMemories(updated);
  };

  const nextQuestion = () => setCurrentIdx((i) => Math.min(i + 1, memories.length - 1));
  const prevQuestion = () => setCurrentIdx((i) => Math.max(i - 1, 0));

  const saveAll = () => {
    // For demo: just log; in real app, POST to backend
    console.log("Saved memories:", memories);
    alert("Memories saved (console only in this demo).");
  };

  if (!memories.length) return <div>Loading...</div>;
  const q = memories[currentIdx];

  return (
    <div className="max-w-xl mx-auto p-6 shadow rounded bg-white">
      <h2 className="text-2xl mb-4">Grandpa’s Memories</h2>
      <div className="mb-4">
        <div className="text-lg font-semibold mb-2">{`Q${q.id}: ${q.question}`}</div>
        <textarea
          value={q.answer}
          onChange={handleAnswerChange}
          rows={4}
          className="w-full p-2 border rounded"
          placeholder="Type your answer here..."
        />
      </div>
      <div className="flex justify-between">
        <button onClick={prevQuestion} disabled={currentIdx === 0} className="btn">
          Previous
        </button>
        <span>
          {currentIdx + 1} / {memories.length}
        </span>
        <button onClick={nextQuestion} disabled={currentIdx === memories.length - 1} className="btn">
          Next
        </button>
      </div>
      <div className="mt-6">
        <button onClick={saveAll} className="btn w-full bg-blue-600 text-white">
          Save All Memories
        </button>
      </div>
    </div>
  );
}
