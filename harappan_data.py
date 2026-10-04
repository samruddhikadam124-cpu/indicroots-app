"""
harappan_data.py - Historical Data Module for Harappan Civilization
Contains:
- 10 Chapters
- 10 Timeline Events
- 8 Key People / Groups
- 8 Key Places
- 10 Facts
- 15 Multiple-Choice Quiz Questions
"""

import database

# -------------------------------------------------------------------
# 1. CHAPTERS (10 Educational Chapters)
# -------------------------------------------------------------------
CHAPTERS = [
    {
        "chapter_number": 1,
        "title": "Origins, Geographical Scope, and Chronological Framework",
        "content": (
            "The Harappan Civilization, often designated as the Indus Valley or Indus-Saraswati Civilization, "
            "represents one of the earliest urban societies in human history, flourishing alongside contemporary Bronze Age "
            "civilizations in Mesopotamia and Egypt. Spanning an estimated area of over one million square kilometers across "
            "modern-day India, Pakistan, and parts of Afghanistan, it was geographically the most expansive of all ancient riverine cultures.\n\n"
            "Archaeologists generally divide the civilization into three broad chronological phases:\n"
            "1. Early Harappan Phase (c. 3300 - 2600 BCE): Characterized by regional agro-pastoral cultures such as the Ravi, Kot Diji, "
            "and Hakra ware traditions, witnessing the early emergence of fortified villages, wheel-thrown pottery, and copper metallurgy.\n"
            "2. Mature Harappan Phase (c. 2600 - 1900 BCE): The pinnacle of urbanism, distinguished by monumental brick architecture, "
            "standardized weights, covered subterranean drainage networks, and vibrant international commerce.\n"
            "3. Late Harappan Phase (c. 1900 - 1300 BCE): A period of gradual de-urbanization, regionalization, and eastward population shifts.\n\n"
            "The civilization developed primarily along the alluvial basins of the Indus River and the perennial Ghaggar-Hakra river system "
            "(identified by many scholars with the Vedic Saraswati). Its remarkable uniformity in urban planning and material culture across "
            "vast geographical distances remains one of the great hallmarks of ancient human organization."
        )
    },
    {
        "chapter_number": 2,
        "title": "The Discovery and Major Citadels: Harappa and Mohenjo-daro",
        "content": (
            "Until the early 1920s, conventional colonial historiography assumed that Indian urban civilization began with the Vedic period "
            "in the second millennium BCE. This assumption was decisively dismantled through landmark excavations conducted by the "
            "Archaeological Survey of India (ASI) under the director-generalship of Sir John Marshall.\n\n"
            "In 1920–1921, Indian archaeologist Rai Bahadur Daya Ram Sahni began systematic excavations at Harappa in Montgomery "
            "(now Sahiwal) district of western Punjab, revealing extensive burnt-brick structures, fortified mounds, and distinctive steatite seals. "
            "The following year, in 1922, historian and archaeologist Rakhaldas Banerjee (R. D. Banerji), while investigating a second-century CE "
            "Buddhist stupa at Mohenjo-daro ('Mound of the Dead') in Larkana district of Sindh, identified Bronze Age strata and seals identical to those at Harappa.\n\n"
            "Recognizing that these two widely separated sites represented a single monumental civilization, Sir John Marshall made a formal "
            "public announcement in the 'Illustrated London News' in September 1924, pushing back the verified antiquity of Indian urban civilization "
            "by more than two thousand years. Both metropolises revealed sophisticated dual-mound layouts consisting of a raised western Citadel "
            "and an expansive eastern Lower Town."
        )
    },
    {
        "chapter_number": 3,
        "title": "Urban Planning, Civic Architecture, and Brick Standardization",
        "content": (
            "The defining achievement of the Mature Harappan culture was its sophisticated urban planning, executed with a level of civic "
            "order unmatched in the ancient world. Settlements were planned along a cardinal grid system, where wide primary avenues ran strictly "
            "North-South and East-West, intersecting at precise ninety-degree right angles. Secondary residential lanes branched off logically, "
            "allowing natural wind currents to sweep through the streets.\n\n"
            "A key hallmark of this urban uniformity was the standardization of building materials. Kiln-burnt bricks, alongside sun-dried mud bricks, "
            "were manufactured across hundreds of settlements according to a strict universal ratio of 4:2:1 (Length : Breadth : Thickness). "
            "Whether excavated in the Indus floodplains, coastal Gujarat, or the foothills of the Himalayas, bricks conformed precisely to this mathematical "
            "proportion, typically measuring 28 × 14 × 7 cm for domestic walls.\n\n"
            "Crucially, Harappan urban centers were divided into distinct functional zones. The western Citadel, erected on massive artificial mud-brick "
            "platforms to safeguard against recurring seasonal inundations, housed civic institutions, granaries, and public assembly structures. "
            "The lower eastern sectors were reserved for residential quarters, merchant shops, and craft workshops."
        )
    },
    {
        "chapter_number": 4,
        "title": "The World's Earliest Subterranean Drainage System",
        "content": (
            "In no other ancient civilization—neither in Pharaonic Egypt nor in dynastic Mesopotamia—did municipal sanitation and public hygiene "
            "receive such meticulous attention as in the Harappan cities. Every major urban center was equipped with an engineered subterranean "
            "drainage system designed to evacuate waste safely away from domestic habitats.\n\n"
            "Domestic wastewater from bathing areas and latrines flowed through vertical terracotta pipes embedded within residential walls into "
            "covered masonry drains running alongside street avenues. Street channels were paved with burnt bricks and covered with fitted stone slabs "
            "or brick lids that could be lifted for periodic maintenance. To prevent clogging, drains incorporated inspection manholes, sumps, and "
            "sediment catch-basins where heavy solid waste accumulated before the filtered liquid discharged into municipal sewer mains.\n\n"
            "The crown jewel of Harappan hydraulic architecture is the Great Bath of Mohenjo-daro, situated on the Citadel mound. Measuring roughly "
            "12 meters by 7 meters with a depth of 2.4 meters, the rectangular basin was lined with finely fitted baked bricks joined with gypsum mortar. "
            "To achieve complete water tightness, engineers applied a thick insulating layer of natural bitumen (asphalt) between the inner brick course "
            "and the outer mud-brick backing. Flanked by colonnades and individual changing cubicles, scholars hypothesize that the Great Bath served "
            "civic or ritual purification functions."
        )
    },
    {
        "chapter_number": 5,
        "title": "Domestic Architecture and Daily Residential Life",
        "content": (
            "Harappan residential architecture prioritized individual privacy, structural durability, and climatic comfort. Domestic houses "
            "were organized around the central courtyard principle: a private, open-air inner courtyard served as the heart of the home, "
            "around which various rooms for sleeping, cooking, and storage were arranged.\n\n"
            "To maintain household seclusion from bustling street avenues, ground-floor walls featured no exterior windows; windows were placed "
            "exclusively on upper stories facing the internal courtyard. Main entrance doorways were positioned in narrow side lanes rather than "
            "directly on primary avenues, preventing passersby from looking directly into the residential interior.\n\n"
            "Many houses were two stories tall, as evidenced by preserved masonry staircases leading to upper floor levels. Homes were routinely equipped "
            "with private paved bathing platforms sloping toward wastewater drain chutes. In Mohenjo-daro alone, archaeologists estimate that "
            "over seven hundred public and private masonry-lined wells supplied a continuous, reliable source of fresh potable water to citizens."
        )
    },
    {
        "chapter_number": 6,
        "title": "Agrarian Economy and Hydraulic Adaptation",
        "content": (
            "The expansive urban populations of the Harappan Civilization were sustained by a highly productive agricultural hinterland. "
            "Peasants took advantage of annual river floodplains, sowing crops as floodwaters receded and harvesting yields before summer heat set in. "
            "The primary agricultural staples included bread wheat (Triticum aestivum), six-rowed barley, sesamum, field peas, and mustard. "
            "At coastal sites like Lothal and Rangpur in Gujarat, archaeological residues also indicate early cultivation of rice.\n\n"
            "A monumental archaeological discovery at Kalibangan in northern Rajasthan revealed the world's earliest known ploughed agricultural field, "
            "dating to the Early Harappan era. The field preserved distinct grid-pattern furrow marks: one set of furrows spaced closely East-West "
            "and a second set spaced wider North-South, demonstrating a sophisticated multi-cropping system identical to practices still utilized in the region today.\n\n"
            "In arid zones where perennial rivers were absent, Harappan engineers pioneered monumental water-harvesting systems. At Dholavira, "
            "located in the saline desert of the Rann of Kutch, engineers built sixteen mammoth rock-cut stepped reservoirs connected by stone dams. "
            "These reservoirs harvested storm run-off from seasonal rivulets (Manhar and Mansar), storing over two hundred and fifty thousand cubic "
            "meters of freshwater to sustain the city through prolonged dry spells."
        )
    },
    {
        "chapter_number": 7,
        "title": "Crafts, Metallurgy, and Lapidary Technology",
        "content": (
            "Harappan material culture showcased an advanced mastery of specialized craft industries, pyrotechnology, and metallurgical science. "
            "Coppersmiths alloyed copper with tin to produce durable bronze tools, utilitarian implements (saws, chisels, knives), and exquisite art pieces. "
            "Their mastery of the lost-wax casting technique (cire perdue) is immortalized in the spirited, naturalistic statuette known as the "
            "'Bronze Dancing Girl' excavated at Mohenjo-daro, depicting a young woman adorned with bangles in an expressive stance.\n\n"
            "Lapidary craftsmanship represented another major manufacturing triumph. Specialized industrial workshops, notably at Lothal in Gujarat "
            "and Chanhudaro in Sindh, mass-produced beads from precious and semi-precious stones, including carnelian, agate, jasper, steatite, and lapis lazuli. "
            "Harappan artisans perfected microscopic diamond and chert drills to perforate hard stone beads and developed chemical heating kilns to induce "
            "a deep carnelian red, followed by alkali acid-etching to produce white geometric patterns.\n\n"
            "Potters utilized fast-turning wheels to manufacture fine red-and-black pottery adorned with motifs of peacocks, pipal leaves, intersecting circles, "
            "and geometric grids. Terracotta modeling produced diverse domestic figurines, toy carts with moving wheels, and animal depictions."
        )
    },
    {
        "chapter_number": 8,
        "title": "Maritime and Overland Trade Networks (Meluhha)",
        "content": (
            "The Harappan economy was deeply integrated into extensive inter-regional and overseas commercial networks. Domestic trade was supported "
            "by two-wheeled bullock carts and riverine transport, acquiring copper from the Khetri mines of Rajasthan, gold from Karnataka, and lapis lazuli "
            "from the Badakhshan region in northern Afghanistan.\n\n"
            "Internationally, Harappans were prolific maritime merchants. At Lothal, on the Gulf of Khambhat in Gujarat, engineers constructed the world's "
            "earliest known tidal dockyard—a massive rectangular basin measuring 215 × 37 meters enclosed by burnt-brick revetments. The dockyard utilized "
            "automated sluice gates to lock in seawater during high tide, enabling deep-draft merchant vessels to berth safely and discharge cargo.\n\n"
            "Cuneiform clay tablets from Mesopotamian dynasties (dating from King Sargon of Akkad, c. 2350 BCE) extensively record sea trade with three "
            "foreign realms: Dilmun (modern Bahrain), Magan (Oman), and Meluhha. Historians widely identify 'Meluhha' as the Indus civilization. "
            "Mesopotamian records describe imports of carnelian beads, lapis lazuli, ivory combs, ebony, and cotton textiles from Meluhha, corroborated "
            "by the discovery of Indus-style steatite seals and cubical weights at Mesopotamian sites like Ur, Kish, and Nippur."
        )
    },
    {
        "chapter_number": 9,
        "title": "Seals, the Undeciphered Script, and Weights",
        "content": (
            "More than 3,500 miniature seals, primarily carved from soft steatite (soapstone) and baked to white hardness, constitute the most "
            "distinctive symbolic artifacts of the Harappan world. Most seals are square or rectangular intaglios featuring masterfully engraved "
            "animal profiles—predominantly the mythical single-horned 'unicorn', along with the humped zebu bull, elephant, tiger, and rhinoceros—accompanied "
            "by brief inscriptions.\n\n"
            "Among the most celebrated is the 'Pashupati Seal' from Mohenjo-daro, depicting a three-faced horned figure seated in a meditative yogic posture, "
            "surrounded by an elephant, tiger, rhinoceros, and buffalo, with two deer below. Archaeologists such as Sir John Marshall identified this as a "
            "proto-historic archetype of Shiva (Lord of Beasts), though interpretations continue to be discussed in modern academic circles.\n\n"
            "The Harappan script consists of roughly four hundred distinct pictographic and logo-syllabic signs, written predominantly from right to left. "
            "At Dholavira, archaeologists uncovered a monumental ten-character stone signboard once displayed over the northern city gate. "
            "Importantly, responsible historians emphasize that despite numerous decipherment claims (suggesting proto-Dravidian, Indo-Aryan, or Munda affinities), "
            "the Harappan script remains conclusively undeciphered due to the brevity of surviving inscriptions and the absence of a bilingual inscription "
            "such as the Rosetta Stone.\n\n"
            "To govern fair exchange, Harappans utilized a uniform binary-decimal weight system based on precision-cut cubical chert stones. "
            "Weights scaled by powers of two (1, 2, 4, 8, 16, 32...) in smaller denominations—with 16 equating to roughly 13.7 grams—before transitioning "
            "to decimal multiples (160, 320, 640) for heavier commercial trade."
        )
    },
    {
        "chapter_number": 10,
        "title": "Decline, Transformation, and Perennial Civilizational Legacy",
        "content": (
            "Around 1900 BCE, the mature urban phase of the Harappan Civilization entered a noticeable decline. Over the following centuries, "
            "monumental civic maintenance ceased, drainage systems fell into disuse, international maritime trade with Mesopotamia dwindled, and "
            "standardized seals and cubical weights disappeared from the archaeological record.\n\n"
            "Early twentieth-century theorists, notably Mortimer Wheeler, attributed this collapse to external violent invasions by Indo-Aryan migrants, "
            "citing unburied skeletal remains at Mohenjo-daro as evidence of a massacre. However, modern scientific archaeology and biological anthropology "
            "have conclusively rejected the 'Aryan invasion' catastrophe. Extensive physical re-examinations show no signs of military trauma or burnt "
            "destruction layers associated with warfare.\n\n"
            "Instead, modern scholars attribute the transformation to a convergence of climatic and hydrological disruptions:\n"
            "1. Shifting monsoon weather patterns, resulting in progressive aridification across western South Asia.\n"
            "2. Tectonic disturbances altering river channels and triggering the gradual desiccation of the perennial Ghaggar-Hakra (Saraswati) river system.\n"
            "3. Periodic disastrous flooding along the lower Indus basin.\n\n"
            "Crucially, the civilization did not vanish catastrophically; rather, it experienced de-urbanization and rural adaptation. Populations gradually "
            "migrated eastward and southward into the fertile Gangetic plains and Gujarat. Their agricultural knowledge, copper-working traditions, "
            "pottery forms, water-purification practices, and spiritual iconography (such as sacred tree worship and yogic motifs) seamlessly merged into the "
            "broader, continuous tapestry of historical Indian culture."
        )
    }
]

