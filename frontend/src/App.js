import React, { useState } from "react";
import axios from "axios";

function App() {
  const [platform, setPlatform] = useState("segment");
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);

  const askQuestion = async () => {
    try {
      const res = await axios.post("http://localhost:5000/query", { platform, question });
      setResponse(res.data.answers);
    } catch (err) {
      console.error(err);
      setResponse(["An error occurred."]);
    }
  };

  return (
    <div>
      <h1>CDP Chatbot</h1>
      <select value={platform} onChange={(e) => setPlatform(e.target.value)}>
        <option value="segment">Segment</option>
        <option value="mparticle">mParticle</option>
        <option value="lytics">Lytics</option>
        <option value="zeotap">Zeotap</option>
      </select>
      <textarea
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button onClick={askQuestion}>Ask</button>
      <div>
        <h2>Response:</h2>
        {response ? response.map((ans, idx) => <p key={idx}>{ans}</p>) : "No response yet."}
      </div>
    </div>
  );
}

export default App;
