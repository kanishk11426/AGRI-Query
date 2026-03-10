/* AgriQuery AI – Frontend Logic */

const API_BASE = "http://localhost:8000";

// ---------------------------------------------------------------------------
// DOM references
// ---------------------------------------------------------------------------
const queryInput       = document.getElementById("queryInput");
const queryBtn         = document.getElementById("queryBtn");
const speakBtn         = document.getElementById("speakBtn");
const loader           = document.getElementById("loader");
const responseSection  = document.getElementById("responseSection");
const answerBox        = document.getElementById("answerBox");
const entitiesBox      = document.getElementById("entitiesBox");
const entitiesList     = document.getElementById("entitiesList");
const relationshipsBox = document.getElementById("relationshipsBox");
const relTableBody     = document.getElementById("relTableBody");
const statsGrid        = document.getElementById("statsGrid");
const examplesGrid     = document.getElementById("examplesGrid");

// ---------------------------------------------------------------------------
// Text-to-Speech Setup (Offline Voice Assistance)
// ---------------------------------------------------------------------------
let isSpeaking = false;
let currentUtterance = null;

function speakText(text) {
  if (!('speechSynthesis' in window)) {
    alert('Text-to-speech is not supported in your browser.');
    return;
  }

  // Stop any ongoing speech
  if (isSpeaking) {
    window.speechSynthesis.cancel();
    isSpeaking = false;
    speakBtn.textContent = '🔊';
    speakBtn.title = 'Read Answer Aloud';
    return;
  }

  currentUtterance = new SpeechSynthesisUtterance(text);
  currentUtterance.rate = 0.9;
  currentUtterance.pitch = 1.0;
  currentUtterance.lang = 'en-US';

  currentUtterance.onstart = () => {
    isSpeaking = true;
    speakBtn.textContent = '🔇';
    speakBtn.title = 'Stop Speaking';
    speakBtn.classList.add('speaking');
  };

  currentUtterance.onend = () => {
    isSpeaking = false;
    speakBtn.textContent = '🔊';
    speakBtn.title = 'Read Answer Aloud';
    speakBtn.classList.remove('speaking');
  };

  currentUtterance.onerror = () => {
    isSpeaking = false;
    speakBtn.textContent = '🔊';
    speakBtn.title = 'Read Answer Aloud';
    speakBtn.classList.remove('speaking');
  };

  window.speechSynthesis.speak(currentUtterance);
}

// ---------------------------------------------------------------------------
// Submit query
// ---------------------------------------------------------------------------
async function submitQuery(question) {
  if (!question || !question.trim()) return;

  // Show loader, hide previous response
  loader.classList.remove("hidden");
  responseSection.classList.add("hidden");
  queryBtn.disabled = true;

  try {
    const res = await fetch(`${API_BASE}/query`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || `Server error ${res.status}`);
    }

    const data = await res.json();
    renderResponse(data);
  } catch (err) {
    renderError(err.message);
  } finally {
    loader.classList.add("hidden");
    queryBtn.disabled = false;
  }
}

// ---------------------------------------------------------------------------
// Render helpers
// ---------------------------------------------------------------------------
function renderResponse(data) {
  // Answer
  answerBox.textContent = data.answer || "No answer returned.";

  // Entities
  if (data.entities_found && data.entities_found.length > 0) {
    entitiesList.innerHTML = "";
    data.entities_found.forEach(entity => {
      const tag = document.createElement("span");
      tag.className = "tag";
      tag.textContent = entity;
      entitiesList.appendChild(tag);
    });
    entitiesBox.classList.remove("hidden");
  } else {
    entitiesBox.classList.add("hidden");
  }

  // Relationships
  if (data.relationships && data.relationships.length > 0) {
    relTableBody.innerHTML = "";
    // Deduplicate rows
    const seen = new Set();
    data.relationships.forEach(rel => {
      const key = `${rel.source}|${rel.relationship}|${rel.target}`;
      if (seen.has(key)) return;
      seen.add(key);
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${escapeHtml(rel.source)}</td>
        <td><em>${escapeHtml(rel.relationship)}</em></td>
        <td>${escapeHtml(rel.target)}</td>`;
      relTableBody.appendChild(tr);
    });
    relationshipsBox.classList.remove("hidden");
  } else {
    relationshipsBox.classList.add("hidden");
  }

  responseSection.classList.remove("hidden");
  responseSection.scrollIntoView({ behavior: "smooth", block: "start" });
}

function renderError(message) {
  answerBox.textContent = `⚠️ Error: ${message}\n\nMake sure the backend is running at ${API_BASE}`;
  entitiesBox.classList.add("hidden");
  relationshipsBox.classList.add("hidden");
  responseSection.classList.remove("hidden");
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

// ---------------------------------------------------------------------------
// Load graph statistics
// ---------------------------------------------------------------------------
async function loadStats() {
  try {
    const res = await fetch(`${API_BASE}/graph/stats`);
    if (!res.ok) throw new Error("Could not load stats");
    const stats = await res.json();
    renderStats(stats);
  } catch {
    statsGrid.innerHTML = `<p class="loading-text">⚠️ Could not connect to the backend at ${API_BASE}. Start the server with: <code>uvicorn backend.app:app --reload</code></p>`;
  }
}

function renderStats(stats) {
  statsGrid.innerHTML = "";

  const mainCards = [
    { value: stats.total_nodes, label: "Total Entities" },
    { value: stats.total_edges, label: "Total Relationships" },
  ];
  mainCards.forEach(c => statsGrid.appendChild(makeStatCard(c.value, c.label)));

  // Node type breakdown
  if (stats.node_types) {
    Object.entries(stats.node_types).sort((a, b) => b[1] - a[1]).forEach(([type, count]) => {
      statsGrid.appendChild(makeStatCard(count, type.replace(/_/g, " ")));
    });
  }
}

function makeStatCard(value, label) {
  const div = document.createElement("div");
  div.className = "stat-card";
  div.innerHTML = `<div class="stat-value">${value}</div><div class="stat-label">${escapeHtml(label)}</div>`;
  return div;
}

// ---------------------------------------------------------------------------
// Event listeners
// ---------------------------------------------------------------------------
queryBtn.addEventListener("click", () => submitQuery(queryInput.value.trim()));

queryInput.addEventListener("keydown", e => {
  if (e.key === "Enter") submitQuery(queryInput.value.trim());
});

// Speaker button - Read answer aloud (Offline voice assistance)
if (speakBtn) {
  speakBtn.addEventListener("click", () => {
    const text = answerBox.textContent;
    if (text) {
      speakText(text);
    }
  });
}

examplesGrid.addEventListener("click", e => {
  const btn = e.target.closest(".example-btn");
  if (!btn) return;
  queryInput.value = btn.textContent.trim();
  submitQuery(queryInput.value);
});

// ---------------------------------------------------------------------------
// Init
// ---------------------------------------------------------------------------
loadStats();