# -------------------------------------------------------------------
# 2. TIMELINE EVENTS (10 Verified Chronological Milestones)
# -------------------------------------------------------------------
TIMELINE_EVENTS = [
    {
        "year": "c. 7000 - 3300 BCE",
        "title": "Neolithic Prelude at Mehrgarh",
        "description": "Settled agro-pastoral communities cultivate barley and wheat, domesticate cattle, and develop early mud-brick architecture in Balochistan."
    },
    {
        "year": "c. 3300 - 2600 BCE",
        "title": "Early Harappan Phase",
        "description": "Emergence of regional farming cultures (Ravi, Kot Diji, and Hakra wares), fortified villages, early copper metallurgy, and initial seal-carving."
    },
    {
        "year": "c. 2600 BCE",
        "title": "Dawn of the Mature Urban Phase",
        "description": "Emergence of planned metropolises with cardinal grid systems, standardized burnt bricks, and centralized civic infrastructure."
    },
    {
        "year": "c. 2500 BCE",
        "title": "Hydraulic Marvels at Mohenjo-daro",
        "description": "Construction of the Great Bath with natural bitumen waterproofing and extensive municipal covered drainage networks."
    },
    {
        "year": "c. 2400 BCE",
        "title": "Establishment of Lothal Tidal Dockyard",
        "description": "Harappan engineers construct a brick basin dockyard on the Gulf of Khambhat in Gujarat, inaugurating international oceanic trade."
    },
    {
        "year": "c. 2350 BCE",
        "title": "Peak Trade with Mesopotamia (Meluhha)",
        "description": "Cuneiform records from Sargon of Akkad document oceanic trade in carnelian, lapis lazuli, and ivory with the land of Meluhha."
    },
    {
        "year": "c. 2200 BCE",
        "title": "Dholavira Water Harvesting and Signboard",
        "description": "Construction of sixteen stone-cut rainwater reservoirs and display of the 10-character monumental signboard at Dholavira in Kutch."
    },
    {
        "year": "c. 1900 BCE",
        "title": "De-urbanization and the Late Harappan Phase",
        "description": "Weakening monsoons and river desiccation lead to the gradual abandonment of major cities and eastward migration toward the Ganga basin."
    },
    {
        "year": "1920 - 1921 CE",
        "title": "Excavation of Harappa by Daya Ram Sahni",
        "description": "Archaeological Survey of India unearths the first Bronze Age citadel mounds and seals at Harappa in Punjab."
    },
    {
        "year": "1922 - 1924 CE",
        "title": "Discovery of Mohenjo-daro and World Announcement",
        "description": "Rakhaldas Banerjee discovers Mohenjo-daro; Sir John Marshall announces the discovery of the Indus Civilization to the world."
    }
]

