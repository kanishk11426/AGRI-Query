"""
Query Processor for AgriQuery AI.

Extracts agricultural entities from natural language queries and generates
human-readable responses using the knowledge graph.
"""
from __future__ import annotations

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .knowledge_graph import AgriculturalKnowledgeGraph


# ---------------------------------------------------------------------------
# Intent patterns
# ---------------------------------------------------------------------------

INTENT_PATTERNS = {
    "fertilizer": [
        r"\bfertili[sz]er\b", r"\bnutrient\b", r"\bmanure\b", r"\burea\b",
        r"\bdap\b", r"\bnpk\b", r"\bpotash\b", r"\bvermicompost\b",
        r"\bsuperphosphate\b",
    ],
    "pest": [
        r"\bpests?\b", r"\binsects?\b", r"\bbug\b", r"\bworm\b", r"\bborer\b",
        r"\baphid\b", r"\bwhitefly\b", r"\bbollworm\b", r"\bthrips\b",
        r"\blocust\b", r"\bmite\b", r"\bleaf miner\b",
    ],
    "disease": [
        r"\bdiseases?\b", r"\bblight\b", r"\brust\b", r"\bmildew\b",
        r"\bwilt\b", r"\bvirus\b", r"\brot\b", r"\bsmut\b", r"\bcanker\b",
        r"\binfect\b", r"\bpathogen\b", r"\byellow\b", r"\bspot\b",
    ],
    "soil": [
        r"\bsoil\b", r"\bclay\b", r"\bsandy\b", r"\bloamy\b",
        r"\balluvial\b", r"\blaterite\b", r"\bblack soil\b", r"\bred soil\b",
    ],
    "treatment": [
        r"\btreat\b", r"\bcure\b", r"\bcontrol\b", r"\bpesticide\b",
        r"\bfungicide\b", r"\binsecticide\b", r"\bspray\b", r"\bapply\b",
        r"\bmanage\b", r"\bprevent\b",
    ],
    "irrigation": [
        r"\birrigation\b", r"\bwater\b", r"\bdrip\b", r"\bflood\b",
        r"\bsprinkler\b", r"\bfurrow\b",
    ],
    "practice": [
        r"\brotation\b", r"\bmulch\b", r"\bintercrop\b", r"\borganic\b",
        r"\btillage\b", r"\bcover crop\b", r"\bfarming practice\b",
    ],
    "general": [
        r"\bwhat\b", r"\bhow\b", r"\bwhich\b", r"\btell\b", r"\babout\b",
        r"\bsuggest\b", r"\brecommend\b",
    ],
}


def _match_intents(query: str) -> list[str]:
    """Return a list of matched intents for a query (lowercase)."""
    q = query.lower()
    matched = []
    for intent, patterns in INTENT_PATTERNS.items():
        if intent == "general":
            continue
        for pattern in patterns:
            if re.search(pattern, q):
                matched.append(intent)
                break
    return matched


def extract_entities(query: str, kg: "AgriculturalKnowledgeGraph") -> list[str]:
    """
    Extract agricultural entity names from a natural language query.
    Returns a list of matched node names.
    """
    q_lower = query.lower()
    found: list[str] = []
    seen: set[str] = set()

    for node in kg.graph.nodes:
        node_lower = node.lower()
        # Use word-boundary-like check: the node name appears as a distinct token
        pattern = r"(?<![a-z])" + re.escape(node_lower) + r"(?![a-z])"
        if re.search(pattern, q_lower):
            if node not in seen:
                found.append(node)
                seen.add(node)

    # Alias matching for common synonyms
    aliases = {
        "paddy": "Rice",
        "paddy crop": "Rice",
        "maize crop": "Maize",
        "corn": "Maize",
        "mustard oil": "Mustard",
        "groundnut oil": "Groundnut",
        "black soil": "Black (Regur)",
        "regur": "Black (Regur)",
    }
    for alias, canonical in aliases.items():
        if alias in q_lower and canonical not in seen:
            node = kg.find_entity(canonical)
            if node:
                found.append(node)
                seen.add(node)

    return found


def _format_list(items: list[str]) -> str:
    if not items:
        return "none"
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + f" and {items[-1]}"


