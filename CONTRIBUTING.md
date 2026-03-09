# 🤝 Contributing to AgriQuery AI

Thank you for your interest in contributing to AgriQuery AI! This guide will help you get started with development.

---

## 📋 Table of Contents

1. [Quick Start](#-quick-start)
2. [Development Setup](#-development-setup)
3. [Running the Application](#-running-the-application)
4. [Testing](#-testing)
5. [Code Style](#-code-style)
6. [Project Structure](#-project-structure)
7. [Making Contributions](#-making-contributions)
8. [Troubleshooting](#-troubleshooting)

---

## 🚀 Quick Start

Follow these steps to get the project running on your local machine:

### Prerequisites

- **Python 3.9+** (Python 3.12 recommended)
- **Git**
- A modern web browser (Chrome, Firefox, Safari, or Edge)

### Setup in 5 Minutes

```bash
# 1. Clone the repository
git clone https://github.com/kanishk11426/AGRI-Query.git
cd AGRI-Query

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate the virtual environment
source venv/bin/activate          # On macOS/Linux
# OR
venv\Scripts\activate              # On Windows

# 4. Install dependencies
pip install -r backend/requirements.txt

# 5. Verify installation
python3 setup_verify.py

# 6. Start the backend server
uvicorn backend.app:app --reload

# 7. Open the frontend (in another terminal)
# Simply open frontend/index.html in your browser
```

The backend API will be available at `http://localhost:8000` and the interactive API docs at `http://localhost:8000/docs`.

---

## 🛠️ Development Setup

### Step 1: Fork and Clone

```bash
# Fork the repository on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/AGRI-Query.git
cd AGRI-Query
```

### Step 2: Set Up Virtual Environment

**Why use a virtual environment?**
A virtual environment isolates project dependencies from your system Python, preventing conflicts.

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

# Your prompt should now show (venv) prefix
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r backend/requirements.txt

# Verify installation
pip list
```

You should see:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `networkx` - Graph algorithms
- `pydantic` - Data validation
- `pytest` - Testing framework
- `httpx` - HTTP client for tests

### Step 4: Verify Setup

Run the setup verification script to ensure everything is configured correctly:

```bash
python3 setup_verify.py
```

This will check:
- ✅ Python version
- ✅ Virtual environment activation
- ✅ Required packages installation
- ✅ Project structure integrity

---

## 🏃 Running the Application

### Backend Server

```bash
# Start the FastAPI server with auto-reload
uvicorn backend.app:app --reload

# The server will start on http://localhost:8000
# API documentation: http://localhost:8000/docs
```

**What does `--reload` do?**
It automatically restarts the server when you modify Python files, making development faster.

### Frontend

The frontend is a simple static HTML page with no build step required:

```bash
# Option 1: Open directly in browser
open frontend/index.html              # macOS
xdg-open frontend/index.html          # Linux
start frontend/index.html             # Windows

# Option 2: Use Python's built-in server (optional)
cd frontend
python3 -m http.server 8080
# Then visit http://localhost:8080
```

### Testing the API

Try these commands to test if everything works:

```bash
# Health check
curl http://localhost:8000/

# Get graph statistics
curl http://localhost:8000/graph/stats

# Query example
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What fertilizer is best for rice?"}'
```

---

## 🧪 Testing

### Running All Tests

```bash
# Run all tests with verbose output
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=backend --cov-report=html

# Run specific test file
pytest tests/test_knowledge_graph.py -v
pytest tests/test_query_processor.py -v
```

### Test Structure

- `tests/test_knowledge_graph.py` - Tests for graph operations (30 tests)
- `tests/test_query_processor.py` - Tests for query processing (26 tests)

### Writing New Tests

When adding new features, please include tests:

```python
# Example test structure
def test_new_feature():
    # Arrange - Set up test data
    graph = KnowledgeGraph()

    # Act - Execute the feature
    result = graph.some_new_method()

    # Assert - Verify results
    assert result is not None
    assert len(result) > 0
```

---

## 🎨 Code Style

### Python Code Style

We follow **PEP 8** style guidelines:

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use descriptive variable names
- Add docstrings to functions and classes
- Type hints are encouraged

**Example:**

```python
def get_related_entities(
    self,
    entity_name: str,
    relationship_type: str = None
) -> list[dict]:
    """
    Get all entities related to the specified entity.

    Args:
        entity_name: Name of the entity to query
        relationship_type: Optional filter for relationship type

    Returns:
        List of related entities with relationship information
    """
    # Implementation here
    pass
```

### Frontend Code Style

- Use consistent indentation (2 spaces for HTML/CSS/JS)
- Use semantic HTML elements
- Keep JavaScript functions small and focused
- Add comments for complex logic

---

## 📁 Project Structure

Understanding the codebase:

```
AGRI-Query/
├── backend/
│   ├── __init__.py
│   ├── app.py                    # FastAPI application & endpoints
│   ├── knowledge_graph.py        # Graph data structure & operations
│   ├── query_processor.py        # NLP query processing logic
│   ├── graph_data.py             # Agricultural data (entities & relationships)
│   └── requirements.txt          # Python dependencies
├── frontend/
│   ├── index.html                # Main web interface
│   ├── style.css                 # Styling and themes
│   └── script.js                 # API calls & UI interactions
├── tests/
│   ├── test_knowledge_graph.py   # Graph operation tests
│   └── test_query_processor.py   # Query processing tests
├── .gitignore
├── README.md                      # Project overview
├── CONTRIBUTING.md               # This file
└── setup_verify.py               # Environment verification script
```

### Key Components

1. **Knowledge Graph** (`backend/knowledge_graph.py`)
   - Uses NetworkX for graph operations
   - Stores entities (crops, soils, fertilizers, etc.)
   - Manages relationships between entities

2. **Query Processor** (`backend/query_processor.py`)
   - Extracts entities from user questions
   - Determines query intent (what/which/how/tell)
   - Generates natural language responses

3. **Graph Data** (`backend/graph_data.py`)
   - Contains all agricultural domain knowledge
   - Defines entities and their relationships
   - Easy to extend with new data

4. **API Layer** (`backend/app.py`)
   - FastAPI endpoints for queries and graph operations
   - CORS enabled for frontend communication
   - Auto-generated API documentation

---

## 🔨 Making Contributions

### 1. Pick an Issue

- Check the [Issues](https://github.com/kanishk11426/AGRI-Query/issues) page
- Look for issues labeled `good first issue` or `help wanted`
- Comment on the issue to let others know you're working on it

### 2. Create a Branch

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/bug-description
```

### 3. Make Your Changes

- Write clean, well-documented code
- Follow the code style guidelines
- Add tests for new features
- Update documentation if needed

### 4. Test Your Changes

```bash
# Run all tests
pytest tests/ -v

# Test manually with the API
uvicorn backend.app:app --reload
# Then test in browser or with curl
```

### 5. Commit Your Changes

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Add feature: description of what you added"

# Good commit message examples:
# "Add new relationship type for crop rotation"
# "Fix bug in entity extraction for multi-word queries"
# "Update README with installation troubleshooting"
```

### 6. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Then create a Pull Request on GitHub
```

**Pull Request Guidelines:**
- Describe what changes you made and why
- Reference any related issues (`Fixes #123`)
- Include screenshots for UI changes
- Ensure all tests pass

---

## 🔧 Troubleshooting

### Common Issues

#### 1. "Command not found: uvicorn"

**Solution:** Make sure your virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate    # or venv\Scripts\activate on Windows
pip install -r backend/requirements.txt
```

#### 2. "Module not found" errors

**Solution:** Ensure you're running commands from the project root directory and the virtual environment is active:
```bash
cd AGRI-Query
source venv/bin/activate
```

#### 3. Port 8000 already in use

**Solution:** Either kill the process using port 8000 or use a different port:
```bash
# Use different port
uvicorn backend.app:app --reload --port 8001

# Or find and kill the process (Linux/macOS)
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

#### 4. CORS errors in browser

**Solution:** The backend is configured to allow all origins. If you still see CORS errors:
- Make sure the backend server is running
- Check that you're using the correct API URL in `frontend/script.js`
- Try opening `frontend/index.html` directly instead of through a file:// URL

#### 5. Tests failing

**Solution:**
```bash
# Update dependencies
pip install --upgrade -r backend/requirements.txt

# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name '*.pyc' -delete

# Run tests again
pytest tests/ -v
```

#### 6. Virtual environment issues

**Solution:** Recreate the virtual environment:
```bash
# Deactivate current environment
deactivate

# Remove old environment
rm -rf venv

# Create new environment
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

### Getting Help

If you're stuck:
1. Check the [README.md](README.md) for basic setup
2. Look through existing [Issues](https://github.com/kanishk11426/AGRI-Query/issues)
3. Create a new issue with:
   - Your operating system
   - Python version (`python3 --version`)
   - Error message (full output)
   - Steps you've already tried

---

## 💡 Ideas for Contributions

Not sure where to start? Here are some ideas:

### Beginner-Friendly
- Add more crops, soils, or diseases to `graph_data.py`
- Improve error messages in the API
- Add more example queries to README
- Fix typos in documentation
- Add more unit tests

### Intermediate
- Add support for more complex queries
- Improve entity extraction algorithm
- Add data validation for graph inputs
- Create more informative error responses
- Add logging throughout the application

### Advanced
- Implement graph visualization with D3.js
- Add caching layer for frequent queries
- Integrate with external APIs (weather, market prices)
- Add user authentication
- Create Docker configuration
- Add CI/CD pipeline

---

## 📝 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Follow the code style guidelines
- Write meaningful commit messages

---

## 📞 Contact

- **Issues:** [GitHub Issues](https://github.com/kanishk11426/AGRI-Query/issues)
- **Repository:** [kanishk11426/AGRI-Query](https://github.com/kanishk11426/AGRI-Query)

---

Thank you for contributing to AgriQuery AI! 🌾 Every contribution, no matter how small, helps make this project better for everyone.