# -------------------------------------------------------------------
# 3. IMPORTANT PEOPLE / GROUPS (8 Key Historical Figures & Groups)
# -------------------------------------------------------------------
PEOPLE = [
    {
        "name": "Rai Bahadur Daya Ram Sahni",
        "role": "Pioneering Indian Archaeologist (ASI)",
        "description": "The first Indian Director-General of the Archaeological Survey of India who began systematic excavations at Harappa in Punjab in 1920–1921, discovering the civilization's first major urban ruins."
    },
    {
        "name": "Rakhaldas Banerjee (R. D. Banerji)",
        "role": "Discoverer of Mohenjo-daro",
        "description": "Distinguished historian and archaeologist who discovered the prehistoric remains of Mohenjo-daro in Sindh in 1922 while investigating an ancient Buddhist stupa mound."
    },
    {
        "name": "Sir John Marshall",
        "role": "Director-General of the ASI (1902–1928)",
        "description": "British archaeologist who coordinated the excavations at Harappa and Mohenjo-daro and made the historic 1924 public announcement revealing the Bronze Age Indus civilization to the world."
    },
    {
        "name": "Dr. S. R. Rao",
        "role": "Excavator of Lothal Port",
        "description": "Pioneering marine archaeologist who directed excavations at Lothal in Gujarat between 1954 and 1962, identifying the world's earliest known tidal dockyard and carnelian bead kilns."
    },
    {
        "name": "Dr. R. S. Bisht",
        "role": "Excavator of Dholavira",
        "description": "Renowned archaeologist who directed the multi-year excavation of Dholavira in the Rann of Kutch from 1990 onwards, uncovering its sophisticated rock-cut water reservoirs and city signboard."
    },
    {
        "name": "The Harappan Merchant Guilds",
        "role": "Inter-Regional and Maritime Traders",
        "description": "The mercantile class that governed oceanic trade with Mesopotamia, Dilmun, and Magan, utilizing standardized cubical chert weights and engraved steatite seals for commercial identification."
    },
    {
        "name": "The Specialized Artisans and Metallurgists",
        "role": "Craft Communities of the Indus",
        "description": "Highly skilled craftsmen who perfected lost-wax bronze casting (cire perdue), micro-drilling of carnelian beads at Chanhudaro, and wheel-thrown painted pottery across urban workshops."
    },
    {
        "name": "The Civic Authorities and Town Planners",
        "role": "Municipal Engineers of Harappan Cities",
        "description": "The anonymous municipal administrators responsible for enforcing the cardinal grid street layout, uniform 4:2:1 brick ratios, and maintenance of public subterranean drainage systems."
    }
]

