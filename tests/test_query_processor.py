"""
Unit tests for the query processor.
"""
import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from backend.knowledge_graph import AgriculturalKnowledgeGraph
from backend.query_processor import extract_entities, process_query, _match_intents


# ---------------------------------------------------------------------------
# Shared fixture
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def kg():
    """Populated knowledge graph for query processor tests."""
    g = AgriculturalKnowledgeGraph()

    g.add_entity("Rice", "Crop", "Staple cereal crop.")
    g.add_entity("Wheat", "Crop", "Cool-season cereal crop.")
    g.add_entity("Tomato", "Crop", "Warm-season vegetable.")
    g.add_entity("Cotton", "Crop", "Fibre crop.")
    g.add_entity("Potato", "Crop", "Cool-season root vegetable.")

    g.add_entity("Clay", "Soil_Type", "Heavy, fine-grained soil.")
    g.add_entity("Alluvial", "Soil_Type", "Fertile river-deposited soil.")
    g.add_entity("Loamy", "Soil_Type", "Balanced soil mixture.")

    g.add_entity("Urea", "Fertilizer", "High-nitrogen fertilizer.")
    g.add_entity("DAP", "Fertilizer", "Di-ammonium phosphate.")
    g.add_entity("NPK Complex", "Fertilizer", "Balanced NPK fertilizer.")

    g.add_entity("Leaf Blight", "Disease", "Fungal disease.")
    g.add_entity("Late Blight", "Disease", "Oomycete disease destructive to potatoes.")
    g.add_entity("Rust", "Disease", "Fungal pustule disease.")
    g.add_entity("Wilt", "Disease", "Soil-borne wilt disease.")
    g.add_entity("Mosaic Virus", "Disease", "Viral mottling disease.")

    g.add_entity("Stem Borer", "Pest", "Larval cereal pest.")
    g.add_entity("Aphid", "Pest", "Sucking pest.")
    g.add_entity("Whitefly", "Pest", "Viral vector pest.")
    g.add_entity("Bollworm", "Pest", "Cotton pest.")

    g.add_entity("Carbendazim", "Pesticide", "Systemic fungicide.")
    g.add_entity("Mancozeb", "Pesticide", "Contact fungicide.")
    g.add_entity("Bordeaux Mixture", "Pesticide", "Copper-based fungicide.")
    g.add_entity("Imidacloprid", "Pesticide", "Neonicotinoid insecticide.")
    g.add_entity("Neem Oil", "Pesticide", "Organic botanical pesticide.")

    g.add_entity("Drip Irrigation", "Irrigation_Method", "Micro-irrigation.")
    g.add_entity("Flood Irrigation", "Irrigation_Method", "Traditional flooding method.")
    g.add_entity("Sprinkler Irrigation", "Irrigation_Method", "Overhead sprinkler.")

    g.add_entity("Crop Rotation", "Farming_Practice", "Alternating crops.")
    g.add_entity("Mulching", "Farming_Practice", "Covering soil surface.")

    # Relationships
    g.add_relationship("Rice", "Clay", "grown_in")
    g.add_relationship("Rice", "Alluvial", "grown_in")
    g.add_relationship("Rice", "Urea", "requires")
    g.add_relationship("Rice", "DAP", "requires")
    g.add_relationship("Rice", "Leaf Blight", "susceptible_to")
    g.add_relationship("Rice", "Stem Borer", "susceptible_to")
    g.add_relationship("Rice", "Flood Irrigation", "benefits_from")
    g.add_relationship("Rice", "Crop Rotation", "benefits_from")

    g.add_relationship("Wheat", "Alluvial", "grown_in")
    g.add_relationship("Wheat", "Loamy", "grown_in")
    g.add_relationship("Wheat", "Urea", "requires")
    g.add_relationship("Wheat", "Rust", "susceptible_to")
    g.add_relationship("Wheat", "Aphid", "susceptible_to")
    g.add_relationship("Wheat", "Sprinkler Irrigation", "benefits_from")

    g.add_relationship("Tomato", "Loamy", "grown_in")
    g.add_relationship("Tomato", "NPK Complex", "requires")
    g.add_relationship("Tomato", "Late Blight", "susceptible_to")
    g.add_relationship("Tomato", "Mosaic Virus", "susceptible_to")
    g.add_relationship("Tomato", "Whitefly", "susceptible_to")
    g.add_relationship("Tomato", "Drip Irrigation", "benefits_from")
    g.add_relationship("Tomato", "Mulching", "benefits_from")

    g.add_relationship("Cotton", "Wilt", "susceptible_to")
    g.add_relationship("Cotton", "Bollworm", "susceptible_to")
    g.add_relationship("Cotton", "Drip Irrigation", "benefits_from")

    g.add_relationship("Potato", "Late Blight", "susceptible_to")
    g.add_relationship("Potato", "Sprinkler Irrigation", "benefits_from")

    g.add_relationship("Leaf Blight", "Carbendazim", "treated_by")
    g.add_relationship("Leaf Blight", "Mancozeb", "treated_by")
    g.add_relationship("Rust", "Mancozeb", "treated_by")
    g.add_relationship("Late Blight", "Bordeaux Mixture", "treated_by")
    g.add_relationship("Late Blight", "Mancozeb", "treated_by")
    g.add_relationship("Mosaic Virus", "Imidacloprid", "treated_by")
    g.add_relationship("Wilt", "Carbendazim", "treated_by")
    g.add_relationship("Aphid", "Neem Oil", "treated_by")
    g.add_relationship("Whitefly", "Imidacloprid", "treated_by")
    g.add_relationship("Bollworm", "Imidacloprid", "treated_by")

    g.add_relationship("Clay", "Rice", "suitable_for")
    g.add_relationship("Alluvial", "Rice", "suitable_for")
    g.add_relationship("Alluvial", "Wheat", "suitable_for")
    g.add_relationship("Loamy", "Tomato", "suitable_for")
    g.add_relationship("Loamy", "Wheat", "suitable_for")

    return g


