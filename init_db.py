"""
IndicRoots - Database Initialization & Seeding Script
Populates indicroots.db with rich historical curricula, figures, places, facts, timelines, and 70+ quiz questions.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "indicroots.db")

def init_database():
    """Initializes tables and seeds historical datasets."""
    if os.path.exists(DB_PATH):
        try:
            os.remove(DB_PATH)
            print("Removed existing database for a fresh initialization.")
        except Exception as e:
            print(f"Notice: {e}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create Tables
    cursor.executescript("""
    CREATE TABLE topics (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        icon TEXT NOT NULL,
        period TEXT NOT NULL,
        summary TEXT NOT NULL,
        overview TEXT NOT NULL,
        accent_color TEXT NOT NULL,
        display_order INTEGER NOT NULL
    );

    CREATE TABLE chapters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id TEXT NOT NULL,
        chapter_number INTEGER NOT NULL,
        title TEXT NOT NULL,
        subtitle TEXT NOT NULL,
        content TEXT NOT NULL,
        key_quote TEXT,
        FOREIGN KEY (topic_id) REFERENCES topics(id)
    );

    CREATE TABLE people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id TEXT NOT NULL,
        name TEXT NOT NULL,
        role_title TEXT NOT NULL,
        lifespan TEXT NOT NULL,
        bio TEXT NOT NULL,
        achievements TEXT NOT NULL,
        quote TEXT,
        avatar_icon TEXT DEFAULT '👤',
        display_order INTEGER DEFAULT 1,
        FOREIGN KEY (topic_id) REFERENCES topics(id)
    );

    CREATE TABLE places (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id TEXT NOT NULL,
        name TEXT NOT NULL,
        location TEXT NOT NULL,
        significance TEXT NOT NULL,
        architecture_style TEXT NOT NULL,
        description TEXT NOT NULL,
        key_features TEXT NOT NULL,
        display_order INTEGER DEFAULT 1,
        FOREIGN KEY (topic_id) REFERENCES topics(id)
    );

    CREATE TABLE facts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id TEXT NOT NULL,
        headline TEXT NOT NULL,
        detail TEXT NOT NULL,
        category TEXT NOT NULL,
        FOREIGN KEY (topic_id) REFERENCES topics(id)
    );

    CREATE TABLE timeline_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id TEXT NOT NULL,
        year_display TEXT NOT NULL,
        sort_year INTEGER NOT NULL,
        title TEXT NOT NULL,
        location TEXT NOT NULL,
        description TEXT NOT NULL,
        importance TEXT DEFAULT 'Major',
        FOREIGN KEY (topic_id) REFERENCES topics(id)
    );

    CREATE TABLE quiz_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id TEXT NOT NULL,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_option TEXT NOT NULL,
        explanation TEXT NOT NULL,
        difficulty TEXT DEFAULT 'Medium',
        FOREIGN KEY (topic_id) REFERENCES topics(id)
    );

    CREATE TABLE quiz_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        score INTEGER NOT NULL,
        total_questions INTEGER NOT NULL,
        percentage REAL NOT NULL
    );

    CREATE INDEX idx_timeline_sort ON timeline_events(sort_year);
    CREATE INDEX idx_quiz_topic ON quiz_questions(topic_id);
    """)

    # 1. SEED TOPICS
    topics_data = [
        (
            "shivaji",
            "Chhatrapati Shivaji Maharaj",
            "⚔️",
            "1630 – 1680 CE",
            "The architect of Hindavi Swarajya who transformed guerrilla tactics (*Ganimi Kawa*) and sea defenses into an enduring sovereign empire.",
            """Chhatrapati Shivaji Maharaj (1630–1680) redefined medieval Indian geopolitics by establishing **Hindavi Swarajya** (self-rule of the native people). Rising in the Western Ghats against the Adilshahi Sultanate and the mighty Mughal Empire, he pioneered agile guerrilla warfare (*Ganimi Kawa*), built India's premier naval defense system, instituted welfare-centric agrarian governance, and dismantled hereditary feudal oppressions while upholding religious freedom and dignity for all subjects.""",
            "#E06D14",
            1
        ),
        (
            "sambhaji",
            "Chhatrapati Sambhaji Maharaj",
            "🛡️",
            "1657 – 1689 CE",
            "The undefeated second Chhatrapati, literary scholar of Sanskrit, and fearless commander who defended Swarajya against continuous multi-front invasions.",
            """Chhatrapati Sambhaji Maharaj (1657–1689), elder son of Shivaji Maharaj, was an extraordinary polymath and warrior king. Across nine tempestuous years of reign, he fought over 120 military engagements against the imperial forces of Aurangzeb, the Portuguese Viceroyalty of Goa, the Siddis of Janjira, and Chikka Devaraja of Mysore without suffering a single defeat. A profound scholar fluent in Sanskrit, Marathi, and Brajbhasha, his supreme martyrdom at Tulapur cemented his revered status as *Dharmaveer*.""",
            "#B33927",
            2
        ),
        (
            "harappa",
            "Harappan Civilization",
            "🏺",
            "c. 3300 – 1300 BCE",
            "The Indus-Saraswati civilization that pioneered monumental grid urbanism, covered subterranean drainage, standardized weights, and international maritime trade.",
            """The Harappan (Indus-Saraswati) Civilization was the largest of the four ancient Old World cradles of civilization, spanning over a million square kilometers across modern India and Pakistan. Renowned for its masterfully planned cities (such as Mohenjo-daro, Harappa, Lothal, and Dholavira), it boasted standardized burnt-brick architecture, the world's earliest known tidal dockyard, covered subterranean drainage systems, advanced metallurgy, and intricate seals that remain one of history's great undeciphered linguistic enigmas.""",
            "#D4AF37",
            3
        ),
        (
            "revolt1857",
            "The Revolt of 1857",
            "🔥",
            "1857 – 1858 CE",
            "India's First War of Independence that united sepoys, dispossessed monarchs, and peasants, permanently ending the British East India Company's rule.",
            """The Indian Uprising of 1857 was a seismic anti-colonial watershed. Sparked by simmering resentments against economic drainage, administrative high-handedness (Doctrine of Lapse), and the grease-cartridge controversy, soldiers, peasants, and regional royals rose in unison across northern and central India. Marked by heroic resistance from Rani Lakshmibai of Jhansi, Tatya Tope, Nana Saheb, Begum Hazrat Mahal, and Veer Kunwar Singh, the revolt broke the East India Company's monopoly and gave birth to modern Indian nationalism.""",
            "#C9381E",
            4
        )
    ]
    cursor.executemany("INSERT INTO topics VALUES (?,?,?,?,?,?,?,?)", topics_data)

    # 2. SEED CHAPTERS (4 per topic = 16 chapters)
    chapters_data = [
        # SHIVAJI MAHARAJ
        (
            "shivaji", 1,
            "The Oath of Swarajya & Early Conquests",
            "From the Raireshwar Temple Pledge (1645) to the Capture of Torna",
            """In 1645, a fifteen-year-old Shivaji, accompanied by loyal Mavala companions such as Tanaji Malusare, Yesaji Kank, and Baji Pasalkar, gathered inside the secluded **Raireshwar Temple** nestled deep in the Sahyadri mountains. There, with hands placed upon the sacred Shivling, they swore an unyielding pledge to establish *Hindavi Swarajya* (self-rule rooted in justice and native dignity).

Shivaji's strategic brilliance manifested immediately. Rather than challenging the entrenched Adilshahi Sultanate in plains warfare, he targeted commanding mountain citadels. His first triumph was the bloodless capture of **Torna Fort** (Prachandgad) in 1646. While repairing the defenses of Torna, workers unearthed pots filled with buried gold treasures. Rejecting personal enrichment, Shivaji used every coin to construct the neighboring fortress of **Rajgad**, which served as his imperial capital for over twenty-five years.

By capturing Kondhana, Purandar, and Chakan, Shivaji established an unassailable bastion across the Sahyadri range, turning rugged topography into an impenetrable shield.""",
            "\"This Kingdom is not mine; it is the will of Providence that Hindavi Swarajya be established.\""
        ),
        (
            "shivaji", 2,
            "Ganimi Kawa & The Pratapgad Encounter (1659)",
            "The Annihilation of Afzal Khan's Armada and Tactical Guerrilla Warfare",
            """By 1659, the Adilshahi Sultanate of Bijapur dispatched its most formidable general, **Afzal Khan**, with a massive army of 10,000 cavalry, heavy artillery, and war elephants, sworn to capture Shivaji dead or alive. Khan desecrated sacred shrines across Tuljapur and Pandharpur to lure Shivaji onto open plains.

Recognizing the tactical suicidal nature of pitched open-ground combat, Shivaji withdrew to the dense, malaria-ridden forests surrounding **Pratapgad Fort**. He feigned vulnerability and enticed Afzal Khan to a personal parley at the base of the fort, with strict terms of carrying only one bodyguard each.

Aware of Khan's notorious track record of deceit (such as the treacherous murder of Kasturi Ranga of Sera), Shivaji wore iron chainmail beneath his tunic, hid a steel helmet under his turban, and concealed *Wagh Nakh* (tiger claws) and a *Bichawa* (scorpion dagger) in his sleeves. When Khan embraced Shivaji and attempted to strangle him with a dagger thrust, the armor deflected the blow. Shivaji struck back with lightning ferocity. The Maratha infantry ambushed the leaderless Adilshahi force in the dense valley of Jawali, capturing cannons, thousands of horses, and shattering Bijapur's military backbone.""",
            "\"Let the enemy have numbers; we hold the terrain, the spirit of our ancestors, and the speed of lightning.\""
        ),
        (
            "shivaji", 3,
            "The Masterclass Escapes & Sea Fort Maritime Power",
            "The Sacrifice at Pavan Khind, Lal Mahal Raid, and Founding of the Maratha Navy",
            """Shivaji's military career was characterized by peerless strategic improvisation:
1. **The Siege of Panhala & Pavan Khind (1660)**: Besieged by Siddi Jauhar at Panhala, Shivaji engineered a daring rainy night breakout. When Adilshahi pursuers closed in, Commander **Baji Prabhu Deshpande** and 300 Mavala warriors defended the narrow mountain pass of Ghodkhind against 4,000 enemy troops until signal cannon shots confirmed Shivaji had safely reached Vishalgad. The pass was immortalized as *Pavan Khind* (The Sacred Pass).
2. **The Surgical Strike on Lal Mahal (1663)**: When Mughal viceroy Shaista Khan occupied Shivaji's childhood palace in Pune with 70,000 troops, Shivaji led 400 commando warriors into the palace under cover of a wedding procession, severed Shaista Khan's fingers in his bedchamber, and escaped before the garrison could mobilize.
3. **The Maratha Navy & Sea Forts**: Shivaji was among the first rulers in medieval India to grasp naval geopolitics: *"He who rules the seas rules the realm."* He commissioned a formidable fleet of *Gurabs* and *Galbats*, and constructed impregnable maritime fortresses like **Sindhudurg** (anchored with molten lead into granite sea reefs), **Vijaydurg**, and **Suvarnadurg** to counter Portuguese, British, and Siddi maritime supremacy.""",
            "\"Jalyukta Durganchi Srushti (Creation of Sea Forts): The master of the sea is master of the realm.\""
        ),
        (
            "shivaji", 4,
            "Rajyabhisheka (1674) & Enlightened Governance",
            "Coronation at Raigad, the Ashta Pradhan Council, and Agrarian Reforms",
            """On **6 June 1674**, atop the magnificent plateau of **Raigad Fort**, Shivaji was consecrated as an independent, sovereign Hindu monarch with the title *Kshatriya Kulavantas Chhatrapati Shivaji Maharaj*. Master of Vedic rites Gaga Bhatt of Varanasi officiated the ceremony before international dignitaries, including British envoy Henry Oxenden.

Shivaji was far more than a legendary conqueror; he was a revolutionary administrator:
- **Ashta Pradhan**: An eight-minister cabinet comprising the *Peshwa* (Prime Minister), *Amatya* (Finance), *Senapati* (Commander-in-Chief), *Sachiv* (State Secretary), *Mantri* (Intelligence), *Sumant* (Foreign Relations), *Panditrao* (Religious Affairs), and *Nyayadhish* (Chief Justice).
- **Agrarian Welfare**: He abolished oppressive *Watandari* hereditary tax farming. State tax was strictly capped at 40% of actual agricultural yields, payable in grain during droughts.
- **Ecological & Humanist Decrees**: His royal edicts (*Adnyapatra*) forbade the felling of fruit-bearing trees without owner compensation and mandated severe court-martial punishment for harming non-combatants, women, mosques, or copies of the Quran during military campaigns.""",
            "\"The ryots (farmers) are not to be troubled. Do not seize even the stem of a peasant's vegetable without just payment.\""
        ),

        # SAMBHAJI MAHARAJ
        (
            "sambhaji", 1,
            "The Prince of Valour & Scholarly Polymath",
            "Education, Military Apprenticeship, and Literary Triumphs",
            """Born on **14 May 1657** at the cloud-kissed heights of Purandar Fort, Sambhaji was raised by his revered grandmother, **Rajmata Jijabai**, following the untimely demise of his mother, Maharani Saibai. Recognizing his razor-sharp intellect, Shivaji ensured the prince mastered military science, equestrian archery, and statecraft alongside classical languages.

By age nine, Sambhaji accompanied Shivaji to the Mughal court at Agra in 1666, observing imperial power dynamics firsthand. At age fourteen, his literary genius manifested in the composition of **Budhabhushanam**—a brilliant Sanskrit treatise spanning statecraft, royal ethics, military diplomacy, and political morality. He subsequently authored *Nakhshikh* and *Nayikabhed* in Brajbhasha, proving himself as adept with the pen as he was with the sword.

Appointed commander of key Maratha detachments, he displayed fearless tactical leadership at the siege of Janjira and across the Deccan borderlands, earning the ardent loyalty of veterans and soldiers.""",
            "\"A ruler without knowledge of Rajneeti (statecraft) is like a ship in a storm without a rudder.\" — Budhabhushanam"
        ),
        (
            "sambhaji", 2,
            "Ascension & The Imperial Deccan Quagmire",
            "Aurangzeb's Southern Campaign and the Multi-Front Maratha Defense",
            """Ascending the throne at Raigad in January 1681 following internal succession intrigues, Chhatrapati Sambhaji faced an existential crisis. Mughal Emperor **Aurangzeb**, infuriated by Sambhaji granting asylum to the rebel Mughal prince Sultan Muhammad Akbar, marched south with an unprecedented imperial armada: over 500,000 soldiers, 100,000 cavalry, and immense siege artillery.

Aurangzeb arrogantly vowed never to return to Delhi until he had annihilated the Maratha state. Instead, Sambhaji inflicted a grueling war of attrition that lasted eight bloody years. 

Employing hyper-mobile cavalry strikes, Sambhaji attacked Mughal supply depots in Khandesh and Berar, raided the wealthy trading metropolis of **Burhanpur**, and defeated imperial divisions led by top generals like Shihab-ud-Din, Bahadur Khan, and Prince Azam. Sambhaji's strategic coordination kept half a million imperial troops trapped in the barren Deccan hills, draining the Mughal treasury and destroying imperial morale.""",
            "\"Let the Emperor bring his five hundred thousand. The Sahyadri rocks will crush his imperial delusions.\""
        ),
        (
            "sambhaji", 3,
            "The Invictus Record: 120 Battles & The Goa Campaign",
            "Humbling Portuguese Imperialism and Crushing the Siddis",
            """During his nine-year reign, Sambhaji fought over **120 military engagements without suffering a single defeat**—an unmatched feat in medieval military annals.

In 1683, when the Portuguese Viceroy in Goa entered into an unholy alliance with Aurangzeb, Sambhaji launched a devastating counter-offensive. Crossing the swollen Mandovi River at low tide, Maratha troops stormed the fortress of **Santo Estevão** (St. Stephen's Island) and laid siege to Chapora and Alorna. The Portuguese Viceroy, Francisco de Távora, was severely wounded, and the colonial administration in Old Goa was pushed to the absolute brink of annihilation. The Viceroy had to pray at the tomb of St. Francis Xavier, begging for divine intervention before a sudden Mughal troop advance from the north forced Sambhaji to redirect his cavalry.

Simultaneously, Sambhaji constructed a 2-kilometer stone bridge into the sea to storm the island fortress of Janjira, breaking the naval dominance of the Siddi pirates.""",
            "\"Neither the Portuguese muskets nor the Sultan's cannons could bend his resolve upon the field of battle.\""
        ),
        (
            "sambhaji", 4,
            "The Supreme Sacrifice at Tulapur (1689)",
            "Dharmaveer: Unbreakable Defiance in the Face of Martyrdom",
            """In early 1689, while returning from a strategic conference at Vishalgad, Sambhaji Maharaj and his trusted poet-minister **Kavi Kalash** stopped at the village of **Sangameshwar**. Betrayed by local conspirators who revealed their lightly guarded location, they were ambushed by Muqarrab Khan's detachment after a fierce defensive stand.

Brought before Aurangzeb at Bahadurgad, the Mughal Emperor offered Sambhaji his life on three non-negotiable conditions:
1. Surrender all Maratha hill fortresses and treasures.
2. Disclose the names of Mughal nobles who secretly sympathized with Swarajya.
3. Renounce his ancestral faith and convert to Islam.

Sambhaji rejected every demand with fiery contempt. For over three agonizing weeks, the emperor subjected Sambhaji and Kavi Kalash to barbaric tortures—blinding with red-hot irons, plucking nails, and peeling flesh. Sambhaji uttered not a single syllable of submission. On **11 March 1689** (Gudhi Padwa), he was executed on the riverbanks of **Tulapur**.

His martyrdom electrified Maharashtra. Instead of crushing Swarajya, Sambhaji's sacrifice unified every Maratha warrior into a ferocious, decentralised people's war (*Swatantrya Sangram*) that ultimately bled the Mughal Empire to death.""",
            "\"You may tear the flesh from my bones, but you cannot tear the spirit of Swarajya from my soul.\""
        ),

        # HARAPPAN CIVILIZATION
        (
            "harappa", 1,
            "Discovery & The Bronze Age Urban Wonder",
            "From Rakhaldas Banerjee and Dayaram Sahni to the Indus-Saraswati Valley",
            """Until the 1920s, world historians believed Indian civilization originated with the Vedic period around 1500 BCE. This eurocentric paradigm was shattered in 1921–1922 when Indian archaeologists **Daya Ram Sahni** (at Harappa in Punjab) and **Rakhaldas Banerjee** (at Mohenjo-daro in Sindh), working under the director-generalship of Sir John Marshall, unearthed the relics of a monumental Bronze Age civilization dating back to 3300 BCE.

Spanning over 1.3 million square kilometers—larger than ancient Egypt and Mesopotamia combined—the Indus-Saraswati Civilization flourished along the fertile floodplains of the Indus and the ancient perennial **Ghaggar-Hakra (Saraswati)** river basin.

Over 1,500 sites have been identified, with major urban centers including Mohenjo-daro, Harappa, Rakhigarhi (the largest site, in Haryana), Dholavira, Kalibangan, and Lothal. Remarkably, this expansive realm exhibited a unified material culture, standardized brick dimensions, uniform script, and consistent weight systems without any evidence of standing royal armies or autocratic despots.""",
            "\"The discovery of Mohenjo-daro pushed back the known antiquity of Indian civilization by over two millennia in a single stroke.\""
        ),
        (
            "harappa", 2,
            "Masterclass Urbanism & Sanitary Engineering",
            "Grid Layouts, The Great Bath, and Subterranean Drainage",
            """The hallmark of Harappan genius was its uncompromising civil engineering:
- **Standardized Grid System**: Cities were divided into distinct sectors along strict cardinal directions (North-South and East-West). Streets intersected at crisp 90-degree right angles, engineered to catch prevailing winds and naturally sweep the avenues clean.
- **Standardized Burnt Bricks**: Buildings utilized kiln-baked bricks manufactured to a strict universal ratio of **4:2:1** (Length : Breadth : Thickness) across all regions from Gujarat to the Khyber Pass.
- **The World's First Subterranean Drainage**: Every residential home featured dedicated bathing rooms and terracotta drainpipes. Wastewater flowed through wall chutes into covered municipal sewer channels running beneath streets, complete with inspection manholes and sump pits for sediment removal.
- **The Great Bath of Mohenjo-daro**: A monumental civic pool measuring 12m × 7m × 2.4m, sealed with baked bricks, gypsum mortar, and a waterproof lining of natural bitumen (asphalt), representing mankind's earliest monumental public water engineering.""",
            "\"In no other ancient civilization—not Egypt, nor Babylon—did civil sanitation and individual hygiene receive such meticulous attention.\""
        ),
        (
            "harappa", 3,
            "Maritime Trade, Dockyards & Advanced Metallurgy",
            "Lothal's Tidal Basin, International Guilds, and Cubical Chert Weights",
            """Harappan society was an international commercial juggernaut. At **Lothal** in Gujarat, Harappan maritime engineers constructed the world's earliest known **tidal dockyard**—a 215-meter-long brick basin engineered with sluice gates to lock in high tides, enabling ocean-going vessels to berth and discharge cargo safely from the Gulf of Khambhat.

International trade routes connected Harappan merchants (referred to in Mesopotamian cuneiform tablets as *Meluhha*) to Dilmun (Bahrain), Makan (Oman), and Akkad. Harappan exports included carnelian beads, lapis lazuli, fine cotton textiles, ivory combs, and copper ingots.

To govern commerce, they devised a sophisticated binary-decimal weight system based on precision-cut cubical **chert stones**. Weights scaled in powers of 2 (1, 2, 4, 8, 16, 32...) up to 16, which equated to 13.7 grams, and decimal multiples thereafter. Their bronze metallurgy produced masterpieces of lost-wax casting (*cire perdue*), most famously the spirited **Bronze Dancing Girl of Mohenjo-daro**.""",
            "\"The dockyard of Lothal remains a staggering testimony to Bronze Age hydraulic knowledge and oceanic commerce.\""
        ),
        (
            "harappa", 4,
            "Seals, The Undeciphered Script & Decline",
            "Pashupati, The Unicorn Seal, Climatic Shifts, and Ecological Adaptation",
            """Over 3,500 carved **steatite seals** have been unearthed, featuring masterfully rendered animals: the one-horned unicorn, humped bulls, tigers, and elephants. Among the most iconic is the **Pashupati Seal**, depicting a horned deity seated in a yogic posture flanked by wild beasts, widely considered a proto-Shiva archetype.

The Harappan script, consisting of approximately 400 distinct glyphs written right-to-left, remains one of antiquity's greatest undeciphered puzzles. At **Dholavira**, archaeologists discovered a monumental ten-character stone signboard that once adorned the northern city gate.

By 1900 BCE, the mature urban phase entered decline. Modern paleoclimatology and satellite hydrology indicate that rather than violent invasions, the civilization transitioned due to **gradual climatic shifts**: shifting monsoons, tectonic disturbances, and the progressive drying up of the mighty Saraswati/Ghaggar-Hakra river system. The populace adapted by migrating eastward into the lush Gangetic plains, carrying their agricultural, spiritual, and urban wisdom into subsequent epochs.""",
            "\"The Harappans did not vanish into thin air; their architectural, spiritual, and craft traditions flowed into the perennial stream of Indian culture.\""
        ),

        # REVOLT OF 1857
        (
            "revolt1857", 1,
            "The Spark & The Smouldering Embers",
            "Doctrine of Lapse, Economic Exploitation, and the Enfield P-53 Cartridge",
            """By the early 1850s, the **British East India Company (EIC)** had transformed from an exploitative trading enterprise into an oppressive imperial regime. Millions of Indian weavers and artisans were pauperized by predatory tariff policies, and high-caste sepoys in the Bengal Army felt their religious customs systematically disregarded.

Lord Dalhousie's aggressive **Doctrine of Lapse** annexed historic Indian sovereign realms—including Satara, Sambalpur, Nagpur, and **Jhansi**—denying Hindu monarchs their legal customary right to pass their thrones to adopted heirs. In 1856, the opulent kingdom of **Awadh (Oudh)** was unceremoniously annexed under the pretext of 'misgovernance', enraging 75,000 sepoys whose families farmed those lands.

The immediate flashpoint arrived with the introduction of the new **Enfield P-53 rifled musket**. The paper cartridges for this rifle were sealed with animal grease rumored to combine cow fat (sacred to Hindus) and pig lard (forbidden to Muslims), which soldiers were forced to bite off with their teeth. On **29 March 1857** at Barrackpore, a young sepoy named **Mangal Pandey** of the 34th Bengal Native Infantry openly rebelled, firing upon his British officers and igniting a prairie fire of revolution.""",
            "\"Die we must one day; why not die striking a blow for the honour of our faith and land?\""
        ),
        (
            "revolt1857", 2,
            "The Uprising at Meerut & March on Delhi",
            "10 May 1857: The Sepoy Rising and the Restoration of Bahadur Shah Zafar",
            """On **10 May 1857**, eighty-five sepoys of the 3rd Light Cavalry at **Meerut** who had refused to touch the greased cartridges were publicly shackled in irons and sentenced to ten years of hard labor. That evening, fellow sepoys broke into open revolt. They attacked the military cantonment, broke open the prisons to liberate their comrades, and raised the cry: *"Chalo Dilli!"* (March to Delhi!).

Galloping through the night across the Yamuna River bridge of boats, the insurgent cavalry entered the historic Red Fort on the morning of 11 May. They surrounded the aged Mughal Emperor, **Bahadur Shah Zafar**, urging him to lend royal legitimacy to their holy war (*Jihad-e-Azadi*) against foreign conquerors.

Reluctantly at first, then wholeheartedly, the 82-year-old poet-monarch accepted the supreme leadership of the rebellion. Letters were dispatched in his imperial name to rulers across Rajasthan, Punjab, Central India, and Maharashtra, summoning them to unite under one banner to liberate the motherland.""",
            "\"As long as the impulse of faith remains in the heart of Hindustan, the sword of Hind shall shine in the court of London.\" — Bahadur Shah Zafar"
        ),
        (
            "revolt1857", 3,
            "Legends of the Battlefield: Jhansi, Awadh & Jagdishpur",
            "Rani Lakshmibai, Tatya Tope, Begum Hazrat Mahal, and Veer Kunwar Singh",
            """Across northern and central India, legendary commanders took up arms:
- **Rani Lakshmibai of Jhansi**: Refusing British annexation with the immortal battle cry *"Meri Jhansi nahi doongi!"* (I shall not surrender my Jhansi), the twenty-two-year-old queen led her troops in hand-to-hand combat against General Hugh Rose. When Jhansi fell after a heroic siege, she escaped at midnight with her adopted son tied to her back, joined forces with Tatya Tope to capture **Gwalior Fort**, and fought gallantly until martyred at Kotah-ki-Serai on 18 June 1858.
- **Tatya Tope & Nana Saheb**: Operating in Kanpur and the ravines of the Chambal, Tatya Tope conducted an iconic guerrilla campaign across thousands of miles, outmaneuvering British columns with rapid marches.
- **Begum Hazrat Mahal**: Seizing control of Lucknow, she crowned her minor son Birjis Qadr, unified Hindu and Muslim nobles, and defended the besieged British Residency for months.
- **Veer Kunwar Singh**: The 80-year-old chieftain of Jagdishpur in Bihar routed British forces at Arrah and Azamgarh. When a bullet wounded his left wrist while crossing the Ganga, he severed his own hand with his sword to prevent gangrene and offered it to the river.""",
            "\"She was the bravest, the best, and the only man among the rebels.\" — British General Sir Hugh Rose on Rani Lakshmibai"
        ),
        (
            "revolt1857", 4,
            "The Aftermath & Birth of Modern Indian Nationalism",
            "The Queen's Proclamation (1858) and the Shattering of Company Rule",
            """Despite colossal popular participation, the rebellion was brutally suppressed by mid-1858 due to superior British artillery, control of the electric telegraph, naval reinforcements, and lack of nationwide central coordination. Bahadur Shah Zafar was exiled to Rangoon, Burma; Rani Lakshmibai and Kunwar Singh fell on the battlefield; Tatya Tope was captured and hanged.

Yet, in defeat, the 1857 revolt achieved a monumental strategic transformation:
1. **Dissolution of the East India Company**: The British Parliament passed the **Government of India Act 1858**, stripping the Company of all administrative authority and transferring rule directly to the British Crown.
2. **Queen Victoria's Proclamation (1 November 1858)**: Pledged non-interference in Indian religious practices and formally abandoned the hated Doctrine of Lapse.
3. **Seed of National Consciousness**: The shared blood of Hindu and Muslim soldiers, peasants, and nobles fighting together laid the foundational bedrock for the modern Indian Freedom Movement led in the subsequent century by Bal Gangadhar Tilak, Subhas Chandra Bose, and Mahatma Gandhi.""",
            "\"The spark struck in 1857 was never extinguished; it smouldered beneath the ash until it consumed the British Empire in 1947.\""
        )
    ]
    cursor.executemany("INSERT INTO chapters (topic_id, chapter_number, title, subtitle, content, key_quote) VALUES (?,?,?,?,?,?)", chapters_data)

    # 3. SEED PEOPLE (5 per topic = 20 people)
    people_data = [
        # SHIVAJI
        (
            "shivaji", "Chhatrapati Shivaji Maharaj", "Founder & First Chhatrapati of Hindavi Swarajya", "1630 – 1680 CE",
            "Visionary military strategist, creator of the Maratha Navy, builder of hill and sea fort networks, and compassionate administrator who instituted the Ashta Pradhan cabinet.",
            "Pioneered Ganimi Kawa guerrilla tactics; liberated Maharashtra from Adilshahi and Mughal hegemony; constructed Sindhudurg and Vijaydurg naval forts; crowned at Raigad in 1674.",
            "Freedom is a boon, which everyone has the right to receive.", "⚔️", 1
        ),
        (
            "shivaji", "Jijabai Bhosale (Rajmata Jijau)", "Queen Mother, Mentor & Spiritual Guide", "1598 – 1674 CE",
            "Mother of Shivaji Maharaj and political architect of Swarajya. Taught Shivaji statecraft, justice, and devotion to native liberation.",
            "Administered the Pune jagir, restored temples, settled local agrarian disputes, and instilled unflinching courage in young Shivaji.",
            "Never bow your head before injustice; rule for the welfare of the people.", "👑", 2
        ),
        (
            "shivaji", "Tanaji Malusare", "Subedar & Hero of Sinhagad", "1600 – 1670 CE",
            "Legendary Maratha commander whose sheer audacity captured the impregnable fortress of Kondhana (Sinhagad) from the Mughals.",
            "Scaled the 300-meter sheer cliff of Kondhana using trained monitor lizards (*Ghorpad* Yashwanti); defeated Udaybhan Rathod before sacrificing his life.",
            "Aadhi lagin Kondhanache, mag majhya Raybache! (First the wedding of Kondhana fort, then my son Rayba's wedding!)", "🛡️", 3
        ),
        (
            "shivaji", "Baji Prabhu Deshpande", "Commander & Hero of Pavan Khind", "1615 – 1660 CE",
            "Fierce Sardar who held the narrow mountain pass of Ghodkhind with just 300 Mavala soldiers against 4,000 Adilshahi cavalry to secure Shivaji's escape.",
            "Fought relentlessly despite dozens of mortal wounds until the signal cannon fire from Vishalgad announced Shivaji's safe arrival.",
            "My life is fulfilled; the Chhatrapati is safe in the citadel.", "🗡️", 4
        ),
        (
            "shivaji", "Netaji Palkar", "First Sarnaubat (Commander-in-Chief)", "c. 1620 – 1680 CE",
            "Known as the 'Second Shivaji' by contemporaries due to his lightning-fast cavalry raids across the Deccan plateau.",
            "Led victorious cavalry sweeps against Mughal and Bijapuri outposts; captured and forcibly converted by Aurangzeb, he escaped back to Maharashtra and was re-inducted into Hinduism by Shivaji.",
            "Speed is our shield; the cavalry moves like the desert wind.", "🐎", 5
        ),

        # SAMBHAJI
        (
            "sambhaji", "Chhatrapati Sambhaji Maharaj", "Second Chhatrapati of Hindavi Swarajya", "1657 – 1689 CE",
            "Undefeated warrior king, master of Sanskrit and Brajbhasha literature, and fearless defender who thwarted Emperor Aurangzeb's armada for nine continuous years.",
            "Fought over 120 military battles without a single defeat; authored Budhabhushanam at age 14; humbled Portuguese colonial forces in Goa.",
            "Death on the battlefield is glorious, but surrender of Swarajya is unthinkable.", "🛡️", 1
        ),
        (
            "sambhaji", "Maharani Yesubai", "Queen Consort & Guardian of Swarajya", "c. 1660 – 1730 CE",
            "Wife of Sambhaji Maharaj and daughter of Pilaji Shirke. A woman of extraordinary fortitude who held the Maratha royal seal during critical sieges.",
            "Led the defense of Raigad Fort in 1689; survived 30 years in Mughal captivity while preserving the Maratha royal lineage and advising Chhatrapati Shahu.",
            "Swarajya will survive as long as there is courage in our veins.", "👑", 2
        ),
        (
            "sambhaji", "Hambirrao Mohite", "Sarnaubat (Supreme Commander)", "1630 – 1687 CE",
            "Maternal uncle of Sambhaji Maharaj and legendary commander-in-chief who crushed Mughal armies at Burhanpur and Wai.",
            "Decisively defeated Bahadur Khan and Prince Azam; martyred by a cannonball while winning the Battle of Wai in 1687.",
            "The Maratha army knows only to advance; retreat is not in our lexicon.", "⚔️", 3
        ),
        (
            "sambhaji", "Kavi Kalash", "Chhandogamatya & Devoted Companion", "c. 1640 – 1689 CE",
            "Eminent scholar, poet from Kannauj, and trusted minister who stood steadfast alongside Sambhaji Maharaj through triumphs and supreme martyrdom.",
            "Composed stirring Sanskrit and Braj poetry; managed diplomatic correspondence; rejected Mughal bribes and endured torture alongside his king.",
            "When the king stands tall as Mount Meru, what threat can imperial dust pose?", "📜", 4
        ),
        (
            "sambhaji", "Santaji Ghorpade", "General & Master of Lightning Guerrilla Warfare", "1660 – 1696 CE",
            "Trained under Sambhaji Maharaj; became one of the two legendary generals (with Dhanaji Jadhav) who struck terror in the Mughal camp after Sambhaji's martyrdom.",
            "Raided Aurangzeb's royal tent at Tulapur; cut the imperial tent ropes and inflicted massive panic across imperial cantonments.",
            "Even Mughal horses shivered and saw Santaji's reflection when drinking water.", "⚡", 5
        ),

        # HARAPPA
        (
            "harappa", "Daya Ram Sahni", "Pioneering Indian Archaeologist", "1879 – 1948 CE",
            "The first Indian Director-General of the Archaeological Survey of India (ASI) who commenced excavations at Harappa in Punjab in 1920–1921.",
            "Discovered the monumental brick structures, citadel mounds, and steatite seals of Harappa, proving Indian urban civilization predated Alexander by millennia.",
            "These brick walls reveal an empire of peace and order unknown to the ancient world.", "🔍", 1
        ),
        (
            "harappa", "Rakhaldas Banerjee", "Discoverer of Mohenjo-daro", "1885 – 1930 CE",
            "Brilliant historian and ASI archaeologist who discovered Mohenjo-daro ('Mound of the Dead') in Sindh in 1922 while investigating a Buddhist stupa.",
            "Identified ancient chert flint scrapers and prehistoric seals beneath Buddhist strata, establishing the Bronze Age antiquity of the site.",
            "Beneath the Kushan stupa lies an older, grander civilization of incredible sophistication.", "🏺", 2
        ),
        (
            "harappa", "Sir John Marshall", "Director-General of ASI (1902–1928)", "1876 – 1958 CE",
            "Oversaw the official announcement to the world in the Illustrated London News (1924) of the discovery of the Indus Valley Civilization.",
            "Coined the term 'Indus Civilization' and supervised major excavation publications on Mohenjo-daro and Harappa.",
            "One step back into the past has opened a vast new horizon of human achievement.", "🏛️", 3
        ),
        (
            "harappa", "S. R. Rao", "Discoverer of Lothal Dockyard", "1922 – 2013 CE",
            "Renowned marine archaeologist who excavated the coastal port city of Lothal in Gujarat between 1954 and 1962.",
            "Discovered the world's earliest known tidal dockyard, micro-bead factory, and seals connecting Lothal with the Persian Gulf.",
            "Lothal was the ancient world's gateway to international maritime enterprise.", "⚓", 4
        ),
        (
            "harappa", "R. S. Bisht", "Excavator of Dholavira", "1944 – Present",
            "Joint Director-General of ASI who directed the landmark multi-year excavations at Dholavira in the Rann of Kutch from 1990 onwards.",
            "Unearthed the unique tri-partite city design, mammoth rock-cut rainwater harvesting reservoirs, and the famous ten-character signboard.",
            "Dholavira's hydraulic engineering is an unparalleled testament to sustainable desert urbanism.", "💧", 5
        ),

        # REVOLT OF 1857
        (
            "revolt1857", "Rani Lakshmibai of Jhansi", "Queen & Warrior Martyr", "1828 – 1858 CE",
            "The iconic Queen of Jhansi (born Manikarnika Tambe) who defied Lord Dalhousie's Doctrine of Lapse and led the armed struggle across Central India.",
            "Heroically defended Jhansi against General Hugh Rose; captured Gwalior Fort; fell fighting in battlefield armor at Kotah-ki-Serai.",
            "Meri Jhansi nahi doongi! (I shall never give up my Jhansi!)", "⚔️", 1
        ),
        (
            "revolt1857", "Mangal Pandey", "Sepoy of the 34th Bengal Native Infantry", "1827 – 1857 CE",
            "The revolutionary soldier whose courageous revolt at Barrackpore on 29 March 1857 sparked the nationwide uprising against the greased cartridges.",
            "Openly defied British officers, calling on his comrades to protect their religious faith and motherland; executed on 8 April 1857.",
            "Come out, brothers! When you strike for freedom, God is on your side.", "🔥", 2
        ),
        (
            "revolt1857", "Tatya Tope (Ramachandra Pandurang)", "Guerrilla General & Strategist", "1814 – 1859 CE",
            "Master of mobile warfare who commanded forces in Kanpur, Kalpi, and Gwalior, baffling the British army with over a year of guerrilla skirmishes.",
            "Evaded thousands of British troops across Central India, Bundelkhand, and Rajasthan; betrayed by Man Singh and martyred at Shivpuri.",
            "I have performed my duty to my Peshwa and to my motherland. I fear no gallows.", "🐎", 3
        ),
        (
            "revolt1857", "Begum Hazrat Mahal", "Queen Mother & Leader of Awadh", "1820 – 1879 CE",
            "First wife of Nawab Wajid Ali Shah who seized leadership after Awadh's annexation, organized the defense of Lucknow, and crowned her son Birjis Qadr.",
            "Mobilized both Hindu and Muslim taluqdars; defended the Residency of Lucknow; refused British amnesty and lived in honorable exile in Nepal.",
            "Our country is our pride; no foreign power has the right to rule over our hearths.", "👑", 4
        ),
        (
            "revolt1857", "Veer Kunwar Singh", "Chieftain of Jagdishpur", "1777 – 1858 CE",
            "Eighty-year-old warrior king of Bihar who led the revolt across Bhojpur, Arrah, and Azamgarh, routing British battalions with brilliant tactics.",
            "Liberated Arrah; cut off his own bullet-shattered hand to prevent poison from spreading; defeated Captain Le Grand's forces shortly before passing away undefeated.",
            "An 80-year-old lion who taught the British that Indian valour knows no age.", "🦁", 5
        )
    ]
    cursor.executemany("INSERT INTO people (topic_id, name, role_title, lifespan, bio, achievements, quote, avatar_icon, display_order) VALUES (?,?,?,?,?,?,?,?,?)", people_data)

    # 4. SEED PLACES (4 per topic = 16 places)
    places_data = [
        # SHIVAJI
        (
            "shivaji", "Raigad Fort", "Mahad, Raigad District, Maharashtra",
            "The sovereign capital of Hindavi Swarajya and venue of Shivaji's historic coronation (1674).",
            "High-altitude Sahyadri hill fort; natural cliff fortification with specialized bastion architecture.",
            "Perched 820 meters above sea level, Raigad was chosen by Shivaji as his capital for its strategic impregnability. It featured an ornate council hall (Darbar), royal mint, massive grain granaries, queens' chambers, and the iconic *Hirakani Buruj* (bastion).",
            "Coronation Throne (Simhasana) site, Hirakani Bastion, Maha Darwaja, Ganga Sagar Lake.", 1
        ),
        (
            "shivaji", "Pratapgad Fort", "Mahabaleshwar, Satara District, Maharashtra",
            "Site of the decisive 1659 battle where Shivaji defeated Adilshahi commander Afzal Khan.",
            "Dual-citadel hill fort (Balekilla and Machi) constructed by Moropant Pingle.",
            "Strategically positioned above the dense Jawali forests to guard the pass to the Konkan coast. Its lower machi hosted the fateful tent meeting between Shivaji and Afzal Khan.",
            "Bhavani Mata Temple, Afzal Khan's Tomb, double-curved bastions, panoramic views of the Western Ghats.", 2
        ),
        (
            "shivaji", "Sindhudurg Fort", "Malvan, Arabian Sea Coast, Maharashtra",
            "Pinnacle of medieval Maratha naval architecture built on Kurte island.",
            "Island sea fort constructed with molten lead foundation and 42 massive bastions.",
            "Commissioned by Shivaji in 1664 to counter Portuguese, British, and Siddi sea marauders. Over 70,000 kilograms of molten lead were poured into undersea bedrock to anchor its 3-kilometer outer ramparts against fierce oceanic waves.",
            "Hidden main entrance (Dilli Darwaja), Shivaji Maharaj Temple, hand and footprint impressions in lime mortar.", 3
        ),
        (
            "shivaji", "Panhala Fort", "Kolhapur District, Maharashtra",
            "Historic fort from which Shivaji executed his legendary rainy night breakout in 1660.",
            "Triangular plateau hill fort with Bijapuri and Maratha architectural layers.",
            "Panhala was besieged by Siddi Jauhar's massive army for five months before Shivaji slipped through the encirclement under cover of storm toward Vishalgad, guarded by Baji Prabhu Deshpande.",
            "Andhar Bavadi (hidden well structure), Amberkhana (massive granary), Sajja Kothi (palace pavilion).", 4
        ),

        # SAMBHAJI
        (
            "sambhaji", "Tulapur", "Pune District, Maharashtra (Confluence of Bhima and Indrayani)",
            "Sacred site of Sambhaji Maharaj's supreme martyrdom in 1689.",
            "Riverbank pilgrimage shrine (Triveni Sangam style) and memorial samadhi.",
            "Located at the holy confluence of the Bhima and Indrayani rivers, Tulapur is where Chhatrapati Sambhaji Maharaj and Kavi Kalash faced their final moments with unflinching dignity after refusing Aurangzeb's ultimatum.",
            "Chhatrapati Sambhaji Maharaj Samadhi, Kavi Kalash memorial, river ghats.", 1
        ),
        (
            "sambhaji", "Burhanpur", "Khandesh, Madhya Pradesh",
            "Wealthy Mughal trading metropolis stormed and raided by Sambhaji in 1681.",
            "Mughal imperial provincial capital and gateway to South India.",
            "In January 1681, Sambhaji and Hambirrao Mohite launched a lightning cavalry raid over 200 miles into Mughal territory, capturing immense treasures from Burhanpur's imperial depots to finance Swarajya's defense.",
            "Shahi Qila remnants, Tapti riverbank fortifications, Jama Masjid.", 2
        ),
        (
            "sambhaji", "Santo Estevão (St. Stephen's Island)", "Ilhas de Goa, Mandovi River, Goa",
            "Site of Sambhaji's daring amphibious assault that brought Portuguese Goa to its knees (1683).",
            "Portuguese riverine island fort guarding the approaches to Old Goa.",
            "Sambhaji personally led Maratha troops wading through the Mandovi river at low tide, capturing the fort and routing the Portuguese Viceroy's counter-attack.",
            "St. Francis Xavier church historic connection, river defense walls, fort ruins.", 3
        ),
        (
            "sambhaji", "Vishalgad", "Kolhapur District, Maharashtra",
            "Formidable mountain bastion where Sambhaji organized council meetings and military rallies.",
            "High-altitude crag fortress situated at the edge of the Konkan cliff.",
            "Vishalgad served as an unbreachable retreat and rally point during Aurangzeb's invasion, housing regional garrisons and treasury reserves.",
            "Amruteshwar Temple, Bhupalgarh access route, steep cliff edges.", 4
        ),

        # HARAPPA
        (
            "harappa", "Mohenjo-daro", "Larkana District, Sindh (Indus River Basin)",
            "The largest urban metropolis of the Bronze Age, renowned for the Great Bath and covered drainage.",
            "Planned brick city on artificial mounds with distinct Citadel and Lower City.",
            "Flourishing around 2500 BCE, Mohenjo-daro housed an estimated 40,000 citizens. It featured multi-story brick homes, private wells, and paved bathrooms connected to street drainage.",
            "The Great Bath, Great Granary / Warehouse, Priest-King bust findspot, Dancing Girl bronzework.", 1
        ),
        (
            "harappa", "Lothal", "Sargwala, Ahmedabad District, Gujarat (Bhogavo River / Gulf of Khambhat)",
            "The world's earliest known tidal dockyard and premier Bronze Age maritime port.",
            "Tidal hydraulic engineering, rectangular burnt-brick basin, acropolis, and bead factory.",
            "Lothal's 215m × 37m dockyard allowed deep-draft trading ships to enter through an inlet channel during high tide, protected from siltation by an automated sluice gate.",
            "Tidal dockyard basin, carnelian bead kiln, Persian Gulf style button seal, double burial site.", 2
        ),
        (
            "harappa", "Dholavira", "Khadir Bet, Great Rann of Kutch, Gujarat",
            "UNESCO World Heritage city celebrated for stone fortifications and massive rainwater reservoirs.",
            "Tri-partite urban plan (Citadel, Middle Town, Lower Town) built using dressed stone.",
            "Dholavira excelled in desert water conservation. Engineers constructed 16 stone reservoirs to capture seasonal monsoon run-off from the Manhar and Mansar torrents, storing over 250,000 cubic meters of water.",
            "Rock-cut water reservoirs, ceremonial stadium, 10-glyph monumental signboard.", 3
        ),
        (
            "harappa", "Kalibangan", "Hanumangarh District, Rajasthan (Ghaggar River)",
            "Site of the world's earliest discovered ploughed agricultural field and ritual fire altars.",
            "Fortified twin mounds with mud-brick construction and fire pits.",
            "Excavations revealed furrow patterns in grid format identical to modern mustard and chickpea cultivation in Rajasthan, proving advanced prehistoric farming.",
            "Ploughed field furrow marks, row of 7 fire altars, terracotta bangles (Kali-bangan means black bangles).", 4
        ),

        # REVOLT OF 1857
        (
            "revolt1857", "Jhansi Fort", "Jhansi, Bundelkhand, Uttar Pradesh",
            "Citadel of Rani Lakshmibai where she mounted her epic defense against British forces.",
            "Hilltop granite fort with twenty-two massive bastions on Bangira hill.",
            "Constructed originally by Raja Bir Singh Deo, the fort stood two weeks of ceaseless bombardment by General Hugh Rose's artillery before the Rani executed her midnight equestrian escape.",
            "Kadak Bijli cannon, Shiva Temple inside the fort, horse jump spot (Ghodakood).", 1
        ),
        (
            "revolt1857", "The Red Fort (Lal Qila)", "Old Delhi, Yamuna Riverbank",
            "Epicenter of the rebellion where sepoys declared Bahadur Shah Zafar Emperor of India.",
            "Mughal red sandstone palace-fortress designed by Ustad Ahmad Lahori.",
            "On 11 May 1857, mutineers entered through the Rajghat gate and assembled in the Diwan-i-Khas, transforming a cantonment sepoy mutiny into a nationwide war of independence.",
            "Diwan-i-Aam, Diwan-i-Khas, Lahore Gate, Salimgarh bridge.", 2
        ),
        (
            "revolt1857", "The British Residency", "Lucknow, Uttar Pradesh",
            "Site of the six-month siege of Lucknow led by Begum Hazrat Mahal and rebel sepoys.",
            "Colonial compound of European bungalows, banquet halls, and defensive bastions.",
            "Besieged from July to November 1857, the bullet-pocked brick ruins remain preserved today in their exact state of destruction as a historical memorial.",
            "Ruined banqueting hall, Bailey Guard Gate, subterranean cellars (Tykhana).", 3
        ),
        (
            "revolt1857", "Meerut Cantonment", "Meerut, Uttar Pradesh",
            "The spark site where the 1857 uprising officially erupted on 10 May 1857.",
            "British colonial military cantonment with cavalry lines and ammunition magazines.",
            "Following the court martial of 85 Indian cavalry troopers, sepoys broke into open revolt on a Sunday evening, liberating prisoners and marching on Delhi.",
            "Parade ground memorial, Kali Paltan temple (where sepoys secretly conferred), Sadar Bazaar.", 4
        )
    ]
    cursor.executemany("INSERT INTO places (topic_id, name, location, significance, architecture_style, description, key_features, display_order) VALUES (?,?,?,?,?,?,?,?)", places_data)

    # 5. SEED FACTS (6 per topic = 24 facts)
    facts_data = [
        # SHIVAJI
        ("shivaji", "First to Establish a Formal Navy in Medieval India", "While most Indian land rulers ignored the oceans, Shivaji built a 400-ship fleet (*Gurabs*, *Galbats*) and constructed marine forts like Sindhudurg and Vijaydurg, earning him the title 'Father of the Indian Navy'.", "Military Genius"),
        ("shivaji", "Strict Moral Code on Battlefield Conduct", "Shivaji strictly outlawed mistreatment of women, prisoners of war, and religious buildings. When his subedar captured the daughter-in-law of the Muslim governor of Kalyan, Shivaji respectfully sent her home with gifts and reprimanded the officer.", "Ethics & Statecraft"),
        ("shivaji", "The Mathematical Genius of Fort Walls", "The curved bastions of Shivaji's forts were engineered at precise angles so that cannonballs would ricochet off rather than crack the stone, leaving zero dead-angles for approaching enemy troops.", "Architecture"),
        ("shivaji", "Abolition of the Watandari Exploitation System", "Shivaji dismantled the oppressive hereditary tax-collection system, replacing it with direct state payments to officials. Farmers paid taxes directly to the government only in proportion to their harvest.", "Agrarian Reform"),
        ("shivaji", "The Sacred Gold-Standard Coin: The Hon", "Shivaji issued his own gold coins called *Shivrai Hon* and copper *Shivrai* following his coronation, signaling complete sovereign independence from the Mughal currency sphere.", "Economy"),
        ("shivaji", "Ganimi Kawa: The Philosophy of Lightning Warfare", "Guerrilla tactics relied on three pillars: exhaustive knowledge of topography, speed exceeding 40 miles a day on mountain ponies, and tactical disengagement when facing unfavorable numbers.", "Tactics"),

        # SAMBHAJI
        ("sambhaji", "120 Battles Fought, Zero Defeats", "Military historians note that throughout his 9-year reign as Chhatrapati, Sambhaji fought over 120 military engagements against Mughals, Siddis, and Portuguese without losing a single battle.", "Military Invictus"),
        ("sambhaji", "A Sanskrit Treatise on Statecraft at Age 14", "At only 14 years old, Sambhaji authored *Budhabhushanam*, an elaborate Sanskrit text advising kings on military tactics, treasury management, espionage networks, and personal ethics.", "Literature"),
        ("sambhaji", "The 2-Kilometer Sea Causeway at Janjira", "To capture the pirate stronghold of Janjira island, Sambhaji ordered his engineers to construct a 2-kilometer rock-and-timber bridge straight into the sea, terrifying the Siddi defenders.", "Engineering"),
        ("sambhaji", "Polyglot Fluency in Six Languages", "Sambhaji was fluent in Sanskrit, Marathi, Brajbhasha, Persian, Hindi, and Kannada, enabling him to correspond directly with foreign ambassadors, regional rulers, and scholars.", "Scholarship"),
        ("sambhaji", "Trapping Half a Million Mughal Troops in the Deccan", "Sambhaji's relentless hit-and-run strategy kept Emperor Aurangzeb's grand army bogged down in the Deccan plateau for nearly a decade, bleeding the imperial treasury of Delhi dry.", "Grand Strategy"),
        ("sambhaji", "Supreme Martyrdom that Ignited a Decentralized War", "Aurangzeb assumed Sambhaji's execution would dismantle the Maratha state. Instead, it unified peasants and nobles into a ferocious, decentralized war that ultimately broke the Mughal Empire.", "Legacy"),

        # HARAPPA
        ("harappa", "World's First Standardized Burnt-Brick Ratio", "Across hundreds of miles, every Harappan kiln produced bricks in the strict ratio of 4:2:1 (length : breadth : height), a proportion modern civil engineers still consider optimal for structural stability.", "Civil Engineering"),
        ("harappa", "Covered Subterranean Drainage 4,500 Years Ago", "While cities in Europe threw sewage onto unpaved streets as late as the 18th century, Harappan homes in 2500 BCE had private latrines connected to underground covered sewers with inspection manholes.", "Sanitation"),
        ("harappa", "The Tidal Sluice Gates of Lothal Dockyard", "Lothal's dockyard engineers calculated ocean tides with staggering precision. They installed wooden sluice gates that opened automatically with high tide and locked in seawater as the tide receded.", "Hydraulics"),
        ("harappa", "Complete Absence of Royal Monuments or War Weaponry", "Unlike Egypt and Mesopotamia with their towering royal pyramids and depictions of slaughtered captives, Harappan sites contain no palaces, royal tombs, or large offensive armories, suggesting a remarkably egalitarian, merchant-led society.", "Society"),
        ("harappa", "Precision Cubical Weights Based on Powers of 2", "Harappans used chert cube weights scaling in binary (1, 2, 4, 8, 16, 32...) up to 16, which weighed 13.7 grams, before transitioning into a base-10 decimal system for heavier trade goods.", "Mathematics"),
        ("harappa", "Dholavira's 16 Rock-Cut Rainwater Reservoirs", "In the arid Rann of Kutch, Dholavira's engineers built 16 interconnected stepped stone reservoirs capable of holding 250,000 cubic meters of freshwater, enough to sustain the city through years of drought.", "Water Conservation"),

        # REVOLT OF 1857
        ("revolt1857", "Rani Lakshmibai's Elite Women's Fighting Brigade", "Rani Lakshmibai formed and trained a dedicated women's regiment in Jhansi called the *Durga Dal*, led by her close companion Jhalkaribai, who famously fought disguised as the Queen to allow the Rani to escape.", "Courage"),
        ("revolt1857", "The Mystery of the Chapatis", "In early 1857, mysterious unleavened bread cakes (*chapatis*) and red lotus flowers were secretly passed from village to village across northern India, serving as an untraceable psychological warning of impending revolution.", "Espionage"),
        ("revolt1857", "An 80-Year-Old Chieftain Who Amputated His Own Arm", "When Veer Kunwar Singh was struck in the wrist by a British musket ball while crossing the Ganga, he took his sword, severed his own arm to stop the poison, and offered it to the sacred river before defeating his pursuers.", "Valour"),
        ("revolt1857", "The Greased Cartridges Were Offensive to Both Major Faiths", "The Enfield P-53 grease contained beef tallow (sacred to Hindus) and pork lard (forbidden to Muslims), uniting Hindu and Muslim soldiers against a shared imperial insult.", "Catalyst"),
        ("revolt1857", "The End of East India Company Rule", "The revolt ended 250 years of commercial and administrative monopoly by the British East India Company. Parliament dissolved the company and placed India under the direct sovereignty of the British Crown.", "Geopolitics"),
        ("revolt1857", "Bahadur Shah Zafar: The Last Mughal Poet Emperor", "Exiled to Rangoon after the revolt, the 82-year-old emperor wrote heartbreaking Urdu poetry about his beloved homeland: *'How unfortunate is Zafar, for his burial he could not even get two yards of land in his beloved country.'*", "Poignancy")
    ]
    cursor.executemany("INSERT INTO facts (topic_id, headline, detail, category) VALUES (?,?,?,?)", facts_data)

    # 6. SEED TIMELINE EVENTS (10 per topic = 40 events)
    timeline_data = [
        # SHIVAJI
        ("shivaji", "19 Feb 1630", 1630, "Birth of Shivaji Maharaj", "Shivneri Fort, Junnar", "Born to Shahaji Bhosale and Jijabai atop the high-walled Shivneri Fort.", "Critical"),
        ("shivaji", "1645", 1645, "The Sacred Oath of Swarajya", "Raireshwar Temple", "15-year-old Shivaji and his Mavala comrades swear to establish Hindavi Swarajya.", "Critical"),
        ("shivaji", "1646", 1646, "Capture of Torna Fort", "Torna (Prachandgad)", "First major fortress captured from Bijapur; buried treasure unearthed is used to build Rajgad.", "Major"),
        ("shivaji", "10 Nov 1659", 1659, "The Battle of Pratapgad", "Pratapgad Foothills", "Shivaji slays the deceitful Adilshahi general Afzal Khan and routs his invading army.", "Critical"),
        ("shivaji", "13 Jul 1660", 1660, "The Defense of Pavan Khind", "Ghodkhind (Pavan Khind)", "Baji Prabhu Deshpande and 300 warriors hold the pass to secure Shivaji's escape to Vishalgad.", "Critical"),
        ("shivaji", "5 Apr 1663", 1663, "Midnight Commando Raid on Lal Mahal", "Pune", "Shivaji infiltrates Shaista Khan's heavily guarded palace quarters, severing his fingers.", "Major"),
        ("shivaji", "6 Jan 1664", 1664, "Sack of Surat", "Surat, Gujarat", "Marathas raid the Mughal Empire's premier financial port, acquiring funds to finance sea defenses.", "Major"),
        ("shivaji", "1664 – 1667", 1665, "Construction of Sindhudurg Sea Fort", "Malvan Coast", "Shivaji commissions the impregnable island citadel, anchoring the foundations of the Maratha Navy.", "Major"),
        ("shivaji", "17 Aug 1666", 1666, "The Daring Escape from Agra", "Agra, Uttar Pradesh", "Shivaji and prince Sambhaji escape from Aurangzeb's house arrest concealed in sweet baskets.", "Critical"),
        ("shivaji", "6 Jun 1674", 1674, "Coronation (Rajyabhisheka)", "Raigad Fort", "Shivaji is formally crowned Chhatrapati of an independent sovereign Maratha Empire.", "Critical"),
        ("shivaji", "3 Apr 1680", 1680, "Passing of Shivaji Maharaj", "Raigad Fort", "The founder of Hindavi Swarajya passes away at age 50, leaving behind an enduring sovereign realm.", "Critical"),

        # SAMBHAJI
        ("sambhaji", "14 May 1657", 1657, "Birth of Sambhaji Maharaj", "Purandar Fort", "Born to Shivaji Maharaj and Maharani Saibai; raised under the tutelage of Rajmata Jijau.", "Major"),
        ("sambhaji", "1666", 1666, "The Agra Embassy at Age Nine", "Agra", "Accompanies Shivaji to the Mughal court; receives the titular rank of 5,000 Mansabdar.", "Major"),
        ("sambhaji", "1671", 1671, "Composition of Budhabhushanam", "Shringarpur", "At age fourteen, prince Sambhaji pens his masterwork in Sanskrit on statecraft and military ethics.", "Major"),
        ("sambhaji", "16 Jan 1681", 1681, "Coronation as Second Chhatrapati", "Raigad Fort", "Ascends the golden throne of Raigad, uniting Maratha sardars amidst looming Mughal threats.", "Critical"),
        ("sambhaji", "30 Jan 1681", 1681, "Lightning Raid on Burhanpur", "Burhanpur, Khandesh", "Sambhaji leads a 20,000-strong cavalry raid, capturing immense Mughal treasury supplies.", "Major"),
        ("sambhaji", "1682", 1682, "The Siege of Janjira & Causeway Construction", "Janjira Island", "Orders the construction of a 2-kilometer stone bridge into the ocean to assault Siddi defenses.", "Major"),
        ("sambhaji", "Nov – Dec 1683", 1683, "The Goa Campaign Against Portuguese", "Old Goa / St. Estevão", "Counter-attacks the Portuguese Viceroy, storming Chapora and pushing colonial Goa to near surrender.", "Critical"),
        ("sambhaji", "1687", 1687, "Battle of Wai & Loss of Hambirrao", "Wai, Satara", "Marathas defeat the Mughal army of Sarja Khan, but Commander-in-Chief Hambirrao Mohite is martyred.", "Major"),
        ("sambhaji", "Feb 1689", 1689, "Ambush at Sangameshwar", "Sangameshwar, Ratnagiri", "Sambhaji and Kavi Kalash are captured in an ambush following a traitorous intelligence leak.", "Critical"),
        ("sambhaji", "11 Mar 1689", 1689, "Supreme Martyrdom at Tulapur", "Tulapur (Bhima Riverbank)", "Defiantly refuses Aurangzeb's demands; martyred as Dharmaveer, sparking the people's war of Swarajya.", "Critical"),

        # HARAPPA
        ("harappa", "c. 3300 BCE", -3300, "Early Harappan (Ravi / Hakra Phase)", "Indus Basin", "Beginning of sedentary agro-pastoral communities, early copper metallurgy, and pottery motifs.", "Major"),
        ("harappa", "c. 2600 BCE", -2600, "Dawn of the Mature Urban Phase", "Mohenjo-daro & Harappa", "Monumental grid urban planning begins; standardized kiln-baked brick construction emerges.", "Critical"),
        ("harappa", "c. 2500 BCE", -2500, "Construction of the Great Bath", "Mohenjo-daro", "Public hydraulic engineering marvel sealed with natural bitumen is constructed in the citadel.", "Major"),
        ("harappa", "c. 2400 BCE", -2400, "Establishment of Lothal Tidal Dockyard", "Lothal, Gujarat", "Engineers build the world's earliest known tidal lock basin for oceanic maritime trade.", "Critical"),
        ("harappa", "c. 2350 BCE", -2350, "Direct Trade with Mesopotamia (Meluhha)", "Ur & Akkad", "Harappan seals, carnelian beads, and ivory items documented in Akkadian cuneiform inscriptions.", "Major"),
        ("harappa", "c. 2200 BCE", -2200, "Dholavira's Giant Water Reservoirs", "Khadir Bet, Kutch", "Stone-cut reservoir complexes and monumental city gateway signage installed.", "Major"),
        ("harappa", "c. 1900 BCE", -1900, "Decline of the Mature Urban Phase", "Indus-Saraswati Basin", "Gradual drying of the Saraswati river system and monsoon shift trigger eastward migration.", "Critical"),
        ("harappa", "1921 CE", 1921, "Excavation of Harappa by Daya Ram Sahni", "Montgomery District, Punjab", "ASI unearths Harappan citadel mounds, demonstrating Bronze Age urbanism in India.", "Critical"),
        ("harappa", "1922 CE", 1922, "Discovery of Mohenjo-daro by R. D. Banerjee", "Larkana, Sindh", "Discovery of the Great Bath and steatite seals pushes back Indian history by 2,000 years.", "Critical"),
        ("harappa", "1954 CE", 1954, "Discovery of Lothal Port by S. R. Rao", "Ahmedabad District, Gujarat", "Unearthing of maritime dockyard reveals the ocean-going heritage of ancient India.", "Major"),

        # REVOLT OF 1857
        ("revolt1857", "1848 – 1856", 1848, "Dalhousie's Doctrine of Lapse", "Across India", "Annexations of Satara (1848), Jhansi (1853), Nagpur (1854), and Awadh (1856) sow widespread anger.", "Major"),
        ("revolt1857", "Jan 1857", 1857, "Greased Cartridge Rumours Spread", "Dum Dum / Barrackpore", "Sepoys learn the Enfield P-53 cartridges are sealed with cow and pig grease.", "Major"),
        ("revolt1857", "29 Mar 1857", 1857, "Mangal Pandey's Defiance at Barrackpore", "Barrackpore, Bengal", "Mangal Pandey shoots his British adjutant, refusing to bear the greased ammunition.", "Critical"),
        ("revolt1857", "10 May 1857", 1857, "The Outbreak at Meerut", "Meerut Cantonment", "Sepoys liberate 85 imprisoned cavalry troopers and march overnight on Delhi shouting 'Chalo Dilli'.", "Critical"),
        ("revolt1857", "11 May 1857", 1857, "Bahadur Shah Zafar Declared Emperor", "Red Fort, Delhi", "Insurgents declare the Mughal poet-king the supreme symbolic leader of the rebellion.", "Critical"),
        ("revolt1857", "Jun 1857", 1857, "Rani Lakshmibai Takes Command of Jhansi", "Jhansi, Bundelkhand", "Rani Lakshmibai assumes sovereign administration of Jhansi following the sepoy rising.", "Critical"),
        ("revolt1857", "Jul 1857", 1857, "Siege of Lucknow Residency Begins", "Lucknow, Awadh", "Begum Hazrat Mahal and rebel sepoys trap the British garrison inside the Residency.", "Major"),
        ("revolt1857", "Apr 1858", 1858, "Kunwar Singh's Victory at Arrah & Martyrdom", "Jagdishpur, Bihar", "80-year-old Kunwar Singh routs British forces across the Ganga before passing away.", "Major"),
        ("revolt1857", "18 Jun 1858", 1858, "Martyrdom of Rani Lakshmibai", "Kotah-ki-Serai, Gwalior", "The Queen of Jhansi falls heroically in battle outside Gwalior Fort fighting General Rose's cavalry.", "Critical"),
        ("revolt1857", "1 Nov 1858", 1858, "Queen Victoria's Proclamation", "Allahabad", "British East India Company dissolved; India placed under direct British Crown governance.", "Critical")
    ]
    cursor.executemany("INSERT INTO timeline_events (topic_id, year_display, sort_year, title, location, description, importance) VALUES (?,?,?,?,?,?,?)", timeline_data)

    # 7. SEED QUIZ QUESTIONS (16 per topic = 64 total, allowing full 15-question quiz for ANY topic)
    quiz_data = [
        # SHIVAJI (16 questions)
        (
            "shivaji",
            "At which temple did a 15-year-old Shivaji take the sacred oath of Hindavi Swarajya in 1645?",
            "Trimbakeshwar Temple", "Raireshwar Temple", "Bhimashankar Temple", "Grishneshwar Temple",
            "B",
            "Shivaji and his young Mavala companions swore their pledge to establish Hindavi Swarajya at the Raireshwar temple in 1645.",
            "Easy"
        ),
        (
            "shivaji",
            "Which was the very first fortress captured by Shivaji Maharaj in 1646?",
            "Raigad", "Torna (Prachandgad)", "Sinhagad", "Pratapgad",
            "B",
            "Shivaji captured Torna Fort at age 16. The treasure discovered during its repair was used to build the fortress of Rajgad.",
            "Easy"
        ),
        (
            "shivaji",
            "Which Adilshahi general attempted to assassinate Shivaji during a truce meeting at Pratapgad in 1659?",
            "Shaista Khan", "Afzal Khan", "Siddi Jauhar", "Rustam Zaman",
            "B",
            "Afzal Khan of Bijapur met Shivaji at the base of Pratapgad in 1659 and attempted to strangle him, but was outmaneuvered and slain.",
            "Easy"
        ),
        (
            "shivaji",
            "What concealed weapon did Shivaji Maharaj use to defend himself against Afzal Khan?",
            "Katar and Talwar", "Wagh Nakh (Tiger Claws) and Bichawa", "Dandpatta and Shield", "Chakram",
            "B",
            "Shivaji concealed steel Wagh Nakh (tiger claws) and a Bichawa dagger in his sleeves, wearing iron chainmail beneath his tunic.",
            "Medium"
        ),
        (
            "shivaji",
            "Who heroically held the mountain pass of Ghodkhind (Pavan Khind) with 300 warriors to secure Shivaji's escape?",
            "Tanaji Malusare", "Baji Prabhu Deshpande", "Hambirrao Mohite", "Murarbaji Deshpande",
            "B",
            "Baji Prabhu Deshpande fought with two swords until signal cannons from Vishalgad announced Shivaji had reached safety.",
            "Easy"
        ),
        (
            "shivaji",
            "Which Mughal commander's fingers were severed by Shivaji in a daring night raid inside Lal Mahal in 1663?",
            "Mirza Raja Jai Singh", "Shaista Khan", "Dilir Khan", "Muazzam",
            "B",
            "Shivaji led 400 commando warriors into Lal Mahal in Pune, severing Shaista Khan's fingers as the viceroy jumped out of a window.",
            "Medium"
        ),
        (
            "shivaji",
            "Which famous island fortress was commissioned by Shivaji with molten lead foundations to establish maritime power?",
            "Janjira", "Sindhudurg", "Murud", "Elephanta",
            "B",
            "Sindhudurg was built in 1664 off the coast of Malvan using over 70,000 kg of molten lead poured into the coral reef bedrock.",
            "Medium"
        ),
        (
            "shivaji",
            "On which historic date did Shivaji Maharaj's formal coronation (Rajyabhisheka) take place at Raigad?",
            "6 June 1674", "15 August 1670", "19 February 1674", "10 November 1672",
            "A",
            "Shivaji was crowned Chhatrapati at Raigad on 6 June 1674 according to Vedic rites officiated by Gaga Bhatt.",
            "Easy"
        ),
        (
            "shivaji",
            "What was the eight-minister advisory council instituted by Chhatrapati Shivaji Maharaj called?",
            "Navaratna", "Ashta Pradhan", "Ashtadiggajas", "Saptaanga",
            "B",
            "The Ashta Pradhan council included the Peshwa (Prime Minister), Amatya (Finance), Senapati (Military), and others.",
            "Easy"
        ),
        (
            "shivaji",
            "Which brave commander sacrificed his life while recapturing the fortress of Kondhana (Sinhagad) in 1670?",
            "Baji Prabhu Deshpande", "Tanaji Malusare", "Netaji Palkar", "Yesaji Kank",
            "B",
            "Tanaji Malusare scaled the sheer cliff of Kondhana and defeated Udaybhan Rathod, prompting Shivaji to say: 'Gad aala, pan sinh gela'.",
            "Easy"
        ),
        (
            "shivaji",
            "What was the unique term used for the Maratha guerrilla warfare doctrine?",
            "Shankhavarta", "Ganimi Kawa", "Chakravyuh", "Tulghuma",
            "B",
            "Ganimi Kawa translates to 'enemy-deceiving guerrilla warfare', utilizing high speed, rugged terrain, and tactical ambushes.",
            "Medium"
        ),
        (
            "shivaji",
            "What gold coin did Chhatrapati Shivaji Maharaj issue following his coronation?",
            "Dinar", "Shivrai Hon", "Mohur", "Tanka",
            "B",
            "Shivaji issued gold 'Hon' and copper 'Shivrai' inscribed with 'Shri Raja Shiva Chhatrapati' in Devanagari script.",
            "Hard"
        ),
        (
            "shivaji",
            "Who was the renowned scholar and priest from Varanasi who officiated Shivaji's coronation ceremony?",
            "Ramdas Swami", "Gaga Bhatt", "Tukaram Maharaj", "Moropant Pingle",
            "B",
            "Pandit Gaga Bhatt (Vishveshvara) of Varanasi established Shivaji's Kshatriya lineage and presided over the Rajyabhisheka.",
            "Medium"
        ),
        (
            "shivaji",
            "In Shivaji's agrarian system, what was the maximum percentage of agricultural yield collected as state tax?",
            "20%", "40%", "60%", "75%",
            "B",
            "Shivaji fixed the state share strictly at 40% of agricultural yield, strictly forbidding arbitrary extortion by middlemen.",
            "Hard"
        ),
        (
            "shivaji",
            "From which Mughal city did Shivaji and his son Sambhaji escape in 1666 by hiding in baskets of sweets?",
            "Delhi", "Agra", "Lahore", "Fatehpur Sikri",
            "B",
            "Shivaji was placed under house arrest by Aurangzeb in Agra and executed a legendary escape inside large sweetmeat baskets.",
            "Easy"
        ),
        (
            "shivaji",
            "What was the name of the Maratha royal code of governance written by Ramchandra Pant Amatya summarizing Shivaji's policies?",
            "Budhabhushanam", "Adnyapatra", "Shivaji Charitra", "Sabhasad Bakhar",
            "B",
            "The Adnyapatra is a 17th-century treatise detailing Shivaji Maharaj's principles of fort building, naval defense, and statecraft.",
            "Hard"
        ),

        # SAMBHAJI (16 questions)
        (
            "sambhaji",
            "In which language did a 14-year-old Prince Sambhaji compose the treatise 'Budhabhushanam'?",
            "Marathi", "Sanskrit", "Prakrit", "Persian",
            "B",
            "Sambhaji composed Budhabhushanam in classical Sanskrit, demonstrating his mastery over statecraft, polity, and poetry.",
            "Medium"
        ),
        (
            "sambhaji",
            "How many military battles did Chhatrapati Sambhaji Maharaj fight without suffering a single defeat?",
            "Over 40", "Over 75", "Over 120", "Over 200",
            "C",
            "Throughout his nine-year reign, Sambhaji fought over 120 military engagements against Mughals, Siddis, and Portuguese without losing one.",
            "Medium"
        ),
        (
            "sambhaji",
            "Which rebel Mughal prince was granted royal asylum by Chhatrapati Sambhaji Maharaj in 1681?",
            "Prince Dara Shikoh", "Prince Sultan Muhammad Akbar", "Prince Khusrau", "Prince Murad",
            "B",
            "Sultan Muhammad Akbar, fourth son of Aurangzeb, rebelled against his father's religious fanaticism and found sanctuary with Sambhaji.",
            "Medium"
        ),
        (
            "sambhaji",
            "Which wealthy Mughal commercial city in Khandesh did Sambhaji raid in January 1681 shortly after his coronation?",
            "Surat", "Burhanpur", "Ahmednagar", "Aurangabad",
            "B",
            "Sambhaji and Hambirrao Mohite launched a lightning raid on Burhanpur, capturing immense imperial wealth to fund the war effort.",
            "Hard"
        ),
        (
            "sambhaji",
            "Against which colonial European power did Sambhaji lead the decisive Goa Campaign in 1683?",
            "The British", "The Portuguese", "The Dutch", "The French",
            "B",
            "Sambhaji counter-attacked Portuguese Goa after they colluded with Aurangzeb, storming St. Estevão island and nearly seizing Old Goa.",
            "Easy"
        ),
        (
            "sambhaji",
            "Who was the devoted poet-scholar from Kannauj who served as Sambhaji's trusted minister and shared his martyrdom?",
            "Gaga Bhatt", "Kavi Kalash", "Moropant Pingle", "Annaji Datto",
            "B",
            "Kavi Kalash (Kabji) was a brilliant scholar and Sambhaji's closest confidant who endured torture and martyrdom beside him.",
            "Easy"
        ),
        (
            "sambhaji",
            "Who served as the supreme Commander-in-Chief (Sarnaubat) under Chhatrapati Sambhaji Maharaj?",
            "Netaji Palkar", "Hambirrao Mohite", "Santaji Ghorpade", "Dhanaji Jadhav",
            "B",
            "Hambirrao Mohite, Sambhaji's maternal uncle, led victorious campaigns across Burhanpur and Gujarat until his death at the Battle of Wai (1687).",
            "Medium"
        ),
        (
            "sambhaji",
            "What engineering marvel did Sambhaji attempt in 1682 to capture the island fort of Janjira?",
            "Submarine tunnel", "A 2-km stone-and-timber sea causeway", "Hot air balloons", "A pontoon boat bridge",
            "B",
            "Sambhaji began building a 2-kilometer stone causeway directly through the ocean waves to bridge the mainland to Janjira.",
            "Hard"
        ),
        (
            "sambhaji",
            "At which village was Chhatrapati Sambhaji Maharaj ambushed and captured by Muqarrab Khan in 1689?",
            "Tulapur", "Sangameshwar", "Mahad", "Aner",
            "B",
            "Sambhaji was captured at Sangameshwar in the Konkan after local conspirators betrayed his small retinue's location.",
            "Medium"
        ),
        (
            "sambhaji",
            "At which location on the Bhima riverbank did Chhatrapati Sambhaji Maharaj attain supreme martyrdom in 1689?",
            "Tulapur", "Paithan", "Alandi", "Dehu",
            "A",
            "Sambhaji attained martyrdom at Tulapur on 11 March 1689, refusing to renounce his faith or surrender Swarajya's forts.",
            "Easy"
        ),
        (
            "sambhaji",
            "What reverent title was bestowed upon Sambhaji Maharaj by the people for his unbreakable defense of dharma and Swarajya?",
            "Dharmaveer", "Maharaja Adhiraj", "Deva Raya", "Sena Dhurandhar",
            "A",
            "Sambhaji is venerated across Maharashtra as 'Dharmaveer' (Defender of the Faith) for his unyielding sacrifice.",
            "Easy"
        ),
        (
            "sambhaji",
            "Which literary works in Brajbhasha were composed by Chhatrapati Sambhaji Maharaj besides Budhabhushanam?",
            "Nakhshikh and Nayikabhed", "Geet Govinda", "Raghuvamsham", "Dasbodh",
            "A",
            "Sambhaji authored Nakhshikh, Nayikabhed, and Saatsatak in Brajbhasha, proving his multifaceted poetic genius.",
            "Hard"
        ),
        (
            "sambhaji",
            "Who was the Queen Consort of Chhatrapati Sambhaji Maharaj who later endured 30 years of Mughal captivity while guiding Swarajya?",
            "Maharani Soyarabai", "Maharani Yesubai", "Maharani Tarabai", "Maharani Putalabai",
            "B",
            "Maharani Yesubai displayed immense fortitude, defending Raigad in 1689 and preserving the Maratha leadership while imprisoned.",
            "Medium"
        ),
        (
            "sambhaji",
            "Which two Maratha generals, trained under Sambhaji, wreaked havoc on Mughal forces through lightning guerrilla warfare after 1689?",
            "Santaji Ghorpade and Dhanaji Jadhav", "Tanaji and Baji Prabhu", "Moropant and Annaji Datto", "Yesaji Kank and Baji Pasalkar",
            "A",
            "Santaji Ghorpade and Dhanaji Jadhav spearheaded the 27-year war of independence, even raiding Aurangzeb's royal tent.",
            "Medium"
        ),
        (
            "sambhaji",
            "Where was Prince Sambhaji born on 14 May 1657?",
            "Shivneri Fort", "Purandar Fort", "Raigad Fort", "Pratapgad Fort",
            "B",
            "Sambhaji was born at Purandar Fort to Chhatrapati Shivaji Maharaj and Maharani Saibai.",
            "Easy"
        ),
        (
            "sambhaji",
            "What was the ultimate strategic consequence of Sambhaji Maharaj's nine-year defense of the Deccan?",
            "Marathas surrendered all hill forts", "Aurangzeb was forced to retreat to Delhi", "It drained the Mughal treasury and triggered the collapse of the Mughal Empire", "The British conquered Maharashtra",
            "C",
            "Sambhaji's defense bogged down 500,000 imperial troops in the Deccan, bankrupting the Mughal Empire and leading directly to its decline.",
            "Medium"
        ),

        # HARAPPA (16 questions)
        (
            "harappa",
            "Which Indian archaeologist excavated the first major site of Harappa in Punjab in 1920–1921?",
            "Rakhaldas Banerjee", "Daya Ram Sahni", "S. R. Rao", "A. Ghosh",
            "B",
            "Rai Bahadur Daya Ram Sahni began excavations at Harappa in 1920 under the direction of Sir John Marshall.",
            "Easy"
        ),
        (
            "harappa",
            "Who discovered the ruins of Mohenjo-daro ('Mound of the Dead') in Sindh in 1922?",
            "Daya Ram Sahni", "Rakhaldas Banerjee", "Mortimer Wheeler", "Alexander Cunningham",
            "B",
            "Rakhaldas Banerjee discovered Mohenjo-daro in 1922 while investigating ancient Buddhist ruins.",
            "Easy"
        ),
        (
            "harappa",
            "What was the standardized dimensional ratio of kiln-baked bricks used across Harappan cities?",
            "3:2:1", "4:2:1", "5:3:2", "4:3:1",
            "B",
            "Harappan burnt bricks universally adhered to the proportion of 4:2:1 (Length : Breadth : Thickness).",
            "Medium"
        ),
        (
            "harappa",
            "At which Harappan site was the world's earliest known tidal dockyard discovered?",
            "Dholavira", "Lothal", "Kalibangan", "Rakhigarhi",
            "B",
            "Lothal in Gujarat featured a sophisticated brick dockyard connected to the Gulf of Khambhat with automated sluice gates.",
            "Easy"
        ),
        (
            "harappa",
            "Which famous Harappan civic structure at Mohenjo-daro was sealed with a waterproof layer of natural bitumen (asphalt)?",
            "The Great Granary", "The Great Bath", "The Pillared Hall", "The Dockyard",
            "B",
            "The Great Bath of Mohenjo-daro was waterproofed with gypsum mortar and a thick lining of natural bitumen.",
            "Medium"
        ),
        (
            "harappa",
            "Which Harappan city in the Rann of Kutch is famous for its 16 rock-cut rainwater reservoirs and 10-glyph signboard?",
            "Lothal", "Dholavira", "Surkotada", "Banawali",
            "B",
            "Dholavira features an extraordinary water-harvesting system and a massive stone signboard found at its northern citadel gate.",
            "Easy"
        ),
        (
            "harappa",
            "At which site was the world's oldest ploughed agricultural field with grid furrows discovered?",
            "Harappa", "Kalibangan", "Chanhudaro", "Alamgirpur",
            "B",
            "Kalibangan in Rajasthan revealed a pre-Harappan ploughed field showing dual-crop furrow patterns identical to modern practices.",
            "Medium"
        ),
        (
            "harappa",
            "What animal is depicted most frequently on Harappan steatite seals?",
            "The Bengal Tiger", "The Unicorn (Single-horned mythical creature)", "The Humped Bull (Zebu)", "The Indian Elephant",
            "B",
            "The single-horned mythical creature ('unicorn') appears on more than 60% of all discovered Harappan seals.",
            "Medium"
        ),
        (
            "harappa",
            "The famous lost-wax cast artifact 'The Dancing Girl' discovered at Mohenjo-daro is made of which material?",
            "Terracotta", "Bronze", "Steatite", "Gold",
            "B",
            "The 10.5 cm Dancing Girl figurine was cast in bronze using the lost-wax (cire perdue) technique around 2300 BCE.",
            "Easy"
        ),
        (
            "harappa",
            "By what name is the Indus Valley Civilization believed to be referred to in ancient Mesopotamian cuneiform tablets?",
            "Magan", "Dilmun", "Meluhha", "Elam",
            "C",
            "Mesopotamian records describe maritime trade in ivory, lapis lazuli, and carnelian with the prosperous land of 'Meluhha'.",
            "Hard"
        ),
        (
            "harappa",
            "What material was primarily used by Harappans to carve their distinctive seals and intaglios?",
            "Marble", "Steatite (Soapstone)", "Sandstone", "Granite",
            "B",
            "Most Harappan seals were carved from soft steatite (soapstone) and then baked at high temperatures to whiten and harden them.",
            "Medium"
        ),
        (
            "harappa",
            "What type of weight system did the Harappans use for precision trade?",
            "Purely metric", "Binary in lower denominations, Decimal in higher ones", "Base-12 duodecimal", "Purely Roman fractions",
            "B",
            "Weights scaled by 1, 2, 4, 8, 16, 32, 64 (binary up to 16, which was ~13.7g) and transitioned to decimal multiples (160, 320, 640).",
            "Hard"
        ),
        (
            "harappa",
            "Which is currently recognized as the largest known geographical site of the Harappan Civilization?",
            "Mohenjo-daro", "Rakhigarhi (Haryana)", "Harappa", "Dholavira",
            "B",
            "Excavations in Rakhigarhi, Haryana, indicate it covers over 350 hectares, making it the largest known Harappan settlement.",
            "Medium"
        ),
        (
            "harappa",
            "In which direction was the undeciphered Harappan script predominantly written?",
            "Left to right", "Right to left", "Top to bottom only", "Boustrophedon alternate lines",
            "B",
            "Overlapping letters on pottery sherds prove Harappan script was written right-to-left, occasionally boustrophedon on longer inscriptions.",
            "Hard"
        ),
        (
            "harappa",
            "What iconic bearded statuette found at Mohenjo-daro is adorned with an ornate trefoil-patterned shawl?",
            "The Dancing Girl", "The Priest-King", "Pashupati", "The Great Mother Goddess",
            "B",
            "The steatite bust of the 'Priest-King' depicts a bearded figure wearing an armband and a shawl with carved trefoil motifs.",
            "Easy"
        ),
        (
            "harappa",
            "According to modern paleoclimatological studies, what was the primary cause of the decline of mature Harappan urban centers around 1900 BCE?",
            "Invasion by foreign armies", "Gradual climatic shifts, drying of the Saraswati/Ghaggar river, and eastward migration", "A massive meteorite impact", "A sudden viral pandemic",
            "B",
            "Geological and satellite data confirm that shifting monsoons and the progressive drying of the Ghaggar-Hakra river forced populations toward the Ganga basin.",
            "Medium"
        ),

        # REVOLT OF 1857 (16 questions)
        (
            "revolt1857",
            "Which controversial doctrine introduced by Lord Dalhousie annexed Jhansi, Satara, and Nagpur?",
            "Subsidiary Alliance", "Doctrine of Lapse", "Permanent Settlement", "Rowlatt Act",
            "B",
            "The Doctrine of Lapse stated that any princely state whose ruler died without a natural male heir would be annexed by the British.",
            "Easy"
        ),
        (
            "revolt1857",
            "On 29 March 1857, which sepoy of the 34th Bengal Native Infantry sparked the uprising at Barrackpore?",
            "Tatya Tope", "Mangal Pandey", "Ishwar Pande", "Bakht Khan",
            "B",
            "Mangal Pandey openly rebelled at Barrackpore parade ground, calling upon his fellow sepoys to resist the greased cartridges.",
            "Easy"
        ),
        (
            "revolt1857",
            "On which date did Indian sepoys at Meerut cantonment openly mutiny and march toward Delhi?",
            "29 March 1857", "10 May 1857", "23 June 1857", "15 August 1857",
            "B",
            "On Sunday evening, 10 May 1857, Meerut sepoys broke out of the cantonment, liberated their imprisoned comrades, and marched to Delhi.",
            "Easy"
        ),
        (
            "revolt1857",
            "Whom did the insurgent sepoys proclaim as the symbolic Emperor of India upon reaching the Red Fort in Delhi?",
            "Nana Saheb", "Bahadur Shah Zafar", "Wajid Ali Shah", "Birjis Qadr",
            "B",
            "The 82-year-old poet-monarch Bahadur Shah Zafar was proclaimed Shahenshah-e-Hindustan (Emperor of India) by the sepoys.",
            "Easy"
        ),
        (
            "revolt1857",
            "What was the immortal battle cry attributed to Rani Lakshmibai of Jhansi?",
            "Inquilab Zindabad", "Meri Jhansi nahi doongi!", "Jai Hind", "Do or Die",
            "B",
            "Upon hearing of Dalhousie's annexation order, Rani Lakshmibai resolutely declared: 'Meri Jhansi nahi doongi!' (I shall not give up my Jhansi!).",
            "Easy"
        ),
        (
            "revolt1857",
            "What was Rani Lakshmibai's birth name before her marriage to Maharaja Gangadhar Rao?",
            "Manikarnika Tambe", "Ahilyabai", "Tarabai", "Rani Chennamma",
            "A",
            "Born Manikarnika (Manu) Tambe in Varanasi, she was raised in the Bithoor household of the exiled Peshwa.",
            "Medium"
        ),
        (
            "revolt1857",
            "Which brilliant guerrilla commander fought alongside Rani Lakshmibai and Nana Saheb across Bundelkhand and Gwalior?",
            "Kunwar Singh", "Tatya Tope (Ramachandra Pandurang)", "Bakht Khan", "Mangal Pandey",
            "B",
            "Tatya Tope led mobile guerrilla operations across thousands of miles, eluding multiple British armies for nearly two years.",
            "Medium"
        ),
        (
            "revolt1857",
            "Which brave queen led the rebellion in Awadh, crowning her minor son Birjis Qadr and defending Lucknow?",
            "Rani Lakshmibai", "Begum Hazrat Mahal", "Rani Avantibai", "Kasturba Gandhi",
            "B",
            "Begum Hazrat Mahal organized the resistance in Awadh and the siege of the British Residency in Lucknow.",
            "Medium"
        ),
        (
            "revolt1857",
            "Which 80-year-old chieftain of Jagdishpur, Bihar, severed his own hand after being wounded and routed British forces?",
            "Tatya Tope", "Veer Kunwar Singh", "Amar Singh", "Maulvi Ahmadullah Shah",
            "B",
            "Veer Kunwar Singh amputated his own bullet-shattered left arm in the Ganga river to prevent gangrene and defeated British forces at Jagdishpur.",
            "Easy"
        ),
        (
            "revolt1857",
            "What rifle's greased cartridge caused outrage among Hindu and Muslim sepoys in early 1857?",
            "Lee-Enfield .303", "Enfield P-53 Rifled Musket", "Brown Bess Flintlock", "Martini-Henry",
            "B",
            "The Enfield Pattern 1853 rifled musket used cartridges lubricated with animal fat that soldiers had to bite open with their teeth.",
            "Medium"
        ),
        (
            "revolt1857",
            "Which items were secretly passed from village to village across northern India as symbols of the impending uprising?",
            "Swords and Shields", "Chapatis (flatbreads) and Red Lotus flowers", "Gold coins and flags", "Incense sticks",
            "B",
            "Chapatis and red lotus flowers were carried by watchmen across northern India as an underground signal of solidarity.",
            "Hard"
        ),
        (
            "revolt1857",
            "Where was Rani Lakshmibai martyred on 18 June 1858 while fighting General Hugh Rose's cavalry?",
            "Jhansi Fort", "Kotah-ki-Serai near Gwalior", "Bithoor", "Kalpi",
            "B",
            "Rani Lakshmibai was martyred on the battlefield of Kotah-ki-Serai near Gwalior Fort in soldier's attire.",
            "Medium"
        ),
        (
            "revolt1857",
            "What British legislative act formally dissolved the East India Company and transferred rule to the British Crown?",
            "Regulating Act of 1773", "Government of India Act 1858", "Pitt's India Act", "Charter Act of 1833",
            "B",
            "The Government of India Act 1858 liquidated the East India Company and transferred administration directly to Queen Victoria.",
            "Medium"
        ),
        (
            "revolt1857",
            "Where was the last Mughal Emperor, Bahadur Shah Zafar, exiled by the British after the rebellion?",
            "London", "Rangoon (Yangon), Burma", "Andaman Islands", "Colombo, Ceylon",
            "B",
            "Bahadur Shah Zafar was exiled to Rangoon, Burma, where he died in 1862 and was buried in an unmarked grave.",
            "Easy"
        ),
        (
            "revolt1857",
            "Which close companion of Rani Lakshmibai disguised herself as the Queen during the siege of Jhansi to facilitate the Rani's escape?",
            "Jhalkaribai", "Uda Devi", "Rani Avantibai", "Kanaklata Barua",
            "A",
            "Jhalkaribai, commander of the women's Durga Dal, closely resembled the Queen and misled British troops while the Rani escaped.",
            "Hard"
        ),
        (
            "revolt1857",
            "What notable phrase did British General Sir Hugh Rose use to describe Rani Lakshmibai in his post-war dispatches?",
            "The cunning rebel of Bundelkhand", "The bravest, the best, and the only man among the rebels", "A dangerous political fugitive", "The queen of chaos",
            "B",
            "General Hugh Rose praised his fallen adversary: 'She was the bravest, the best, and the only man among the rebels.'",
            "Hard"
        )
    ]
    cursor.executemany("INSERT INTO quiz_questions (topic_id, question, option_a, option_b, option_c, option_d, correct_option, explanation, difficulty) VALUES (?,?,?,?,?,?,?,?,?)", quiz_data)

    conn.commit()
    conn.close()
    print("IndicRoots database initialized and seeded successfully with rich historical data!")

if __name__ == "__main__":
    init_database()
