"""
Agricultural Knowledge Graph Engine using NetworkX.
"""
import networkx as nx
from typing import Optional


class AgriculturalKnowledgeGraph:
    """NetworkX-based directed graph for agricultural domain knowledge."""

    VALID_NODE_TYPES = {
        "Crop", "Soil_Type", "Fertilizer", "Disease",
        "Pest", "Pesticide", "Irrigation_Method", "Farming_Practice",
    }

    VALID_RELATIONSHIPS = {
        "requires", "susceptible_to", "suitable_for", "affects",
        "treated_by", "benefits_from", "grown_in", "prevented_by",
    }

    def __init__(self):
        self.graph = nx.DiGraph()

    # ------------------------------------------------------------------
    # Mutation helpers
    # ------------------------------------------------------------------

    def add_entity(self, name: str, entity_type: str, description: str = "") -> None:
        """Add a node to the knowledge graph."""
        if entity_type not in self.VALID_NODE_TYPES:
            raise ValueError(f"Invalid entity type '{entity_type}'. "
                             f"Valid types: {self.VALID_NODE_TYPES}")
        self.graph.add_node(
            name,
            name=name,
            type=entity_type,
            description=description,
        )

    def add_relationship(self, source: str, target: str, relationship: str) -> None:
        """Add a directed edge between two entities."""
        if relationship not in self.VALID_RELATIONSHIPS:
            raise ValueError(f"Invalid relationship '{relationship}'. "
                             f"Valid relationships: {self.VALID_RELATIONSHIPS}")
        if source not in self.graph:
            raise ValueError(f"Source entity '{source}' not found in graph.")
        if target not in self.graph:
            raise ValueError(f"Target entity '{target}' not found in graph.")
        self.graph.add_edge(source, target, relationship=relationship)

    # ------------------------------------------------------------------
    # Query helpers
    # ------------------------------------------------------------------

    def find_entity(self, name: str) -> Optional[str]:
        """Find an entity by exact match first, then case-insensitive / partial match."""
        if name in self.graph:
            return name
        name_lower = name.lower()
        # Case-insensitive exact match
        for node in self.graph.nodes:
            if node.lower() == name_lower:
                return node
        # Partial match
        for node in self.graph.nodes:
            if name_lower in node.lower():
                return node
        return None

    def find_entities(self, name: str) -> list:
        """Return all entities that match (case-insensitive / partial)."""
        name_lower = name.lower()
        matches = []
        for node in self.graph.nodes:
            if name_lower in node.lower():
                matches.append(node)
        return matches

    def get_relationships(self, entity_name: str) -> dict:
        """Return all incoming and outgoing relationships for an entity."""
        node = self.find_entity(entity_name)
        if node is None:
            return {}

        outgoing = [
            {
                "target": target,
                "relationship": self.graph[node][target].get("relationship"),
                "target_type": self.graph.nodes[target].get("type"),
            }
            for target in self.graph.successors(node)
        ]
        incoming = [
            {
                "source": source,
                "relationship": self.graph[source][node].get("relationship"),
                "source_type": self.graph.nodes[source].get("type"),
            }
            for source in self.graph.predecessors(node)
        ]
        node_data = dict(self.graph.nodes[node])
        return {
            "entity": node,
            "attributes": node_data,
            "outgoing": outgoing,
            "incoming": incoming,
        }

    def get_entities_by_type(self, entity_type: str) -> list:
        """Return all entities of a given type."""
        return [
            dict(self.graph.nodes[n])
            for n in self.graph.nodes
            if self.graph.nodes[n].get("type") == entity_type
        ]

    def get_related_entities(self, entity_name: str, relationship_type: str) -> list:
        """Return entities connected to *entity_name* by *relationship_type*."""
        node = self.find_entity(entity_name)
        if node is None:
            return []
        results = []
        for target in self.graph.successors(node):
            if self.graph[node][target].get("relationship") == relationship_type:
                results.append(dict(self.graph.nodes[target]))
        # Also check reverse direction
        for source in self.graph.predecessors(node):
            if self.graph[source][node].get("relationship") == relationship_type:
                results.append(dict(self.graph.nodes[source]))
        return results

    def get_path(self, source: str, target: str) -> Optional[list]:
        """Return the shortest path between two entities, or None if no path exists."""
        src = self.find_entity(source)
        tgt = self.find_entity(target)
        if src is None or tgt is None:
            return None
        try:
            path = nx.shortest_path(self.graph, src, tgt)
            return path
        except nx.NetworkXNoPath:
            return None
        except nx.NodeNotFound:
            return None

    def get_graph_stats(self) -> dict:
        """Return statistics about the knowledge graph."""
        type_counts: dict = {}
        for n in self.graph.nodes:
            t = self.graph.nodes[n].get("type", "Unknown")
            type_counts[t] = type_counts.get(t, 0) + 1

        rel_counts: dict = {}
        for _, _, data in self.graph.edges(data=True):
            r = data.get("relationship", "unknown")
            rel_counts[r] = rel_counts.get(r, 0) + 1

        return {
            "total_nodes": self.graph.number_of_nodes(),
            "total_edges": self.graph.number_of_edges(),
            "node_types": type_counts,
            "relationship_types": rel_counts,
        }

    def get_all_entities(self) -> list:
        """Return all entities with their attributes."""
        return [dict(self.graph.nodes[n]) for n in self.graph.nodes]