# -------------------------------------------------------------------
# 4. IMPORTANT PLACES (8 Strategic Archaeological Sites)
# -------------------------------------------------------------------
PLACES = [
    {
        "name": "Harappa",
        "location": "Sahiwal (Montgomery) District, Punjab (Ravi River basin)",
        "description": "The first excavated type-site of the civilization, featuring extensive citadel mounds, work platforms for grain thrashing, and monumental granary structures."
    },
    {
        "name": "Mohenjo-daro",
        "location": "Larkana District, Sindh (Indus River basin)",
        "description": "The largest metropolis of the civilization, renowned for the Great Bath, the Great Granary/Warehouse, paved multi-story brick homes, and over 700 municipal water wells."
    },
    {
        "name": "Lothal",
        "location": "Ahmedabad District, Gujarat (Bhogavo River / Gulf of Khambhat)",
        "description": "Ancient coastal port city featuring the world's earliest known tidal dockyard with automated sluice gates, carnelian bead-making workshops, and double burial sites."
    },
    {
        "name": "Dholavira",
        "location": "Khadir Bet, Great Rann of Kutch, Gujarat",
        "description": "UNESCO World Heritage city celebrated for monumental dressed-stone architecture, 16 rock-cut rainwater reservoirs, a ceremonial stadium, and a 10-glyph city signboard."
    },
    {
        "name": "Kalibangan",
        "location": "Hanumangarh District, Rajasthan (Ghaggar River basin)",
        "description": "Archaeological site famous for uncovering the world's oldest grid-furrow ploughed agricultural field, rows of ritual fire altars, and distinctive terracotta bangles."
    },
    {
        "name": "Rakhigarhi",
        "location": "Hisar District, Haryana (Ghaggar-Hakra basin)",
        "description": "Currently recognized as the largest known geographical site of the Harappan civilization, spanning over 350 hectares of residential mounds and cemeteries."
    },
    {
        "name": "Chanhudaro",
        "location": "Nawabshah District, Sindh",
        "description": "A specialized industrial manufacturing town with zero citadel fortifications, dedicated entirely to shell-working, seal-engraving, and carnelian bead production."
    },
    {
        "name": "Banawali",
        "location": "Fatehabad District, Haryana",
        "description": "Fortified settlement situated along the ancient Saraswati riverbed, known for radial street planning, high-quality barley seeds, and terracotta plough models."
    }
]

