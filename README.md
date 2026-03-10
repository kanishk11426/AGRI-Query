# 🌾 AgriQuery AI – Intelligent Agricultural Query System

AgriQuery AI is a full-stack application that helps farmers, agronomists, and enthusiasts obtain instant, knowledge-graph–powered answers to agricultural questions — completely offline, with no external LLM API required.

---

## ✨ Features

- **Comprehensive Knowledge Graph** with 129 agricultural entities and 366+ relationships covering crops, pests, diseases, and treatments
- **Natural language query processing** using keyword matching and intent heuristics
- **Offline Voice Assistance** with text-to-speech output for hands-free listening
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

The graph contains **129 entities** across **8 types**:

| Type | Count | Examples |
|------|-------|----------|
| Crop | 30 | Rice, Wheat, Tomato, Cotton, Mango, Banana, Papaya, Grapes, Citrus, Tea, Coffee, Chilli, Brinjal, Cabbage … |
| Soil_Type | 7 | Clay, Sandy, Loamy, Black (Regur), Red, Alluvial, Laterite |
| Fertilizer | 15 | Urea, DAP, NPK Complex, Vermicompost, Compost, Farmyard Manure, Biofertilizer, Boron Fertilizer … |
| Disease | 20 | Leaf Blight, Rust, Powdery Mildew, Wilt, Late Blight, Anthracnose, Fusarium Wilt, Panama Disease … |
| Pest | 20 | Stem Borer, Whitefly, Aphid, Bollworm, Armyworm, Jassid, Mealybug, Diamondback Moth, Fruit Fly … |
| Pesticide | 18 | Fungicide, Insecticide, Neem Oil, Bordeaux Mixture, Bacillus thuringiensis, Trichoderma, Spinosad … |
| Irrigation_Method | 7 | Drip Irrigation, Flood Irrigation, Sprinkler Irrigation, Furrow Irrigation, Rainwater Harvesting … |
| Farming_Practice | 12 | Crop Rotation, Mulching, Intercropping, Organic Farming, IPM, Precision Agriculture, Greenhouse … |

**Relationship types:** `requires` · `susceptible_to` · `suitable_for` · `affects` · `treated_by` · `benefits_from` · `grown_in` · `prevented_by`

**Example relationships:**
- `Rice` —[grown_in]→ `Clay`
- `Rice` —[requires]→ `Urea`
- `Tomato` —[susceptible_to]→ `Late Blight`
- `Late Blight` —[treated_by]→ `Bordeaux Mixture`
- `Cotton` —[benefits_from]→ `Drip Irrigation`

---

## 🚀 Quick Start

### Automated Setup (Recommended)

Run the quick start script to automatically set up your environment:

```bash
git clone https://github.com/kanishk11426/AGRI-Query.git
cd AGRI-Query
./quick_start.sh
```

This will:
- Create a virtual environment
- Install all dependencies
- Verify your setup

### Manual Setup

#### Prerequisites
- Python 3.9+

#### 1. Clone the repository
```bash
git clone https://github.com/kanishk11426/AGRI-Query.git
cd AGRI-Query
```

#### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

#### 3. Install dependencies
```bash
pip install -r backend/requirements.txt
```

#### 4. Verify setup (optional but recommended)
```bash
python3 setup_verify.py
```

#### 5. Start the backend
```bash
uvicorn backend.app:app --reload
```

The API is now available at **http://localhost:8000**
Interactive docs: **http://localhost:8000/docs**

#### 6. Open the frontend
Simply open `frontend/index.html` in your browser (no build step required):
```bash
open frontend/index.html          # macOS
xdg-open frontend/index.html      # Linux
start frontend/index.html         # Windows
```

---

## 🎤 Voice Assistance (Offline)

AgriQuery AI includes **fully offline** text-to-speech voice assistance for hands-free listening:

### Text-to-Speech (TTS) - Fully Offline
- **Speaker Button (🔊)**: Click the speaker button in the answer section to hear the response read aloud
- **Toggle Control**: Click again to stop the speech output
- **Natural Voice**: Uses the browser's built-in speech synthesis for natural-sounding responses
- **Completely Offline**: Works without any internet connection using your device's built-in voices

### Usage Tips
- **No Internet Required**: Text-to-speech works entirely offline once the page is loaded
- **Browser Compatibility**: All modern browsers (Chrome, Firefox, Edge, Safari)
- **Accessible**: Helps users who prefer audio feedback or have visual impairments
- **Hands-Free Listening**: Listen to answers while working in the field

### Why No Speech-to-Text?
To maintain the project's commitment to **fully offline operation**, we've excluded speech-to-text (voice input) because:
- Web Speech API's speech recognition requires internet connectivity in most browsers
- Adding offline speech recognition would require large ML models (~100MB+)
- Text input is simple, fast, and works reliably offline

Users can type their queries or use the example query buttons for quick access.

---

## 🤝 Contributing

Want to contribute to AgriQuery AI? Check out our [**Contributing Guide**](CONTRIBUTING.md) for:
- Detailed setup instructions
- Development workflow
- Code style guidelines
- Testing procedures
- Troubleshooting tips

We welcome contributions of all kinds — from bug fixes to new features!

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
| `What fertilizer does mango need?` | New fruit crop query |
| `Which pests attack banana?` | Tropical crop pest relationships |
| `How to treat anthracnose in chilli?` | Disease treatment for vegetables |
| `What is integrated pest management?` | Modern farming practice info |
| `Which crops benefit from greenhouse farming?` | Advanced farming technique |
| `How to control diamondback moth in cabbage?` | Biological pest control |

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
├── CONTRIBUTING.md          # Contribution guidelines
├── README.md                # This file
├── quick_start.sh           # Automated setup script
└── setup_verify.py          # Environment verification tool
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
