"""
Pre-populated agricultural data for the knowledge graph.
Defines nodes (entities) and their relationships.
"""
from .knowledge_graph import AgriculturalKnowledgeGraph


def build_graph() -> AgriculturalKnowledgeGraph:
    """Build and return a knowledge graph populated with agricultural data."""
    kg = AgriculturalKnowledgeGraph()

    # ------------------------------------------------------------------
    # Crops
    # ------------------------------------------------------------------
    crops = [
        ("Rice", "Staple cereal crop grown in waterlogged paddy fields; major food source in Asia."),
        ("Wheat", "Cool-season cereal crop; principal ingredient of flour and bread."),
        ("Tomato", "Warm-season vegetable fruit; requires well-drained fertile soil."),
        ("Cotton", "Fibre crop grown in tropical and subtropical regions."),
        ("Maize", "Versatile cereal crop used for food, fodder, and industry."),
        ("Sugarcane", "Tall perennial grass; primary source of sugar worldwide."),
        ("Potato", "Cool-season root vegetable; high starch content."),
        ("Soybean", "Legume crop rich in protein; fixes atmospheric nitrogen."),
        ("Mustard", "Cool-season oilseed crop; used for oil and spice."),
        ("Onion", "Bulb vegetable requiring well-drained sandy loam soil."),
        ("Barley", "Hardy cereal crop tolerant of cold and drought conditions."),
        ("Groundnut", "Legume oilseed crop grown in sandy loam soils."),
    ]
    for name, desc in crops:
        kg.add_entity(name, "Crop", desc)

    # ------------------------------------------------------------------
    # Soil Types
    # ------------------------------------------------------------------
    soils = [
        ("Clay", "Heavy, fine-grained soil with high water retention; poor drainage."),
        ("Sandy", "Coarse-textured soil with excellent drainage but low fertility."),
        ("Loamy", "Balanced mixture of sand, silt, and clay; ideal for most crops."),
        ("Black (Regur)", "Deep, dark soil high in clay minerals; excellent for cotton."),
        ("Red", "Well-drained soil low in nitrogen; suitable for millets and groundnuts."),
        ("Alluvial", "Fertile soil deposited by rivers; ideal for wheat and rice."),
        ("Laterite", "Acidic, iron-rich soil found in high-rainfall areas; good for tea and coffee."),
    ]
    for name, desc in soils:
        kg.add_entity(name, "Soil_Type", desc)

    # ------------------------------------------------------------------
    # Fertilizers
    # ------------------------------------------------------------------
    fertilizers = [
        ("Urea", "High-nitrogen synthetic fertilizer (46% N); promotes leafy growth."),
        ("DAP", "Di-ammonium phosphate; provides nitrogen and phosphorus for root development."),
        ("Potash (MOP)", "Muriate of potash; supplies potassium for fruit quality and disease resistance."),
        ("NPK Complex", "Balanced complex fertilizer supplying nitrogen, phosphorus, and potassium."),
        ("Vermicompost", "Organic fertilizer produced by earthworms; improves soil structure."),
        ("Superphosphate", "Phosphorus fertilizer that promotes root and flower development."),
        ("Ammonium Sulphate", "Nitrogen and sulphur fertilizer used in alkaline soils."),
        ("Zinc Sulphate", "Micronutrient fertilizer correcting zinc deficiency in crops."),
    ]
    for name, desc in fertilizers:
        kg.add_entity(name, "Fertilizer", desc)

    # ------------------------------------------------------------------
    # Diseases
    # ------------------------------------------------------------------
    diseases = [
        ("Leaf Blight", "Fungal/bacterial disease causing irregular brown lesions on leaves."),
        ("Rust", "Fungal disease producing orange or brown pustules on leaves and stems."),
        ("Powdery Mildew", "Fungal disease producing white powdery coating on plant surfaces."),
        ("Wilt", "Soil-borne disease causing wilting, yellowing, and plant death."),
        ("Mosaic Virus", "Viral disease transmitted by aphids causing mottled yellow-green leaves."),
        ("Late Blight", "Oomycete disease causing water-soaked lesions; destructive in potatoes."),
        ("Smut", "Fungal disease replacing grain with black sooty masses."),
        ("Root Rot", "Fungal/bacterial disease causing decay of roots and lower stem."),
        ("Bacterial Canker", "Bacterial disease causing cankers and gummosis on stems."),
        ("Downy Mildew", "Fungal disease producing grayish mold on undersides of leaves."),
    ]
    for name, desc in diseases:
        kg.add_entity(name, "Disease", desc)

    # ------------------------------------------------------------------
    # Pests
    # ------------------------------------------------------------------
    pests = [
        ("Stem Borer", "Larval pest boring into stems of cereals, causing dead hearts and white ears."),
        ("Whitefly", "Tiny sucking insect; vector of many viral plant diseases."),
        ("Aphid", "Soft-bodied sucking pest; vectors mosaic virus and other pathogens."),
        ("Bollworm", "Larval pest attacking cotton bolls and flower buds."),
        ("Fruit Borer", "Moth larva boring into fruits; damages tomato and other vegetables."),
        ("Cutworm", "Nocturnal caterpillar cutting seedlings at ground level."),
        ("Locust", "Migratory pest forming large swarms that devastate crops."),
        ("Thrips", "Tiny rasping-sucking insect damaging onion, chilli, and cotton."),
        ("Mite", "Tiny arachnid pest causing leaf bronzing and reduced vigour."),
        ("Leaf Miner", "Fly larva tunnelling inside leaves, creating winding mines."),
    ]
    for name, desc in pests:
        kg.add_entity(name, "Pest", desc)

    # ------------------------------------------------------------------
    # Pesticides / Treatments
    # ------------------------------------------------------------------
    pesticides = [
        ("Fungicide", "Chemical agent used to kill or inhibit fungal pathogens on crops."),
        ("Insecticide", "Chemical agent used to kill insect pests threatening crops."),
        ("Neem Oil", "Organic botanical pesticide effective against a broad spectrum of pests."),
        ("Copper Sulphate", "Inorganic fungicide and bactericide used in Bordeaux mixture."),
        ("Bordeaux Mixture", "Classic copper-based fungicide mixture of copper sulphate and lime."),
        ("Carbendazim", "Systemic benzimidazole fungicide for controlling leaf blight and smut."),
        ("Imidacloprid", "Systemic neonicotinoid insecticide effective against sucking pests."),
        ("Mancozeb", "Broad-spectrum contact fungicide protecting against blight and mildew."),
        ("Chlorpyrifos", "Organophosphate insecticide used against stem borers and cutworms."),
        ("Trichoderma", "Biocontrol fungus used as a bio-pesticide against soil-borne diseases."),
    ]
    for name, desc in pesticides:
        kg.add_entity(name, "Pesticide", desc)

    # ------------------------------------------------------------------
    # Irrigation Methods
    # ------------------------------------------------------------------
    irrigation = [
        ("Drip Irrigation", "Micro-irrigation delivering water directly to the root zone; highly efficient."),
        ("Flood Irrigation", "Traditional method flooding entire field; used for rice and sugarcane."),
        ("Sprinkler Irrigation", "Overhead sprinkler system mimicking rainfall; good for wheat and vegetables."),
        ("Furrow Irrigation", "Water flows in furrows between crop rows; used for maize and cotton."),
    ]
    for name, desc in irrigation:
        kg.add_entity(name, "Irrigation_Method", desc)

    # ------------------------------------------------------------------
    # Farming Practices
    # ------------------------------------------------------------------
    practices = [
        ("Crop Rotation", "Alternating different crops each season to improve soil health and break pest cycles."),
        ("Mulching", "Covering soil surface with organic material to retain moisture and suppress weeds."),
        ("Intercropping", "Growing two or more crops simultaneously to maximise land use and reduce pests."),
        ("Organic Farming", "Farming without synthetic chemicals; relies on organic inputs and biological control."),
        ("Zero Tillage", "Planting without ploughing to reduce soil erosion and conserve moisture."),
        ("Cover Cropping", "Growing plants to protect and enrich soil between main crop seasons."),
    ]
    for name, desc in practices:
        kg.add_entity(name, "Farming_Practice", desc)

    # ------------------------------------------------------------------
    # Relationships  (50+ defined below)
    # ------------------------------------------------------------------

    # Crop → Soil_Type  (grown_in)
    kg.add_relationship("Rice", "Clay", "grown_in")
    kg.add_relationship("Rice", "Alluvial", "grown_in")
    kg.add_relationship("Wheat", "Alluvial", "grown_in")
    kg.add_relationship("Wheat", "Loamy", "grown_in")
    kg.add_relationship("Tomato", "Loamy", "grown_in")
    kg.add_relationship("Cotton", "Black (Regur)", "grown_in")
    kg.add_relationship("Cotton", "Red", "grown_in")
    kg.add_relationship("Maize", "Loamy", "grown_in")
    kg.add_relationship("Sugarcane", "Alluvial", "grown_in")
    kg.add_relationship("Sugarcane", "Black (Regur)", "grown_in")
    kg.add_relationship("Potato", "Sandy", "grown_in")
    kg.add_relationship("Potato", "Loamy", "grown_in")
    kg.add_relationship("Soybean", "Loamy", "grown_in")
    kg.add_relationship("Mustard", "Loamy", "grown_in")
    kg.add_relationship("Mustard", "Sandy", "grown_in")
    kg.add_relationship("Onion", "Sandy", "grown_in")
    kg.add_relationship("Groundnut", "Sandy", "grown_in")
    kg.add_relationship("Barley", "Loamy", "grown_in")

    # Crop → Fertilizer  (requires)
    kg.add_relationship("Rice", "Urea", "requires")
    kg.add_relationship("Rice", "DAP", "requires")
    kg.add_relationship("Wheat", "Urea", "requires")
    kg.add_relationship("Wheat", "DAP", "requires")
    kg.add_relationship("Wheat", "Potash (MOP)", "requires")
    kg.add_relationship("Tomato", "NPK Complex", "requires")
    kg.add_relationship("Tomato", "Vermicompost", "requires")
    kg.add_relationship("Cotton", "Urea", "requires")
    kg.add_relationship("Cotton", "Potash (MOP)", "requires")
    kg.add_relationship("Maize", "Urea", "requires")
    kg.add_relationship("Maize", "NPK Complex", "requires")
    kg.add_relationship("Sugarcane", "Urea", "requires")
    kg.add_relationship("Sugarcane", "Potash (MOP)", "requires")
    kg.add_relationship("Potato", "NPK Complex", "requires")
    kg.add_relationship("Potato", "Potash (MOP)", "requires")
    kg.add_relationship("Soybean", "Superphosphate", "requires")
    kg.add_relationship("Mustard", "Urea", "requires")
    kg.add_relationship("Onion", "NPK Complex", "requires")
    kg.add_relationship("Onion", "Ammonium Sulphate", "requires")
    kg.add_relationship("Groundnut", "Zinc Sulphate", "requires")

    # Crop → Disease  (susceptible_to)
    kg.add_relationship("Rice", "Leaf Blight", "susceptible_to")
    kg.add_relationship("Rice", "Smut", "susceptible_to")
    kg.add_relationship("Rice", "Root Rot", "susceptible_to")
    kg.add_relationship("Wheat", "Rust", "susceptible_to")
    kg.add_relationship("Wheat", "Smut", "susceptible_to")
    kg.add_relationship("Wheat", "Powdery Mildew", "susceptible_to")
    kg.add_relationship("Tomato", "Late Blight", "susceptible_to")
    kg.add_relationship("Tomato", "Mosaic Virus", "susceptible_to")
    kg.add_relationship("Tomato", "Wilt", "susceptible_to")
    kg.add_relationship("Cotton", "Wilt", "susceptible_to")
    kg.add_relationship("Cotton", "Root Rot", "susceptible_to")
    kg.add_relationship("Potato", "Late Blight", "susceptible_to")
    kg.add_relationship("Potato", "Root Rot", "susceptible_to")
    kg.add_relationship("Maize", "Leaf Blight", "susceptible_to")
    kg.add_relationship("Maize", "Smut", "susceptible_to")
    kg.add_relationship("Mustard", "Downy Mildew", "susceptible_to")
    kg.add_relationship("Mustard", "Rust", "susceptible_to")
    kg.add_relationship("Onion", "Downy Mildew", "susceptible_to")

    # Crop → Pest  (susceptible_to)
    kg.add_relationship("Rice", "Stem Borer", "susceptible_to")
    kg.add_relationship("Wheat", "Aphid", "susceptible_to")
    kg.add_relationship("Tomato", "Whitefly", "susceptible_to")
    kg.add_relationship("Tomato", "Fruit Borer", "susceptible_to")
    kg.add_relationship("Cotton", "Bollworm", "susceptible_to")
    kg.add_relationship("Cotton", "Whitefly", "susceptible_to")
    kg.add_relationship("Cotton", "Thrips", "susceptible_to")
    kg.add_relationship("Maize", "Stem Borer", "susceptible_to")
    kg.add_relationship("Maize", "Cutworm", "susceptible_to")
    kg.add_relationship("Potato", "Aphid", "susceptible_to")
    kg.add_relationship("Onion", "Thrips", "susceptible_to")
    kg.add_relationship("Groundnut", "Leaf Miner", "susceptible_to")

    # Disease → Pesticide  (treated_by)
    kg.add_relationship("Leaf Blight", "Carbendazim", "treated_by")
    kg.add_relationship("Leaf Blight", "Mancozeb", "treated_by")
    kg.add_relationship("Leaf Blight", "Bordeaux Mixture", "treated_by")
    kg.add_relationship("Rust", "Mancozeb", "treated_by")
    kg.add_relationship("Rust", "Fungicide", "treated_by")
    kg.add_relationship("Powdery Mildew", "Bordeaux Mixture", "treated_by")
    kg.add_relationship("Powdery Mildew", "Fungicide", "treated_by")
    kg.add_relationship("Late Blight", "Mancozeb", "treated_by")
    kg.add_relationship("Late Blight", "Bordeaux Mixture", "treated_by")
    kg.add_relationship("Late Blight", "Copper Sulphate", "treated_by")
    kg.add_relationship("Wilt", "Carbendazim", "treated_by")
    kg.add_relationship("Wilt", "Trichoderma", "treated_by")
    kg.add_relationship("Smut", "Carbendazim", "treated_by")
    kg.add_relationship("Root Rot", "Trichoderma", "treated_by")
    kg.add_relationship("Root Rot", "Carbendazim", "treated_by")
    kg.add_relationship("Mosaic Virus", "Imidacloprid", "treated_by")
    kg.add_relationship("Downy Mildew", "Mancozeb", "treated_by")
    kg.add_relationship("Downy Mildew", "Bordeaux Mixture", "treated_by")

    # Pest → Pesticide  (treated_by)
    kg.add_relationship("Stem Borer", "Chlorpyrifos", "treated_by")
    kg.add_relationship("Stem Borer", "Insecticide", "treated_by")
    kg.add_relationship("Whitefly", "Imidacloprid", "treated_by")
    kg.add_relationship("Whitefly", "Neem Oil", "treated_by")
    kg.add_relationship("Aphid", "Imidacloprid", "treated_by")
    kg.add_relationship("Aphid", "Neem Oil", "treated_by")
    kg.add_relationship("Bollworm", "Insecticide", "treated_by")
    kg.add_relationship("Bollworm", "Chlorpyrifos", "treated_by")
    kg.add_relationship("Fruit Borer", "Insecticide", "treated_by")
    kg.add_relationship("Cutworm", "Chlorpyrifos", "treated_by")
    kg.add_relationship("Thrips", "Imidacloprid", "treated_by")
    kg.add_relationship("Thrips", "Neem Oil", "treated_by")
    kg.add_relationship("Leaf Miner", "Neem Oil", "treated_by")
    kg.add_relationship("Mite", "Neem Oil", "treated_by")

    # Crop → Irrigation_Method  (benefits_from)
    kg.add_relationship("Rice", "Flood Irrigation", "benefits_from")
    kg.add_relationship("Tomato", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Cotton", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Cotton", "Furrow Irrigation", "benefits_from")
    kg.add_relationship("Wheat", "Sprinkler Irrigation", "benefits_from")
    kg.add_relationship("Maize", "Furrow Irrigation", "benefits_from")
    kg.add_relationship("Sugarcane", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Sugarcane", "Furrow Irrigation", "benefits_from")
    kg.add_relationship("Potato", "Sprinkler Irrigation", "benefits_from")
    kg.add_relationship("Onion", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Groundnut", "Sprinkler Irrigation", "benefits_from")

    # Crop → Farming_Practice  (benefits_from)
    kg.add_relationship("Rice", "Crop Rotation", "benefits_from")
    kg.add_relationship("Wheat", "Zero Tillage", "benefits_from")
    kg.add_relationship("Soybean", "Intercropping", "benefits_from")
    kg.add_relationship("Tomato", "Mulching", "benefits_from")
    kg.add_relationship("Potato", "Mulching", "benefits_from")
    kg.add_relationship("Maize", "Intercropping", "benefits_from")
    kg.add_relationship("Cotton", "Intercropping", "benefits_from")
    kg.add_relationship("Mustard", "Crop Rotation", "benefits_from")
    kg.add_relationship("Groundnut", "Crop Rotation", "benefits_from")

    # Pest → Disease  (affects indirectly / vectors)
    kg.add_relationship("Whitefly", "Mosaic Virus", "affects")
    kg.add_relationship("Aphid", "Mosaic Virus", "affects")

    # Disease → Crop  (affects)
    kg.add_relationship("Mosaic Virus", "Tomato", "affects")
    kg.add_relationship("Late Blight", "Potato", "affects")
    kg.add_relationship("Rust", "Wheat", "affects")
    kg.add_relationship("Leaf Blight", "Rice", "affects")
    kg.add_relationship("Leaf Blight", "Maize", "affects")
    kg.add_relationship("Wilt", "Cotton", "affects")

    # Soil → Crop  (suitable_for)
    kg.add_relationship("Alluvial", "Rice", "suitable_for")
    kg.add_relationship("Alluvial", "Wheat", "suitable_for")
    kg.add_relationship("Alluvial", "Sugarcane", "suitable_for")
    kg.add_relationship("Black (Regur)", "Cotton", "suitable_for")
    kg.add_relationship("Black (Regur)", "Sugarcane", "suitable_for")
    kg.add_relationship("Loamy", "Tomato", "suitable_for")
    kg.add_relationship("Loamy", "Maize", "suitable_for")
    kg.add_relationship("Loamy", "Soybean", "suitable_for")
    kg.add_relationship("Sandy", "Potato", "suitable_for")
    kg.add_relationship("Sandy", "Onion", "suitable_for")
    kg.add_relationship("Sandy", "Groundnut", "suitable_for")
    kg.add_relationship("Clay", "Rice", "suitable_for")
    kg.add_relationship("Red", "Groundnut", "suitable_for")
    kg.add_relationship("Laterite", "Barley", "suitable_for")

    # Disease → Crop  (prevented_by good practice)
    kg.add_relationship("Wilt", "Crop Rotation", "prevented_by")
    kg.add_relationship("Root Rot", "Organic Farming", "prevented_by")
    kg.add_relationship("Mosaic Virus", "Neem Oil", "prevented_by")
    kg.add_relationship("Late Blight", "Bordeaux Mixture", "prevented_by")
    kg.add_relationship("Rust", "Fungicide", "prevented_by")
    kg.add_relationship("Powdery Mildew", "Neem Oil", "prevented_by")
    kg.add_relationship("Smut", "Carbendazim", "prevented_by")

    return kg
