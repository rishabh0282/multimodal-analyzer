import React, { useState } from "react";
import "./ImageAnalyze.css";

export default function ImageAnalyze() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function submit(e) {
    e.preventDefault();
    if (!file) {
      setError("Please select an image");
      return;
    }
    setLoading(true);
    setError("");
    const fd = new FormData();
    fd.append("file", file);
    try {
      const res = await fetch("/api/analyze/image", { method: "POST", body: fd });
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
    <div className="analyze-container image-container">
      <h2>Analyze Image</h2>
      <form onSubmit={submit}>
        <input type="file" accept="image/*" onChange={(e) => setFile(e.target.files[0])} disabled={loading} />
        <button type="submit" disabled={loading || !file}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </form>
      {error && <div className="error-message">{error}</div>}
      {loading && <div className="loading">Processing image...</div>}
      {result && (
        <div className="result-box">
          <h3>Analysis Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
