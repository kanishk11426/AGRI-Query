"""
Pre-populated agricultural data for the knowledge graph.
Defines nodes (entities) and their relationships.
"""
from .knowledge_graph import AgriculturalKnowledgeGraph


def build_graph() -> AgriculturalKnowledgeGraph:
    """Build and return a knowledge graph populated with agricultural data."""
    kg = AgriculturalKnowledgeGraph()

    # ------------------------------------------------------------------
    # Crops (Expanded from 12 to 30)
    # ------------------------------------------------------------------
    crops = [
        # Original crops (12)
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
        # New crops (18)
        ("Mango", "Tropical stone fruit; high-value commercial crop requiring warm climate."),
        ("Banana", "Perennial herbaceous plant producing nutritious fruit clusters."),
        ("Papaya", "Fast-growing tropical fruit tree; rich in vitamins and enzymes."),
        ("Grapes", "Climbing vine producing fruit clusters; used for wine and fresh consumption."),
        ("Citrus", "Broad category including oranges, lemons, and limes; rich in vitamin C."),
        ("Tea", "Perennial bush grown in hilly regions; processed leaves used for beverage."),
        ("Coffee", "Evergreen shrub producing beans for coffee beverage; requires shade."),
        ("Rubber", "Tropical tree producing latex for rubber production."),
        ("Coconut", "Palm tree producing versatile nuts; thrives in coastal regions."),
        ("Chilli", "Hot pepper plant; important spice crop requiring warm conditions."),
        ("Brinjal", "Eggplant; warm-season vegetable requiring well-drained soil."),
        ("Cabbage", "Cool-season leafy vegetable; forms compact heads."),
        ("Cauliflower", "Cool-season vegetable producing white curds."),
        ("Carrot", "Root vegetable rich in beta-carotene; prefers loose soil."),
        ("Peas", "Cool-season legume; fixes nitrogen and improves soil fertility."),
        ("Cucumber", "Warm-season vine crop; high water content fruit."),
        ("Garlic", "Bulbous crop with strong flavor; used for culinary and medicinal purposes."),
        ("Ginger", "Rhizomatous herb; important spice and medicinal crop."),
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
    # Fertilizers (Expanded from 8 to 15)
    # ------------------------------------------------------------------
    fertilizers = [
        # Original fertilizers (8)
        ("Urea", "High-nitrogen synthetic fertilizer (46% N); promotes leafy growth."),
        ("DAP", "Di-ammonium phosphate; provides nitrogen and phosphorus for root development."),
        ("Potash (MOP)", "Muriate of potash; supplies potassium for fruit quality and disease resistance."),
        ("NPK Complex", "Balanced complex fertilizer supplying nitrogen, phosphorus, and potassium."),
        ("Vermicompost", "Organic fertilizer produced by earthworms; improves soil structure."),
        ("Superphosphate", "Phosphorus fertilizer that promotes root and flower development."),
        ("Ammonium Sulphate", "Nitrogen and sulphur fertilizer used in alkaline soils."),
        ("Zinc Sulphate", "Micronutrient fertilizer correcting zinc deficiency in crops."),
        # New fertilizers (7)
        ("Farmyard Manure", "Traditional organic fertilizer from decomposed animal waste; improves soil health."),
        ("Compost", "Decomposed organic matter; enriches soil with nutrients and beneficial microbes."),
        ("Green Manure", "Crops grown and ploughed back into soil to add organic matter and nitrogen."),
        ("Calcium Nitrate", "Water-soluble fertilizer providing calcium and nitrogen; prevents blossom end rot."),
        ("Magnesium Sulphate", "Epsom salt; corrects magnesium deficiency and improves chlorophyll production."),
        ("Boron Fertilizer", "Micronutrient essential for pollination, fruit set, and cell wall formation."),
        ("Biofertilizer", "Living microorganisms that enhance nutrient availability; includes Rhizobium and Azotobacter."),
    ]
    for name, desc in fertilizers:
        kg.add_entity(name, "Fertilizer", desc)

    # ------------------------------------------------------------------
    # Diseases (Expanded from 10 to 20)
    # ------------------------------------------------------------------
    diseases = [
        # Original diseases (10)
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
        # New diseases (10)
        ("Anthracnose", "Fungal disease causing dark sunken lesions on fruits, leaves, and stems."),
        ("Fusarium Wilt", "Soil-borne fungal disease blocking vascular system; causes sudden wilting."),
        ("Bacterial Leaf Spot", "Bacterial disease causing circular water-soaked spots on leaves."),
        ("Fire Blight", "Bacterial disease causing blackened, scorched appearance in shoots and blossoms."),
        ("Cercospora Leaf Spot", "Fungal disease producing circular spots with gray centers on leaves."),
        ("Black Rot", "Fungal disease causing V-shaped yellow lesions on leaf margins in crucifers."),
        ("Alternaria Blight", "Fungal disease causing brown to black leaf spots with concentric rings."),
        ("Verticillium Wilt", "Soil-borne fungal disease causing yellowing and wilting of lower leaves."),
        ("Panama Disease", "Fusarium wilt specific to bananas; causes yellowing and plant collapse."),
        ("Citrus Canker", "Bacterial disease causing raised lesions on citrus fruits and leaves."),
    ]
    for name, desc in diseases:
        kg.add_entity(name, "Disease", desc)

    # ------------------------------------------------------------------
    # Pests (Expanded from 10 to 20)
    # ------------------------------------------------------------------
    pests = [
        # Original pests (10)
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
        # New pests (10)
        ("Armyworm", "Caterpillar pest moving in large groups; attacks grasses and cereals."),
        ("Jassid", "Leafhopper causing leaf curling, hopper burn, and reduced yield."),
        ("Scale Insect", "Sap-sucking pest with waxy covering; weakens plants and excretes honeydew."),
        ("Mealybug", "Soft-bodied sucking pest covered in white waxy secretions."),
        ("Pod Borer", "Caterpillar pest damaging legume pods; reduces seed quality and yield."),
        ("Diamondback Moth", "Major pest of cruciferous crops; larvae feed on leaves creating holes."),
        ("Shoot Fly", "Fly larvae damaging growing shoots of cereals; causes dead heart symptoms."),
        ("Root Knot Nematode", "Microscopic soil-dwelling roundworm causing galls on roots."),
        ("Fruit Fly", "Adult fly laying eggs in fruits; maggots feed inside causing rot."),
        ("Rice Bug", "Sucking bug feeding on developing grains; causes chaffy and discolored rice."),
    ]
    for name, desc in pests:
        kg.add_entity(name, "Pest", desc)

    # ------------------------------------------------------------------
    # Pesticides / Treatments (Expanded from 10 to 18)
    # ------------------------------------------------------------------
    pesticides = [
        # Original pesticides (10)
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
        # New pesticides (8)
        ("Bacillus thuringiensis", "Biological insecticide bacteria producing toxins against caterpillars."),
        ("Spinosad", "Organic insecticide derived from soil bacteria; controls moths and flies."),
        ("Pyrethrum", "Natural insecticide extracted from chrysanthemum flowers; broad-spectrum pest control."),
        ("Diazinon", "Organophosphate insecticide for soil pests and root knot nematodes."),
        ("Sulfur Dust", "Elemental sulfur fungicide and acaricide; controls mites and powdery mildew."),
        ("Azadirachtin", "Active compound from neem; insect growth regulator and feeding deterrent."),
        ("Metarhizium", "Entomopathogenic fungus used as biological control for various insect pests."),
        ("Beauveria bassiana", "Fungal biopesticide infecting and killing a wide range of insect pests."),
    ]
    for name, desc in pesticides:
        kg.add_entity(name, "Pesticide", desc)

    # ------------------------------------------------------------------
    # Irrigation Methods (Expanded from 4 to 7)
    # ------------------------------------------------------------------
    irrigation = [
        # Original irrigation methods (4)
        ("Drip Irrigation", "Micro-irrigation delivering water directly to the root zone; highly efficient."),
        ("Flood Irrigation", "Traditional method flooding entire field; used for rice and sugarcane."),
        ("Sprinkler Irrigation", "Overhead sprinkler system mimicking rainfall; good for wheat and vegetables."),
        ("Furrow Irrigation", "Water flows in furrows between crop rows; used for maize and cotton."),
        # New irrigation methods (3)
        ("Sub-surface Irrigation", "Water delivered below soil surface through buried pipes; reduces evaporation."),
        ("Rainwater Harvesting", "Collecting and storing rainwater for irrigation during dry periods."),
        ("Micro-sprinkler Irrigation", "Low-pressure irrigation delivering fine spray; suitable for orchards and vegetables."),
    ]
    for name, desc in irrigation:
        kg.add_entity(name, "Irrigation_Method", desc)

    # ------------------------------------------------------------------
    # Farming Practices (Expanded from 6 to 12)
    # ------------------------------------------------------------------
    practices = [
        # Original farming practices (6)
        ("Crop Rotation", "Alternating different crops each season to improve soil health and break pest cycles."),
        ("Mulching", "Covering soil surface with organic material to retain moisture and suppress weeds."),
        ("Intercropping", "Growing two or more crops simultaneously to maximise land use and reduce pests."),
        ("Organic Farming", "Farming without synthetic chemicals; relies on organic inputs and biological control."),
        ("Zero Tillage", "Planting without ploughing to reduce soil erosion and conserve moisture."),
        ("Cover Cropping", "Growing plants to protect and enrich soil between main crop seasons."),
        # New farming practices (6)
        ("Integrated Pest Management", "Holistic pest control combining biological, cultural, and chemical methods."),
        ("Precision Agriculture", "Using GPS and sensors to optimize field-level management of crops."),
        ("Greenhouse Farming", "Controlled environment agriculture protecting crops from weather extremes."),
        ("Hydroponics", "Soilless cultivation growing plants in nutrient-rich water solutions."),
        ("Agroforestry", "Integrating trees with crops/livestock; improves biodiversity and soil health."),
        ("Composting", "Recycling organic waste into nutrient-rich soil amendment through decomposition."),
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

    # ------------------------------------------------------------------
    # NEW RELATIONSHIPS for expanded entities (150+ new relationships)
    # ------------------------------------------------------------------

    # New Crops → Soil_Type (grown_in)
    kg.add_relationship("Mango", "Alluvial", "grown_in")
    kg.add_relationship("Mango", "Loamy", "grown_in")
    kg.add_relationship("Banana", "Alluvial", "grown_in")
    kg.add_relationship("Banana", "Loamy", "grown_in")
    kg.add_relationship("Papaya", "Sandy", "grown_in")
    kg.add_relationship("Papaya", "Loamy", "grown_in")
    kg.add_relationship("Grapes", "Loamy", "grown_in")
    kg.add_relationship("Grapes", "Sandy", "grown_in")
    kg.add_relationship("Citrus", "Sandy", "grown_in")
    kg.add_relationship("Citrus", "Loamy", "grown_in")
    kg.add_relationship("Tea", "Laterite", "grown_in")
    kg.add_relationship("Coffee", "Laterite", "grown_in")
    kg.add_relationship("Rubber", "Laterite", "grown_in")
    kg.add_relationship("Coconut", "Sandy", "grown_in")
    kg.add_relationship("Coconut", "Laterite", "grown_in")
    kg.add_relationship("Chilli", "Loamy", "grown_in")
    kg.add_relationship("Chilli", "Sandy", "grown_in")
    kg.add_relationship("Brinjal", "Loamy", "grown_in")
    kg.add_relationship("Cabbage", "Loamy", "grown_in")
    kg.add_relationship("Cauliflower", "Loamy", "grown_in")
    kg.add_relationship("Carrot", "Sandy", "grown_in")
    kg.add_relationship("Carrot", "Loamy", "grown_in")
    kg.add_relationship("Peas", "Loamy", "grown_in")
    kg.add_relationship("Cucumber", "Loamy", "grown_in")
    kg.add_relationship("Garlic", "Loamy", "grown_in")
    kg.add_relationship("Ginger", "Loamy", "grown_in")

    # New Crops → Fertilizer (requires)
    kg.add_relationship("Mango", "NPK Complex", "requires")
    kg.add_relationship("Mango", "Vermicompost", "requires")
    kg.add_relationship("Mango", "Boron Fertilizer", "requires")
    kg.add_relationship("Banana", "Potash (MOP)", "requires")
    kg.add_relationship("Banana", "Farmyard Manure", "requires")
    kg.add_relationship("Papaya", "NPK Complex", "requires")
    kg.add_relationship("Papaya", "Calcium Nitrate", "requires")
    kg.add_relationship("Grapes", "NPK Complex", "requires")
    kg.add_relationship("Grapes", "Zinc Sulphate", "requires")
    kg.add_relationship("Citrus", "Urea", "requires")
    kg.add_relationship("Citrus", "Magnesium Sulphate", "requires")
    kg.add_relationship("Tea", "Ammonium Sulphate", "requires")
    kg.add_relationship("Coffee", "NPK Complex", "requires")
    kg.add_relationship("Rubber", "Urea", "requires")
    kg.add_relationship("Coconut", "Potash (MOP)", "requires")
    kg.add_relationship("Coconut", "Compost", "requires")
    kg.add_relationship("Chilli", "NPK Complex", "requires")
    kg.add_relationship("Chilli", "Calcium Nitrate", "requires")
    kg.add_relationship("Brinjal", "NPK Complex", "requires")
    kg.add_relationship("Brinjal", "Vermicompost", "requires")
    kg.add_relationship("Cabbage", "Urea", "requires")
    kg.add_relationship("Cabbage", "Boron Fertilizer", "requires")
    kg.add_relationship("Cauliflower", "NPK Complex", "requires")
    kg.add_relationship("Cauliflower", "Boron Fertilizer", "requires")
    kg.add_relationship("Carrot", "Superphosphate", "requires")
    kg.add_relationship("Carrot", "Compost", "requires")
    kg.add_relationship("Peas", "Superphosphate", "requires")
    kg.add_relationship("Peas", "Biofertilizer", "requires")
    kg.add_relationship("Cucumber", "NPK Complex", "requires")
    kg.add_relationship("Cucumber", "Vermicompost", "requires")
    kg.add_relationship("Garlic", "NPK Complex", "requires")
    kg.add_relationship("Ginger", "NPK Complex", "requires")
    kg.add_relationship("Ginger", "Farmyard Manure", "requires")
    kg.add_relationship("Barley", "Urea", "requires")
    kg.add_relationship("Soybean", "Biofertilizer", "requires")

    # New Crops → Disease (susceptible_to)
    kg.add_relationship("Mango", "Anthracnose", "susceptible_to")
    kg.add_relationship("Mango", "Powdery Mildew", "susceptible_to")
    kg.add_relationship("Banana", "Panama Disease", "susceptible_to")
    kg.add_relationship("Banana", "Fusarium Wilt", "susceptible_to")
    kg.add_relationship("Papaya", "Anthracnose", "susceptible_to")
    kg.add_relationship("Grapes", "Downy Mildew", "susceptible_to")
    kg.add_relationship("Grapes", "Powdery Mildew", "susceptible_to")
    kg.add_relationship("Citrus", "Citrus Canker", "susceptible_to")
    kg.add_relationship("Tea", "Rust", "susceptible_to")
    kg.add_relationship("Coffee", "Rust", "susceptible_to")
    kg.add_relationship("Chilli", "Bacterial Leaf Spot", "susceptible_to")
    kg.add_relationship("Chilli", "Anthracnose", "susceptible_to")
    kg.add_relationship("Brinjal", "Wilt", "susceptible_to")
    kg.add_relationship("Brinjal", "Bacterial Canker", "susceptible_to")
    kg.add_relationship("Cabbage", "Black Rot", "susceptible_to")
    kg.add_relationship("Cabbage", "Downy Mildew", "susceptible_to")
    kg.add_relationship("Cauliflower", "Black Rot", "susceptible_to")
    kg.add_relationship("Cauliflower", "Downy Mildew", "susceptible_to")
    kg.add_relationship("Carrot", "Alternaria Blight", "susceptible_to")
    kg.add_relationship("Peas", "Powdery Mildew", "susceptible_to")
    kg.add_relationship("Peas", "Rust", "susceptible_to")
    kg.add_relationship("Cucumber", "Downy Mildew", "susceptible_to")
    kg.add_relationship("Cucumber", "Powdery Mildew", "susceptible_to")
    kg.add_relationship("Garlic", "Downy Mildew", "susceptible_to")
    kg.add_relationship("Ginger", "Bacterial Canker", "susceptible_to")
    kg.add_relationship("Ginger", "Root Rot", "susceptible_to")

    # New Crops → Pest (susceptible_to)
    kg.add_relationship("Mango", "Fruit Fly", "susceptible_to")
    kg.add_relationship("Mango", "Mealybug", "susceptible_to")
    kg.add_relationship("Banana", "Aphid", "susceptible_to")
    kg.add_relationship("Banana", "Mealybug", "susceptible_to")
    kg.add_relationship("Papaya", "Fruit Fly", "susceptible_to")
    kg.add_relationship("Papaya", "Aphid", "susceptible_to")
    kg.add_relationship("Grapes", "Thrips", "susceptible_to")
    kg.add_relationship("Grapes", "Mealybug", "susceptible_to")
    kg.add_relationship("Citrus", "Scale Insect", "susceptible_to")
    kg.add_relationship("Citrus", "Leaf Miner", "susceptible_to")
    kg.add_relationship("Tea", "Mite", "susceptible_to")
    kg.add_relationship("Coffee", "Stem Borer", "susceptible_to")
    kg.add_relationship("Coconut", "Mite", "susceptible_to")
    kg.add_relationship("Chilli", "Thrips", "susceptible_to")
    kg.add_relationship("Chilli", "Aphid", "susceptible_to")
    kg.add_relationship("Brinjal", "Fruit Borer", "susceptible_to")
    kg.add_relationship("Brinjal", "Jassid", "susceptible_to")
    kg.add_relationship("Cabbage", "Diamondback Moth", "susceptible_to")
    kg.add_relationship("Cabbage", "Aphid", "susceptible_to")
    kg.add_relationship("Cauliflower", "Diamondback Moth", "susceptible_to")
    kg.add_relationship("Cauliflower", "Aphid", "susceptible_to")
    kg.add_relationship("Carrot", "Aphid", "susceptible_to")
    kg.add_relationship("Peas", "Pod Borer", "susceptible_to")
    kg.add_relationship("Peas", "Aphid", "susceptible_to")
    kg.add_relationship("Cucumber", "Whitefly", "susceptible_to")
    kg.add_relationship("Cucumber", "Aphid", "susceptible_to")
    kg.add_relationship("Garlic", "Thrips", "susceptible_to")
    kg.add_relationship("Ginger", "Shoot Fly", "susceptible_to")
    kg.add_relationship("Soybean", "Pod Borer", "susceptible_to")
    kg.add_relationship("Sugarcane", "Stem Borer", "susceptible_to")
    kg.add_relationship("Barley", "Aphid", "susceptible_to")
    kg.add_relationship("Rice", "Rice Bug", "susceptible_to")

    # New Disease → Pesticide (treated_by)
    kg.add_relationship("Anthracnose", "Mancozeb", "treated_by")
    kg.add_relationship("Anthracnose", "Carbendazim", "treated_by")
    kg.add_relationship("Fusarium Wilt", "Trichoderma", "treated_by")
    kg.add_relationship("Fusarium Wilt", "Carbendazim", "treated_by")
    kg.add_relationship("Bacterial Leaf Spot", "Copper Sulphate", "treated_by")
    kg.add_relationship("Bacterial Leaf Spot", "Bordeaux Mixture", "treated_by")
    kg.add_relationship("Fire Blight", "Copper Sulphate", "treated_by")
    kg.add_relationship("Cercospora Leaf Spot", "Mancozeb", "treated_by")
    kg.add_relationship("Black Rot", "Mancozeb", "treated_by")
    kg.add_relationship("Black Rot", "Carbendazim", "treated_by")
    kg.add_relationship("Alternaria Blight", "Mancozeb", "treated_by")
    kg.add_relationship("Verticillium Wilt", "Trichoderma", "treated_by")
    kg.add_relationship("Panama Disease", "Trichoderma", "treated_by")
    kg.add_relationship("Citrus Canker", "Copper Sulphate", "treated_by")
    kg.add_relationship("Citrus Canker", "Bordeaux Mixture", "treated_by")

    # New Pest → Pesticide (treated_by)
    kg.add_relationship("Armyworm", "Chlorpyrifos", "treated_by")
    kg.add_relationship("Armyworm", "Bacillus thuringiensis", "treated_by")
    kg.add_relationship("Jassid", "Imidacloprid", "treated_by")
    kg.add_relationship("Scale Insect", "Neem Oil", "treated_by")
    kg.add_relationship("Mealybug", "Neem Oil", "treated_by")
    kg.add_relationship("Mealybug", "Azadirachtin", "treated_by")
    kg.add_relationship("Pod Borer", "Bacillus thuringiensis", "treated_by")
    kg.add_relationship("Pod Borer", "Spinosad", "treated_by")
    kg.add_relationship("Diamondback Moth", "Bacillus thuringiensis", "treated_by")
    kg.add_relationship("Diamondback Moth", "Spinosad", "treated_by")
    kg.add_relationship("Shoot Fly", "Imidacloprid", "treated_by")
    kg.add_relationship("Root Knot Nematode", "Diazinon", "treated_by")
    kg.add_relationship("Root Knot Nematode", "Trichoderma", "treated_by")
    kg.add_relationship("Fruit Fly", "Spinosad", "treated_by")
    kg.add_relationship("Fruit Fly", "Pyrethrum", "treated_by")
    kg.add_relationship("Rice Bug", "Insecticide", "treated_by")
    kg.add_relationship("Mite", "Sulfur Dust", "treated_by")
    kg.add_relationship("Bollworm", "Bacillus thuringiensis", "treated_by")
    kg.add_relationship("Fruit Borer", "Bacillus thuringiensis", "treated_by")
    kg.add_relationship("Cutworm", "Metarhizium", "treated_by")
    kg.add_relationship("Whitefly", "Beauveria bassiana", "treated_by")

    # New Crops → Irrigation_Method (benefits_from)
    kg.add_relationship("Mango", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Mango", "Micro-sprinkler Irrigation", "benefits_from")
    kg.add_relationship("Banana", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Papaya", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Grapes", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Citrus", "Micro-sprinkler Irrigation", "benefits_from")
    kg.add_relationship("Tea", "Sprinkler Irrigation", "benefits_from")
    kg.add_relationship("Coffee", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Coconut", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Chilli", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Brinjal", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Cabbage", "Sprinkler Irrigation", "benefits_from")
    kg.add_relationship("Cauliflower", "Sprinkler Irrigation", "benefits_from")
    kg.add_relationship("Carrot", "Sprinkler Irrigation", "benefits_from")
    kg.add_relationship("Peas", "Sprinkler Irrigation", "benefits_from")
    kg.add_relationship("Cucumber", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Garlic", "Drip Irrigation", "benefits_from")
    kg.add_relationship("Ginger", "Drip Irrigation", "benefits_from")

    # New Crops → Farming_Practice (benefits_from)
    kg.add_relationship("Mango", "Mulching", "benefits_from")
    kg.add_relationship("Mango", "Organic Farming", "benefits_from")
    kg.add_relationship("Banana", "Mulching", "benefits_from")
    kg.add_relationship("Papaya", "Mulching", "benefits_from")
    kg.add_relationship("Grapes", "Integrated Pest Management", "benefits_from")
    kg.add_relationship("Tea", "Organic Farming", "benefits_from")
    kg.add_relationship("Coffee", "Agroforestry", "benefits_from")
    kg.add_relationship("Chilli", "Mulching", "benefits_from")
    kg.add_relationship("Chilli", "Integrated Pest Management", "benefits_from")
    kg.add_relationship("Brinjal", "Mulching", "benefits_from")
    kg.add_relationship("Cabbage", "Crop Rotation", "benefits_from")
    kg.add_relationship("Cauliflower", "Crop Rotation", "benefits_from")
    kg.add_relationship("Cucumber", "Greenhouse Farming", "benefits_from")
    kg.add_relationship("Peas", "Crop Rotation", "benefits_from")
    kg.add_relationship("Soybean", "Zero Tillage", "benefits_from")
    kg.add_relationship("Tomato", "Greenhouse Farming", "benefits_from")
    kg.add_relationship("Cucumber", "Hydroponics", "benefits_from")

    # New Soil → Crop (suitable_for)
    kg.add_relationship("Loamy", "Mango", "suitable_for")
    kg.add_relationship("Loamy", "Banana", "suitable_for")
    kg.add_relationship("Loamy", "Papaya", "suitable_for")
    kg.add_relationship("Loamy", "Grapes", "suitable_for")
    kg.add_relationship("Loamy", "Chilli", "suitable_for")
    kg.add_relationship("Loamy", "Brinjal", "suitable_for")
    kg.add_relationship("Loamy", "Cabbage", "suitable_for")
    kg.add_relationship("Loamy", "Cauliflower", "suitable_for")
    kg.add_relationship("Loamy", "Peas", "suitable_for")
    kg.add_relationship("Loamy", "Cucumber", "suitable_for")
    kg.add_relationship("Loamy", "Garlic", "suitable_for")
    kg.add_relationship("Loamy", "Ginger", "suitable_for")
    kg.add_relationship("Sandy", "Citrus", "suitable_for")
    kg.add_relationship("Sandy", "Coconut", "suitable_for")
    kg.add_relationship("Sandy", "Carrot", "suitable_for")
    kg.add_relationship("Laterite", "Tea", "suitable_for")
    kg.add_relationship("Laterite", "Coffee", "suitable_for")
    kg.add_relationship("Laterite", "Rubber", "suitable_for")
    kg.add_relationship("Laterite", "Coconut", "suitable_for")

    # New Disease → Crop (affects)
    kg.add_relationship("Anthracnose", "Mango", "affects")
    kg.add_relationship("Anthracnose", "Chilli", "affects")
    kg.add_relationship("Panama Disease", "Banana", "affects")
    kg.add_relationship("Citrus Canker", "Citrus", "affects")
    kg.add_relationship("Black Rot", "Cabbage", "affects")
    kg.add_relationship("Black Rot", "Cauliflower", "affects")

    # New Disease → Prevention (prevented_by)
    kg.add_relationship("Anthracnose", "Crop Rotation", "prevented_by")
    kg.add_relationship("Fusarium Wilt", "Crop Rotation", "prevented_by")
    kg.add_relationship("Verticillium Wilt", "Crop Rotation", "prevented_by")
    kg.add_relationship("Black Rot", "Crop Rotation", "prevented_by")
    kg.add_relationship("Root Knot Nematode", "Crop Rotation", "prevented_by")

    return kg

