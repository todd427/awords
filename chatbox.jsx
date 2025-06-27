import React, { useState, useRef } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export default function ChatBox() {
  const [messages, setMessages] = useState([
    { role: "assistant", text: "Hello! How can I help you today?" }
  ]);
  const [input, setInput] = useState("");
  const textareaRef = useRef();

  // Handle sending a message
  const sendMessage = () => {
    if (input.trim() === "") return;
    setMessages([...messages, { role: "user", text: input }]);
    setInput("");
    // (Optional) Call your LLM API here and append the assistant's response
  };

  // Keyboard behavior: Enter for newline, Ctrl+Enter for send
  const handleKeyDown = (e) => {
    if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) {
      e.preventDefault();
      sendMessage();
    }
  };

  // Copy message text to clipboard
  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
  };

  return (
    <div style={{
      maxWidth: 600, margin: "2rem auto", borderRadius: 12,
      boxShadow: "0 4px 16px #ccc", background: "#fff", padding: 24
    }}>
      <div style={{
        maxHeight: 400, overflowY: "auto", marginBottom: 16, padding: 8,
        border: "1px solid #eee", borderRadius: 8, background: "#fafbfc"
      }}>
        {messages.map((msg, i) => (
          <div key={i} style={{
            margin: "8px 0",
            textAlign: msg.role === "user" ? "right" : "left"
          }}>
            <span
              style={{
                display: "inline-block",
                background: msg.role === "user" ? "#e0ecff" : "#f0f0f0",
                color: "#111",
                padding: "8px 12px",
                borderRadius: 8,
                maxWidth: 420,
                whiteSpace: "pre-wrap"
              }}
            >
              <ReactMarkdown remarkPlugins={[remarkGfm]}>{msg.text}</ReactMarkdown>
            </span>
            <button
              style={{
                marginLeft: 8, background: "#eee", border: "none", borderRadius: 4, padding: "2px 6px", fontSize: 12, cursor: "pointer"
              }}
              title="Copy to clipboard"
              onClick={() => copyToClipboard(msg.text)}
            >
              📋
            </button>
          </div>
        ))}
      </div>
      <textarea
        ref={textareaRef}
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
        rows={4}
        placeholder="Type your message here (Markdown supported)..."
        style={{
          width: "100%", resize: "vertical", padding: 8, borderRadius: 6, fontSize: 16,
          border: "1px solid #bbb", marginBottom: 8
        }}
      />
      <div style={{ textAlign: "right" }}>
        <button
          onClick={sendMessage}
          style={{
            background: "#4f8cff", color: "#fff", padding: "10px 24px",
            border: "none", borderRadius: 8, fontSize: 16, cursor: "pointer"
          }}
        >
          Send (Ctrl+Enter)
        </button>
      </div>
      <div style={{ marginTop: 12, color: "#888", fontSize: 13 }}>
        <b>Tips:</b> Use <code>Ctrl+Enter</code> (or <code>Cmd+Enter</code> on Mac) to send. <br />
        <b>Markdown supported!</b> Try: <code>**bold**</code>, <code>*italic*</code>, lists, links, code, etc.<br />
        Click <span style={{ fontSize: "120%" }}>📋</span> to copy any message.
      </div>
    </div>
  );
}
