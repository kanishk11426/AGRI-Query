"""
Unit tests for the AgriculturalKnowledgeGraph class.
"""
import pytest
import sys
import os

# Allow running tests from the repo root with:  pytest tests/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from backend.knowledge_graph import AgriculturalKnowledgeGraph


@pytest.fixture
def empty_kg():
    return AgriculturalKnowledgeGraph()


@pytest.fixture
def kg():
    """A small populated graph used across multiple tests."""
    g = AgriculturalKnowledgeGraph()
    g.add_entity("Rice", "Crop", "Staple cereal crop.")
    g.add_entity("Clay", "Soil_Type", "Heavy, fine-grained soil.")
    g.add_entity("Urea", "Fertilizer", "High-nitrogen fertilizer.")
    g.add_entity("Leaf Blight", "Disease", "Fungal disease causing leaf lesions.")
    g.add_entity("Stem Borer", "Pest", "Larval pest of cereals.")
    g.add_entity("Carbendazim", "Pesticide", "Systemic fungicide.")
    g.add_entity("Drip Irrigation", "Irrigation_Method", "Micro-irrigation method.")
    g.add_entity("Crop Rotation", "Farming_Practice", "Alternating crops each season.")

    g.add_relationship("Rice", "Clay", "grown_in")
    g.add_relationship("Rice", "Urea", "requires")
    g.add_relationship("Rice", "Leaf Blight", "susceptible_to")
    g.add_relationship("Rice", "Stem Borer", "susceptible_to")
    g.add_relationship("Leaf Blight", "Carbendazim", "treated_by")
    g.add_relationship("Rice", "Drip Irrigation", "benefits_from")
    g.add_relationship("Rice", "Crop Rotation", "benefits_from")
    return g


# ---------------------------------------------------------------------------
# add_entity
# ---------------------------------------------------------------------------

class TestAddEntity:
    def test_add_valid_entity(self, empty_kg):
        empty_kg.add_entity("Wheat", "Crop", "Cool-season cereal.")
        assert "Wheat" in empty_kg.graph
        assert empty_kg.graph.nodes["Wheat"]["type"] == "Crop"

    def test_add_entity_stores_description(self, empty_kg):
        empty_kg.add_entity("Sandy", "Soil_Type", "Coarse-textured soil.")
        assert empty_kg.graph.nodes["Sandy"]["description"] == "Coarse-textured soil."

    def test_add_entity_invalid_type_raises(self, empty_kg):
        with pytest.raises(ValueError, match="Invalid entity type"):
            empty_kg.add_entity("Unknown", "Animal", "Not a valid type.")

    def test_add_entity_empty_description(self, empty_kg):
        empty_kg.add_entity("Urea", "Fertilizer")
        assert empty_kg.graph.nodes["Urea"]["description"] == ""


# ---------------------------------------------------------------------------
# add_relationship
# ---------------------------------------------------------------------------

class TestAddRelationship:
    def test_add_valid_relationship(self, kg):
        # grown_in already exists; test a new one
        kg.add_entity("Alluvial", "Soil_Type", "Fertile river soil.")
        kg.add_relationship("Rice", "Alluvial", "grown_in")
        assert kg.graph.has_edge("Rice", "Alluvial")

    def test_add_relationship_invalid_type_raises(self, kg):
        with pytest.raises(ValueError, match="Invalid relationship"):
            kg.add_relationship("Rice", "Clay", "likes")

    def test_add_relationship_missing_source_raises(self, kg):
        with pytest.raises(ValueError, match="Source entity"):
            kg.add_relationship("Corn", "Clay", "grown_in")

    def test_add_relationship_missing_target_raises(self, kg):
        with pytest.raises(ValueError, match="Target entity"):
            kg.add_relationship("Rice", "Sandy", "grown_in")


# ---------------------------------------------------------------------------
# find_entity
# ---------------------------------------------------------------------------