def _entity_section(name: str, kg: "AgriculturalKnowledgeGraph") -> str:
    """Generate a descriptive paragraph about an entity."""
    rels = kg.get_relationships(name)
    if not rels:
        return f"I found '{name}' in the knowledge base but have no detailed information."

    attrs = rels.get("attributes", {})
    entity_type = attrs.get("type", "Entity")
    description = attrs.get("description", "")

    lines = [f"**{name}** ({entity_type})"]
    if description:
        lines.append(description)

    # Outgoing relationships
    outgoing_by_rel: dict[str, list[str]] = {}
    for edge in rels.get("outgoing", []):
        r = edge["relationship"]
        t = edge["target"]
        outgoing_by_rel.setdefault(r, []).append(t)

    rel_labels = {
        "requires": "Requires fertilizer(s)",
        "susceptible_to": "Susceptible to",
        "grown_in": "Grows in soil type(s)",
        "benefits_from": "Benefits from",
        "treated_by": "Treated by",
        "affects": "Affects",
        "suitable_for": "Suitable for crop(s)",
        "prevented_by": "Can be prevented by",
    }
    for rel, targets in outgoing_by_rel.items():
        label = rel_labels.get(rel, rel.replace("_", " ").capitalize())
        lines.append(f"  • {label}: {_format_list(targets)}")

    # Incoming relationships (selected)
    incoming_by_rel: dict[str, list[str]] = {}
    for edge in rels.get("incoming", []):
        r = edge["relationship"]
        s = edge["source"]
        incoming_by_rel.setdefault(r, []).append(s)

    for rel, sources in incoming_by_rel.items():
        label = rel_labels.get(rel, rel.replace("_", " ").capitalize())
        lines.append(f"  • {label} by: {_format_list(sources)}")

    return "\n".join(lines)


def process_query(question: str, kg: "AgriculturalKnowledgeGraph") -> dict:
    """
    Process a natural language agricultural query and return a structured response.

    Returns a dict with keys:
        - question (str)
        - answer (str)
        - entities_found (list[str])
        - relationships (list[dict])
    """
    if not question or not question.strip():
        return {
            "question": question,
            "answer": "Please enter a question to get started.",
            "entities_found": [],
            "relationships": [],
        }

    intents = _match_intents(question)
    entities = extract_entities(question, kg)

    relationships: list[dict] = []
    answer_parts: list[str] = []

    # ------------------------------------------------------------------
    # Case 1: specific entities found
    # ------------------------------------------------------------------
    if entities:
        for entity in entities:
            rels = kg.get_relationships(entity)
            if rels:
                answer_parts.append(_entity_section(entity, kg))
                # Collect relationships for structured output
                for edge in rels.get("outgoing", []):
                    relationships.append({
                        "source": entity,
                        "relationship": edge["relationship"],
                        "target": edge["target"],
                    })
                for edge in rels.get("incoming", []):
                    relationships.append({
                        "source": edge["source"],
                        "relationship": edge["relationship"],
                        "target": entity,
                    })

        # Provide intent-specific supplements
        if "fertilizer" in intents:
            for entity in entities:
                ferts = kg.get_related_entities(entity, "requires")
                if ferts:
                    names = [f["name"] for f in ferts]
                    answer_parts.append(
                        f"💡 Recommended fertilizers for {entity}: {_format_list(names)}."
                    )

        if "pest" in intents or "disease" in intents:
            for entity in entities:
                threats = kg.get_related_entities(entity, "susceptible_to")
                if threats:
                    names = [t["name"] for t in threats]
                    answer_parts.append(
                        f"⚠️ {entity} is susceptible to: {_format_list(names)}."
                    )

        if "treatment" in intents:
            for entity in entities:
                treatments = kg.get_related_entities(entity, "treated_by")
                if treatments:
                    names = [t["name"] for t in treatments]
                    answer_parts.append(
                        f"🩺 Treatment for {entity}: {_format_list(names)}."
                    )

        if "soil" in intents:
            for entity in entities:
                soils = kg.get_related_entities(entity, "grown_in")
                if soils:
                    names = [s["name"] for s in soils]
                    answer_parts.append(
                        f"🌱 {entity} grows well in: {_format_list(names)} soil."
                    )
                crops = kg.get_related_entities(entity, "suitable_for")
                if crops:
                    names = [c["name"] for c in crops]
                    answer_parts.append(
                        f"🌱 Crops suitable for {entity} soil: {_format_list(names)}."
                    )

        if "irrigation" in intents:
            for entity in entities:
                methods = kg.get_related_entities(entity, "benefits_from")
                methods = [m for m in methods
                           if kg.graph.nodes[m["name"]].get("type") == "Irrigation_Method"]
                if methods:
                    names = [m["name"] for m in methods]
                    answer_parts.append(
                        f"💧 Irrigation methods for {entity}: {_format_list(names)}."
                    )

        if answer_parts:
            answer = "\n\n".join(answer_parts)
        else:
            answer = (
                f"I found information about {_format_list(entities)} in the "
                "knowledge base, but no specific details match your query. "
                "Try asking about fertilizers, pests, diseases, soil type, or irrigation."
            )

    # ------------------------------------------------------------------
    # Case 2: intent detected but no specific entity matched
    # ------------------------------------------------------------------
    elif intents:
        intent_responses = {
            "fertilizer": _respond_fertilizers(kg),
            "pest": _respond_pests(kg),
            "disease": _respond_diseases(kg),
            "soil": _respond_soils(kg),
            "treatment": _respond_treatments(kg),
            "irrigation": _respond_irrigation(kg),
            "practice": _respond_practices(kg),
        }
        parts = [intent_responses[i] for i in intents if i in intent_responses]
        answer = "\n\n".join(parts) if parts else _fallback()

    # ------------------------------------------------------------------
    # Case 3: no match at all
    # ------------------------------------------------------------------
    else:
        answer = _fallback()

    return {
        "question": question,
        "answer": answer,
        "entities_found": entities,
        "relationships": relationships,
    }