# -------------------------------------------------------------------
# 5. INTERESTING FACTS (10 Verified Historical Facts)
# -------------------------------------------------------------------
FACTS = [
    "Standardized Burnt-Brick Ratio: Across hundreds of miles, every Harappan kiln produced bricks in the strict ratio of 4:2:1 (length : breadth : height), optimal for structural stability.",
    "World's Earliest Subterranean Drainage: Covered street sewers with sediment catch-pits existed in Harappan cities in 2500 BCE, millennia before comparable European sanitation.",
    "The Undeciphered Script: Despite over 400 distinct glyphs written right-to-left, the Harappan script remains unread due to short inscriptions and lack of bilingual texts.",
    "Absence of Monarchy and War Monuments: No lavish palaces, royal pyramids, or depictions of military conquests exist in Harappan sites, suggesting an egalitarian or civic-council governance.",
    "Precision Binary-Decimal Weights: Harappans used chert cube weights scaling in binary (1, 2, 4, 8, 16, 32...) in lower values (~13.7g unit) and decimal multiples in higher values.",
    "Dholavira's Hydraulic Marvel: In the arid Rann of Kutch, engineers built 16 stepped stone reservoirs holding 250,000 cubic meters of rainwater, sustaining the city through droughts.",
    "Natural Bitumen Waterproofing: The Great Bath of Mohenjo-daro used gypsum mortar and an insulating layer of natural bitumen (asphalt) sealed between brick walls.",
    "Mesopotamian Trade Identity (Meluhha): Cuneiform clay tablets from Akkad and Ur describe oceanic imports of carnelian, lapis lazuli, and ivory from the distant land of Meluhha.",
    "Prehistoric Agrarian Innovation: The world's earliest ploughed field discovered at Kalibangan shows dual-crop furrow patterns identical to modern mustard and chickpea cultivation.",
    "De-urbanization Rather than Annihilation: Modern scientific archaeology confirms that shifting monsoons and river desiccation led to gradual rural migration rather than an 'Aryan invasion'."
]

