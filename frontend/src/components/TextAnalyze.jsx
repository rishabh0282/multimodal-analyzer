import React, { useState } from "react";
import "./TextAnalyze.css";

export default function TextAnalyze() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function submit(e) {
    e.preventDefault();
    if (!text.trim()) {
      setError("Please enter text to analyze");
      return;
    }
    setLoading(true);
    setError("");
    try {
      const res = await fetch("/api/analyze/text", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      const json = await res.json();
      if (res.ok) {
        setResult(json);
      } else {
        setError(json.detail || "Analysis failed");
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="analyze-container text-container">
      <h2>?? Analyze Text</h2>
      <form onSubmit={submit}>
        <textarea
          rows={4}
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text to analyze..."
          disabled={loading}
        />
        <button type="submit" disabled={loading || !text.trim()}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </form>
      {error && <div className="error-message">{error}</div>}
      {loading && <div className="loading">Processing text...</div>}
      {result && (
        <div className="result-box">
          <h3>Analysis Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
