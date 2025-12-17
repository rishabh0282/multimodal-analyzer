import React from "react";
import ImageAnalyze from "./components/ImageAnalyze";
import TextAnalyze from "./components/TextAnalyze";
import "./App.css";

export default function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1>?? Multimodal Analyzer</h1>
        <p>Analyze images and text with AI</p>
      </header>
      <main className="app-main">
        <ImageAnalyze />
        <TextAnalyze />
      </main>
      <footer className="app-footer">
        <p>Powered by PyTorch + Transformers + Flask</p>
      </footer>
    </div>
  );
}