# -------------------------------------------------------------------
# 6. QUIZ QUESTIONS (15 Multiple-Choice Questions)
# -------------------------------------------------------------------
QUIZ_QUESTIONS = [
    {
        "question": "Which Indian archaeologist excavated the first major site of Harappa in Punjab in 1920-1921?",
        "option_a": "Rakhaldas Banerjee",
        "option_b": "Daya Ram Sahni",
        "option_c": "S. R. Rao",
        "option_d": "R. S. Bisht",
        "correct_option": "B",
        "explanation": "Rai Bahadur Daya Ram Sahni began excavations at Harappa in 1920 under the director-generalship of Sir John Marshall."
    },
    {
        "question": "Who discovered the ruins of Mohenjo-daro in Sindh in 1922?",
        "option_a": "Daya Ram Sahni",
        "option_b": "Rakhaldas Banerjee",
        "option_c": "Mortimer Wheeler",
        "option_d": "Alexander Cunningham",
        "correct_option": "B",
        "explanation": "Rakhaldas Banerjee discovered Mohenjo-daro in 1922 while investigating an ancient Buddhist stupa mound."
    },
    {
        "question": "What was the standardized dimensional ratio of bricks used across Harappan cities?",
        "option_a": "3:2:1",
        "option_b": "4:2:1",
        "option_c": "5:3:2",
        "option_d": "4:3:1",
        "correct_option": "B",
        "explanation": "Harappan kiln-burnt and mud bricks adhered strictly to the ratio of 4:2:1 (Length : Breadth : Thickness)."
    },
    {
        "question": "At which Harappan coastal site in Gujarat was the world's earliest known tidal dockyard discovered?",
        "option_a": "Dholavira",
        "option_b": "Lothal",
        "option_c": "Kalibangan",
        "option_d": "Surkotada",
        "correct_option": "B",
        "explanation": "Lothal featured a brick dockyard basin engineered with sluice gates on the Gulf of Khambhat to berth trading ships."
    },
    {
        "question": "Which natural material was used to waterproof the Great Bath of Mohenjo-daro between its brick layers?",
        "option_a": "Lime plaster alone",
        "option_b": "Natural bitumen (asphalt)",
        "option_c": "Molten lead",
        "option_d": "Clay wax",
        "correct_option": "B",
        "explanation": "Engineers lined the Great Bath with gypsum mortar and an insulating layer of natural bitumen (asphalt) to achieve water tightness."
    },
    {
        "question": "Which Harappan city in Kutch is celebrated for its 16 rock-cut rainwater reservoirs and 10-glyph city signboard?",
        "option_a": "Lothal",
        "option_b": "Dholavira",
        "option_c": "Banawali",
        "option_d": "Rakhigarhi",
        "correct_option": "B",
        "explanation": "Dholavira is renowned for its stone rainwater reservoirs and a monumental 10-character signboard found at its northern citadel gate."
    },
    {
        "question": "At which Harappan site in Rajasthan was the world's oldest ploughed agricultural field discovered?",
        "option_a": "Harappa",
        "option_b": "Kalibangan",
        "option_c": "Chanhudaro",
        "option_d": "Rakhigarhi",
        "correct_option": "B",
        "explanation": "Kalibangan preserved grid-pattern furrow marks demonstrating sophisticated multi-crop agriculture."
    },
    {
        "question": "What animal is depicted most frequently on Harappan carved steatite seals?",
        "option_a": "The Royal Bengal Tiger",
        "option_b": "The Unicorn (single-horned mythical creature)",
        "option_c": "The Humped Zebu Bull",
        "option_d": "The Indian Elephant",
        "correct_option": "B",
        "explanation": "The mythical single-horned 'unicorn' appears on more than 60 percent of all discovered Harappan seals."
    },
    {
        "question": "The famous statuette known as the 'Dancing Girl' discovered at Mohenjo-daro is cast from which material?",
        "option_a": "Terracotta",
        "option_b": "Bronze",
        "option_c": "Steatite",
        "option_d": "Copper alloyed with silver",
        "correct_option": "B",
        "explanation": "The 10.5-centimeter figurine was cast in bronze using the ancient lost-wax technique (cire perdue)."
    },
    {
        "question": "By what geographic name is the Indus civilization believed to be referred to in ancient Mesopotamian cuneiform tablets?",
        "option_a": "Dilmun",
        "option_b": "Magan",
        "option_c": "Meluhha",
        "option_d": "Elam",
        "correct_option": "C",
        "explanation": "Akkadian and Ur records describe oceanic trade in carnelian, lapis lazuli, and ivory with the land of Meluhha."
    },
    {
        "question": "What soft mineral stone was primarily used by Harappan craftsmen to carve seals?",
        "option_a": "Granite",
        "option_b": "Steatite (Soapstone)",
        "option_c": "Sandstone",
        "option_d": "Basalt",
        "correct_option": "B",
        "explanation": "Harappan seals were carved from soft steatite (soapstone) and heated in kilns to whiten and harden them."
    },
    {
        "question": "What mathematical characteristic defined the precision Harappan cubical chert weight system?",
        "option_a": "Purely decimal throughout",
        "option_b": "Binary in lower denominations, Decimal in higher denominations",
        "option_c": "Duodecimal (base-12)",
        "option_d": "Random unstandardized stones",
        "correct_option": "B",
        "explanation": "Weights scaled in powers of 2 (1, 2, 4, 8, 16, 32...) in lower units and in decimal multiples (160, 320, 640) for larger goods."
    },
    {
        "question": "Which site in Haryana is currently recognized by archaeologists as the largest known settlement of the Harappan civilization?",
        "option_a": "Mohenjo-daro",
        "option_b": "Rakhigarhi",
        "option_c": "Banawali",
        "option_d": "Kalibangan",
        "correct_option": "B",
        "explanation": "Rakhigarhi in Haryana spans over 350 hectares, making it the largest documented Harappan settlement."
    },
    {
        "question": "What is the current academic consensus regarding the decipherment of the Harappan script?",
        "option_a": "It was fully deciphered as Sanskrit in 1950",
        "option_b": "It remains conclusively undeciphered due to brief texts and lack of bilingual inscriptions",
        "option_c": "It was proven to be identical to Mesopotamian cuneiform",
        "option_d": "It has been officially translated as ancient Greek",
        "correct_option": "B",
        "explanation": "Despite various proposed theories, the script remains undeciphered due to short inscriptions and the absence of a bilingual key."
    },
    {
        "question": "What do modern geological and climatic studies indicate was the primary factor in the de-urbanization of the Harappan Civilization around 1900 BCE?",
        "option_a": "A single catastrophic foreign military invasion",
        "option_b": "Weakening monsoons, shifting river courses, and drying of the Ghaggar-Hakra river system",
        "option_c": "A volcanic eruption across Gujarat",
        "option_d": "A sudden meteorite impact",
        "correct_option": "B",
        "explanation": "Climatic data confirms that shifting monsoons and the progressive drying of the Ghaggar-Hakra river triggered gradual rural migration."
    }
]