class TestFindEntity:
    def test_exact_match(self, kg):
        assert kg.find_entity("Rice") == "Rice"

    def test_case_insensitive_match(self, kg):
        assert kg.find_entity("rice") == "Rice"
        assert kg.find_entity("UREA") == "Urea"

    def test_partial_match(self, kg):
        result = kg.find_entity("Blight")
        assert result == "Leaf Blight"

    def test_no_match_returns_none(self, kg):
        assert kg.find_entity("Mango") is None


# ---------------------------------------------------------------------------
# get_relationships
# ---------------------------------------------------------------------------

class TestGetRelationships:
    def test_returns_dict_for_known_entity(self, kg):
        result = kg.get_relationships("Rice")
        assert isinstance(result, dict)
        assert result["entity"] == "Rice"

    def test_outgoing_relationships(self, kg):
        result = kg.get_relationships("Rice")
        targets = [e["target"] for e in result["outgoing"]]
        assert "Clay" in targets
        assert "Urea" in targets

    def test_incoming_relationships(self, kg):
        result = kg.get_relationships("Leaf Blight")
        sources = [e["source"] for e in result["incoming"]]
        assert "Rice" in sources

    def test_unknown_entity_returns_empty(self, kg):
        result = kg.get_relationships("Mango")
        assert result == {}


# ---------------------------------------------------------------------------
# get_entities_by_type
# ---------------------------------------------------------------------------

class TestGetEntitiesByType:
    def test_returns_crops(self, kg):
        crops = kg.get_entities_by_type("Crop")
        names = [c["name"] for c in crops]
        assert "Rice" in names

    def test_returns_empty_for_unknown_type(self, kg):
        assert kg.get_entities_by_type("Animal") == []

    def test_returns_only_requested_type(self, kg):
        fertilizers = kg.get_entities_by_type("Fertilizer")
        for f in fertilizers:
            assert f["type"] == "Fertilizer"


# ---------------------------------------------------------------------------
# get_related_entities
# ---------------------------------------------------------------------------

class TestGetRelatedEntities:
    def test_requires_fertilizer(self, kg):
        results = kg.get_related_entities("Rice", "requires")
        names = [r["name"] for r in results]
        assert "Urea" in names

    def test_grown_in_soil(self, kg):
        results = kg.get_related_entities("Rice", "grown_in")
        names = [r["name"] for r in results]
        assert "Clay" in names

    def test_no_relationships_returns_empty(self, kg):
        result = kg.get_related_entities("Rice", "suitable_for")
        assert isinstance(result, list)

    def test_unknown_entity_returns_empty(self, kg):
        assert kg.get_related_entities("Mango", "requires") == []


# ---------------------------------------------------------------------------
# get_path
# ---------------------------------------------------------------------------

class TestGetPath:
    def test_direct_path(self, kg):
        path = kg.get_path("Rice", "Clay")
        assert path is not None
        assert path[0] == "Rice"
        assert path[-1] == "Clay"

    def test_no_path_returns_none(self, kg):
        # Carbendazim has no outgoing edges to Rice in this small graph
        path = kg.get_path("Carbendazim", "Rice")
        assert path is None

    def test_unknown_entity_returns_none(self, kg):
        assert kg.get_path("Mango", "Clay") is None


# ---------------------------------------------------------------------------
# get_graph_stats
# ---------------------------------------------------------------------------

class TestGetGraphStats:
    def test_returns_stats_dict(self, kg):
        stats = kg.get_graph_stats()
        assert "total_nodes" in stats
        assert "total_edges" in stats
        assert "node_types" in stats
        assert "relationship_types" in stats

    def test_node_count_correct(self, kg):
        stats = kg.get_graph_stats()
        assert stats["total_nodes"] == 8

    def test_edge_count_correct(self, kg):
        stats = kg.get_graph_stats()
        assert stats["total_edges"] == 7

    def test_node_types_present(self, kg):
        stats = kg.get_graph_stats()
        assert "Crop" in stats["node_types"]
        assert "Soil_Type" in stats["node_types"]
