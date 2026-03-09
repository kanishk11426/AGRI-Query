"""
FastAPI backend for AgriQuery AI.
"""
from fastapi import FastAPI, HTTPException, Query as QueryParam
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .graph_data import build_graph
from .query_processor import process_query

# ---------------------------------------------------------------------------
# Application setup
# ---------------------------------------------------------------------------

app = FastAPI(
    title="AgriQuery AI",
    description="Intelligent Agricultural Query System with Knowledge Graph",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Build the knowledge graph once at startup
kg = build_graph()


# ---------------------------------------------------------------------------
# Request / Response schemas
# ---------------------------------------------------------------------------

class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    question: str
    answer: str
    entities_found: list
    relationships: list


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/")
def root():
    """Health check endpoint."""
    return {
        "message": "Welcome to AgriQuery AI – Intelligent Agricultural Query System",
        "status": "running",
        "docs": "/docs",
    }


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    """
    Process an agricultural query.

    Accepts a JSON body ``{ "question": "..." }`` and returns a structured
    answer with found entities and relationships.
    """
    if not request.question or not request.question.strip():
        raise HTTPException(status_code=422, detail="Question must not be empty.")

    result = process_query(request.question, kg)
    return result


@app.get("/graph/stats")
def graph_stats():
    """Return statistics about the knowledge graph."""
    return kg.get_graph_stats()


@app.get("/graph/entities")
def graph_entities(entity_type: str = QueryParam(default=None)):
    """
    Return all entities, optionally filtered by *entity_type*.

    Example: ``/graph/entities?entity_type=Crop``
    """
    if entity_type:
        entities = kg.get_entities_by_type(entity_type)
        if not entities and entity_type not in kg.VALID_NODE_TYPES:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid entity type '{entity_type}'. "
                       f"Valid types: {sorted(kg.VALID_NODE_TYPES)}",
            )
        return {"entity_type": entity_type, "entities": entities}
    return {"entities": kg.get_all_entities()}


@app.get("/graph/entity/{name}")
def graph_entity(name: str):
    """
    Return details and relationships for a specific entity.

    Performs a case-insensitive / partial name match.
    """
    matched = kg.find_entity(name)
    if matched is None:
        raise HTTPException(status_code=404, detail=f"Entity '{name}' not found.")
    return kg.get_relationships(matched)