# -------------------------------------------------------------------
# DATABASE SEEDING FUNCTION
# -------------------------------------------------------------------
def load_harappan_data():
    """
    Inserts the complete historical dataset for Harappan Civilization
    into the SQLite database without modifying previous datasets.
    """
    # Ensure tables exist
    database.create_tables()

    # Check if Harappan topic already exists
    topics = database.get_topics()
    topic_id = None
    for t in topics:
        if "Harappan" in t["title"]:
            topic_id = t["id"]
            break

    # If topic does not exist, add it
    if topic_id is None:
        topic_id = database.add_topic(
            title="Harappan Civilization",
            period="c. 3300 - 1300 BCE",
            summary=(
                "Pioneering Bronze Age civilization renowned for grid urban planning, subterranean drainage, "
                "standardized weights, and international maritime trade."
            )
        )
        print(f"[OK] Created topic: Harappan Civilization (Topic ID: {topic_id})")
    else:
        print(f"[OK] Found existing topic: Harappan Civilization (Topic ID: {topic_id})")

    # Clear old data for Harappan only, preserving Shivaji and Sambhaji completely
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chapters WHERE topic_id = ?", (topic_id,))
    cursor.execute("DELETE FROM timeline WHERE topic_id = ?", (topic_id,))
    cursor.execute("DELETE FROM people WHERE topic_id = ?", (topic_id,))
    cursor.execute("DELETE FROM places WHERE topic_id = ?", (topic_id,))
    cursor.execute("DELETE FROM facts WHERE topic_id = ?", (topic_id,))
    cursor.execute("DELETE FROM quiz_questions WHERE topic_id = ?", (topic_id,))
    conn.commit()
    conn.close()

    # 1. Insert 10 Chapters
    for ch in CHAPTERS:
        database.add_chapter(topic_id, ch["chapter_number"], ch["title"], ch["content"])
    print(f"[OK] Inserted {len(CHAPTERS)} chapters for Harappan Civilization.")

    # 2. Insert 10 Timeline Events
    for ev in TIMELINE_EVENTS:
        database.add_timeline_event(topic_id, ev["year"], ev["title"], ev["description"])
    print(f"[OK] Inserted {len(TIMELINE_EVENTS)} timeline events.")

    # 3. Insert 8 Important People / Groups
    for p in PEOPLE:
        database.add_person(topic_id, p["name"], p["role"], p["description"])
    print(f"[OK] Inserted {len(PEOPLE)} important people/groups.")

    # 4. Insert 8 Important Places
    for pl in PLACES:
        database.add_place(topic_id, pl["name"], pl["location"], pl["description"])
    print(f"[OK] Inserted {len(PLACES)} important places.")

    # 5. Insert 10 Facts
    for f in FACTS:
        database.add_fact(topic_id, f)
    print(f"[OK] Inserted {len(FACTS)} facts.")

    # 6. Insert 15 Quiz Questions
    for q in QUIZ_QUESTIONS:
        database.add_quiz_question(
            topic_id,
            q["question"],
            q["option_a"],
            q["option_b"],
            q["option_c"],
            q["option_d"],
            q["correct_option"],
            q["explanation"]
        )
    print(f"[OK] Inserted {len(QUIZ_QUESTIONS)} quiz questions.")

    print(f"\n[SUCCESS] Harappan Civilization dataset loaded into database successfully!")
    return topic_id


if __name__ == "__main__":
    print("Loading Harappan Civilization dataset into SQLite database...")
    load_harappan_data()