# ---------------------------------------------------------------------------
# Intent-specific fallback responders
# ---------------------------------------------------------------------------

def _respond_fertilizers(kg: "AgriculturalKnowledgeGraph") -> str:
    ferts = kg.get_entities_by_type("Fertilizer")
    names = [f["name"] for f in ferts]
    return (
        "🌿 **Fertilizers in the knowledge base:**\n"
        + _format_list(names)
        + "\n\nTry asking: 'What fertilizer is best for rice?' or 'What does wheat require?'"
    )


def _respond_pests(kg: "AgriculturalKnowledgeGraph") -> str:
    pests = kg.get_entities_by_type("Pest")
    names = [p["name"] for p in pests]
    return (
        "🐛 **Common agricultural pests:**\n"
        + _format_list(names)
        + "\n\nTry asking: 'Which pests affect tomato?' or 'How to treat stem borer?'"
    )


def _respond_diseases(kg: "AgriculturalKnowledgeGraph") -> str:
    diseases = kg.get_entities_by_type("Disease")
    names = [d["name"] for d in diseases]
    return (
        "🦠 **Common crop diseases:**\n"
        + _format_list(names)
        + "\n\nTry asking: 'What diseases affect cotton?' or 'How to treat leaf blight?'"
    )


def _respond_soils(kg: "AgriculturalKnowledgeGraph") -> str:
    soils = kg.get_entities_by_type("Soil_Type")
    names = [s["name"] for s in soils]
    return (
        "🌍 **Soil types in the knowledge base:**\n"
        + _format_list(names)
        + "\n\nTry asking: 'Which soil is suitable for wheat?' or 'What crops grow in clay soil?'"
    )


def _respond_treatments(kg: "AgriculturalKnowledgeGraph") -> str:
    pesticides = kg.get_entities_by_type("Pesticide")
    names = [p["name"] for p in pesticides]
    return (
        "💊 **Available pesticides and treatments:**\n"
        + _format_list(names)
        + "\n\nTry asking: 'How to treat late blight?' or 'What treats aphid?'"
    )


def _respond_irrigation(kg: "AgriculturalKnowledgeGraph") -> str:
    methods = kg.get_entities_by_type("Irrigation_Method")
    names = [m["name"] for m in methods]
    return (
        "💧 **Irrigation methods:**\n"
        + _format_list(names)
        + "\n\nTry asking: 'Tell me about drip irrigation' or 'What irrigation suits sugarcane?'"
    )


def _respond_practices(kg: "AgriculturalKnowledgeGraph") -> str:
    practices = kg.get_entities_by_type("Farming_Practice")
    names = [p["name"] for p in practices]
    return (
        "🌾 **Farming practices:**\n"
        + _format_list(names)
        + "\n\nTry asking: 'Tell me about crop rotation' or 'What farming practice helps tomato?'"
    )


def _fallback() -> str:
    return (
        "I'm sorry, I couldn't find relevant information for your query. "
        "Here are some example questions you can try:\n"
        "• 'What fertilizer is best for rice?'\n"
        "• 'Which pests affect tomato plants?'\n"
        "• 'What diseases affect cotton?'\n"
        "• 'Which soil type is suitable for wheat?'\n"
        "• 'How to treat leaf blight?'\n"
        "• 'Tell me about drip irrigation'\n"
        "• 'What crops grow well in clay soil?'"
    )