# ---------------------------------------------------------------------------
# _match_intents
# ---------------------------------------------------------------------------

class TestMatchIntents:
    def test_fertilizer_intent(self):
        assert "fertilizer" in _match_intents("What fertilizer is good for rice?")

    def test_pest_intent(self):
        assert "pest" in _match_intents("Which pests affect tomato?")

    def test_disease_intent(self):
        assert "disease" in _match_intents("What diseases affect cotton?")

    def test_soil_intent(self):
        assert "soil" in _match_intents("Which soil type is suitable for wheat?")

    def test_treatment_intent(self):
        assert "treatment" in _match_intents("How to treat leaf blight?")

    def test_irrigation_intent(self):
        assert "irrigation" in _match_intents("Tell me about drip irrigation")

    def test_multiple_intents(self):
        intents = _match_intents("What fertilizer and pest control does rice need?")
        assert "fertilizer" in intents
        assert "pest" in intents

    def test_no_match_returns_empty(self):
        intents = _match_intents("Hello world!")
        assert intents == []


# ---------------------------------------------------------------------------
# extract_entities
# ---------------------------------------------------------------------------

class TestExtractEntities:
    def test_extracts_crop_name(self, kg):
        entities = extract_entities("What fertilizer is best for Rice?", kg)
        assert "Rice" in entities

    def test_extracts_disease_name(self, kg):
        entities = extract_entities("How to treat Leaf Blight?", kg)
        assert "Leaf Blight" in entities

    def test_extracts_soil_type(self, kg):
        entities = extract_entities("What crops grow in Clay soil?", kg)
        assert "Clay" in entities

    def test_paddy_alias(self, kg):
        entities = extract_entities("What disease affects paddy crops?", kg)
        assert "Rice" in entities

    def test_no_entity_found_returns_empty(self, kg):
        entities = extract_entities("What is the weather today?", kg)
        assert entities == []

    def test_case_insensitive_extraction(self, kg):
        entities = extract_entities("tell me about wheat", kg)
        assert "Wheat" in entities


# ---------------------------------------------------------------------------
# process_query
# ---------------------------------------------------------------------------

class TestProcessQuery:
    def test_fertilizer_query_rice(self, kg):
        result = process_query("What fertilizer is best for rice?", kg)
        assert result["question"] == "What fertilizer is best for rice?"
        assert "Rice" in result["entities_found"]
        assert any(
            r["relationship"] == "requires" for r in result["relationships"]
        )
        assert "Urea" in result["answer"] or "DAP" in result["answer"]

    def test_pest_query_tomato(self, kg):
        result = process_query("Which pests affect tomato plants?", kg)
        assert "Tomato" in result["entities_found"]
        assert "Whitefly" in result["answer"]

    def test_disease_query_cotton(self, kg):
        result = process_query("What diseases affect cotton?", kg)
        assert "Cotton" in result["entities_found"]
        assert "Wilt" in result["answer"] or "Bollworm" in result["answer"]

    def test_soil_query_wheat(self, kg):
        result = process_query("Which soil type is suitable for wheat?", kg)
        assert "Wheat" in result["entities_found"]
        assert "Alluvial" in result["answer"] or "Loamy" in result["answer"]

    def test_treatment_query_leaf_blight(self, kg):
        result = process_query("How to treat leaf blight?", kg)
        assert "Leaf Blight" in result["entities_found"]
        assert "Carbendazim" in result["answer"] or "Mancozeb" in result["answer"]

    def test_irrigation_query(self, kg):
        result = process_query("Tell me about drip irrigation", kg)
        assert "Drip Irrigation" in result["entities_found"]
        assert result["answer"] != ""

    def test_crops_in_clay_soil(self, kg):
        result = process_query("What crops grow well in clay soil?", kg)
        assert "Clay" in result["entities_found"]

    def test_paddy_alias_query(self, kg):
        result = process_query("What causes disease in paddy crop?", kg)
        assert "Rice" in result["entities_found"]

    def test_empty_query_returns_prompt(self, kg):
        result = process_query("", kg)
        assert "Please enter" in result["answer"]
        assert result["entities_found"] == []

    def test_unknown_query_returns_fallback(self, kg):
        result = process_query("xyz123 foobar", kg)
        assert result["entities_found"] == []
        assert result["answer"] != ""

    def test_response_has_required_keys(self, kg):
        result = process_query("Tell me about rice", kg)
        assert "question" in result
        assert "answer" in result
        assert "entities_found" in result
        assert "relationships" in result

    def test_relationships_list_structure(self, kg):
        result = process_query("What fertilizer does rice need?", kg)
        for rel in result["relationships"]:
            assert "source" in rel
            assert "relationship" in rel
            assert "target" in rel
