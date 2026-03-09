# 🌾 AgriQuery AI – Intelligent Agricultural Query System

AgriQuery AI is a full-stack application that helps farmers, agronomists, and enthusiasts obtain instant, knowledge-graph–powered answers to agricultural questions — completely offline, with no external LLM API required.

---

## ✨ Features

- **Knowledge Graph engine** built with NetworkX containing 50+ agricultural entities and 150+ relationships
- **Natural language query processing** using keyword matching and intent heuristics
- **FastAPI backend** with auto-generated interactive API docs (`/docs`)
- **Responsive, agriculture-themed frontend** (HTML + CSS + Vanilla JS)
- **No external dependencies** — runs entirely offline after `pip install`
- **Comprehensive test suite** (56 unit tests)

---

## 🏗️ Architecture

```
User Browser
    │
    │  HTTP (JSON)
    ▼
FastAPI (backend/app.py)
    │
    ├── Query Processor (backend/query_processor.py)
    │       │
    │       └── Entity extraction  →  Intent detection  →  Response generation
    │
    └── Knowledge Graph (backend/knowledge_graph.py)
            │
            └── NetworkX DiGraph  ←  Pre-populated by (backend/graph_data.py)
```

---

## 📚 Knowledge Graph

The graph contains nodes of **8 types**:

| Type | Examples |
|------|---------|
| Crop | Rice, Wheat, Tomato, Cotton, Maize, Sugarcane, Potato, Soybean … |
| Soil_Type | Clay, Sandy, Loamy, Black (Regur), Red, Alluvial, Laterite |
| Fertilizer | Urea, DAP, Potash (MOP), NPK Complex, Vermicompost … |
| Disease | Leaf Blight, Rust, Powdery Mildew, Wilt, Late Blight … |
| Pest | Stem Borer, Whitefly, Aphid, Bollworm, Thrips … |
| Pesticide | Fungicide, Carbendazim, Mancozeb, Bordeaux Mixture … |
| Irrigation_Method | Drip Irrigation, Flood Irrigation, Sprinkler Irrigation … |
| Farming_Practice | Crop Rotation, Mulching, Intercropping, Organic Farming … |

**Relationship types:** `requires` · `susceptible_to` · `suitable_for` · `affects` · `treated_by` · `benefits_from` · `grown_in` · `prevented_by`

**Example relationships:**
- `Rice` —[grown_in]→ `Clay`
- `Rice` —[requires]→ `Urea`
- `Tomato` —[susceptible_to]→ `Late Blight`
- `Late Blight` —[treated_by]→ `Bordeaux Mixture`
- `Cotton` —[benefits_from]→ `Drip Irrigation`

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.9+

### 1. Clone the repository
```bash
git clone https://github.com/kanishk11426/AGRI-Query.git
cd AGRI-Query
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r backend/requirements.txt
```

### 4. Start the backend
```bash
uvicorn backend.app:app --reload
```

The API is now available at **http://localhost:8000**  
Interactive docs: **http://localhost:8000/docs**

### 5. Open the frontend
Simply open `frontend/index.html` in your browser (no build step required):
```bash
open frontend/index.html          # macOS
xdg-open frontend/index.html      # Linux
start frontend/index.html         # Windows
```

---

## 📡 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/query` | Process a natural language query |
| GET | `/graph/stats` | Knowledge graph statistics |
| GET | `/graph/entities` | List all entities (optional `?entity_type=Crop`) |
| GET | `/graph/entity/{name}` | Details & relationships for a specific entity |

### POST /query

**Request:**
```json
{ "question": "What fertilizer is best for rice?" }
```

**Response:**
```json
{
  "question": "What fertilizer is best for rice?",
  "answer": "**Rice** (Crop)\nStaple cereal crop...\n  • Requires fertilizer(s): Urea and DAP\n...",
  "entities_found": ["Rice"],
  "relationships": [
    { "source": "Rice", "relationship": "requires", "target": "Urea" },
    { "source": "Rice", "relationship": "requires", "target": "DAP" }
  ]
}
```

---

## 💬 Example Queries

| Query | What it demonstrates |
|-------|---------------------|
| `What fertilizer is best for rice?` | Crop → Fertilizer relationships |
| `Which pests affect tomato plants?` | Crop → Pest relationships |
| `What diseases affect cotton?` | Crop → Disease relationships |
| `Which soil type is suitable for wheat?` | Crop → Soil relationships |
| `How to treat leaf blight?` | Disease → Pesticide (treated_by) |
| `Tell me about drip irrigation` | Irrigation method details |
| `What crops grow well in clay soil?` | Soil → Crop (suitable_for) |
| `What causes yellow leaves in paddy?` | Alias + disease detection |

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

Tests cover:
- `tests/test_knowledge_graph.py` – 30 unit tests for all graph methods
- `tests/test_query_processor.py` – 26 unit tests for intent detection, entity extraction, and query processing

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|-----------|
| Backend API | Python 3.9+, FastAPI, Uvicorn |
| Knowledge Graph | NetworkX |
| Data Validation | Pydantic v2 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Testing | pytest |

---

## 📁 Project Structure

```
AGRI-Query/
├── backend/
│   ├── __init__.py
│   ├── app.py               # FastAPI server
│   ├── knowledge_graph.py   # NetworkX graph engine
│   ├── query_processor.py   # NLP-like query processing
│   ├── graph_data.py        # Pre-populated agricultural data
│   └── requirements.txt
├── frontend/
│   ├── index.html           # Main web interface
│   ├── style.css            # Agriculture-themed styling
│   └── script.js            # Frontend logic
├── tests/
│   ├── test_knowledge_graph.py
│   └── test_query_processor.py
├── .gitignore
└── README.md
```

---

## 🔮 Future Enhancements

- Integrate a local LLM (e.g., Ollama + Llama 3) for richer answers
- Interactive graph visualisation with D3.js or Vis.js
- Multi-language support for regional farmers
- REST API authentication & rate limiting
- Docker Compose deployment
- Weather API integration for seasonal crop recommendations
- Mobile-first Progressive Web App

---

## 📄 License

This project is licensed under the **MIT License**.
