"""
content.py - Historical Data Module for Chhatrapati Shivaji Maharaj
Contains:
- 10 Chapters
- 10 Timeline Events
- 8 Key People
- 8 Key Places
- 10 Interesting Facts
- 15 Multiple-Choice Quiz Questions
"""

import database

# -------------------------------------------------------------------
# 1. CHAPTERS (10 Educational Chapters)
# -------------------------------------------------------------------
CHAPTERS = [
    {
        "chapter_number": 1,
        "title": "Birth, Lineage, and Formative Years",
        "content": (
            "Shivaji Bhosale was born at the hill fortress of Shivneri, near Junnar in western Maharashtra. "
            "His father, Shahaji Bhosale, was a distinguished military commander who served successively under the "
            "Ahmadnagar Nizamshahi and the Bijapur Adilshahi Sultanates. His mother, Jijabai (Rajmata Jijau), was the daughter "
            "of Lakhuji Jadhavrao of Sindkhed Raja, descending from a prominent noble lineage.\n\n"
            "Historians have noted a debate regarding Shivaji's exact date of birth. While older regional bakhars and early British "
            "accounts often suggested 6 April 1627, modern historical consensus, corroborated by the contemporary 'Jedhe Shakavali' "
            "and officially accepted by the Government of Maharashtra, places the date on 19 February 1630.\n\n"
            "During his childhood, while Shahaji was campaigning in the southern Deccan, Shivaji was raised in Pune under the guardianship "
            "of his mother Jijabai and the seasoned administrator Dadoji Konddeo. Jijabai instilled in young Shivaji a deep sense of justice, "
            "devotion, and cultural consciousness, using episodes from the Ramayana and Mahabharata to cultivate his ethical outlook. "
            "Surrounded by the rugged terrain of the Sahyadri mountains and bonding closely with the local pastoral hill-dwellers known as "
            "the Mavalas, Shivaji acquired unparalleled knowledge of the regional topography that would later form the bedrock of his military strategy."
        )
    },
    {
        "chapter_number": 2,
        "title": "The Oath of Swarajya and Early Fort Conquests",
        "content": (
            "In 1645, at approximately fifteen years of age, Shivaji assembled a loyal circle of youth from the Maval region, "
            "including close companions such as Tanaji Malusare, Yesaji Kank, and Baji Pasalkar, at the secluded Raireshwar Temple "
            "in the Bhor region. There, they took a solemn pledge to establish 'Hindavi Swarajya'—self-rule founded on justice and freedom "
            "from external despotic subjugation.\n\n"
            "Shivaji's political vision was pragmatic from the start. Rather than attempting open warfare against entrenched sultanate armies, "
            "he recognized that mountain fortresses formed the true keys to power in the Deccan. In 1646, he achieved his first major military "
            "triumph by securing Torna Fort (also known as Prachandgad) from the Adilshahi garrison through tactical persuasion and swift maneuvering.\n\n"
            "While repairing the fortifications of Torna, workers unearthed buried treasure pots filled with gold coins. Shivaji did not keep "
            "this wealth for personal luxury; instead, he invested every coin into constructing the adjacent hill fort of Rajgad. Rajgad served "
            "as his principal capital for over twenty-five years, standing as an unassailable bastion of the nascent Maratha state."
        )
    },
    {
        "chapter_number": 3,
        "title": "Consolidation in the Western Ghats (1647-1656)",
        "content": (
            "Between 1647 and 1656, Shivaji methodically expanded his domain across the Sahyadri ranges. He acquired strategic fortresses "
            "including Chakan, Kondhana (later renamed Sinhagad), and Purandar, fortifying them into mutually supporting defense networks. "
            "When the Bijapur court imprisoned his father Shahaji in an attempt to curb Shivaji's rising rebellion, Shivaji demonstrated mature "
            "diplomatic shrewdness by appealing to Mughal prince Murad Bakhsh, thereby exerting political pressure on Bijapur to secure his father's release.\n\n"
            "In 1656, Shivaji made a crucial territorial acquisition: the valley of Jawali, ruled by the More family, who held the hereditary "
            "feudal title of Chandrarao More under Adilshahi patronage. The Mores had consistently opposed Shivaji's calls for a unified native realm. "
            "Following failed diplomatic negotiations and subsequent conflict, Shivaji annexed the Jawali region.\n\n"
            "The acquisition of Jawali doubled Shivaji's territory and gave him command over the dense forests and trade routes leading to the "
            "Konkan coast. Recognizing the strategic importance of this rugged frontier, he commissioned his chief engineer, Moropant Trimbak Pingle, "
            "to construct the formidable fortress of Pratapgad on a towering ridge overlooking the Jawali valley."
        )
    },
    {
        "chapter_number": 4,
        "title": "The Battle of Pratapgad and Afzal Khan (1659)",
        "content": (
            "Alarmed by Shivaji's growing power, the Bijapur Sultanate dispatched its most experienced general, Afzal Khan, in 1659 with an army "
            "exceeding 10,000 soldiers, heavy siege guns, and cavalry. Afzal Khan marched through the Deccan plains, deliberately desecrating "
            "prominent religious shrines at Tuljapur and Pandharpur to provoke Shivaji into abandoning his mountain defenses for open-field combat.\n\n"
            "Refusing to fight on the enemy's terms, Shivaji remained stationed at Pratapgad, enveloped by the dense, treacherous Jawali forests. "
            "Recognizing that a direct assault on the mountain would be catastrophic, Afzal Khan initiated diplomatic talks, proposing a private "
            "meeting at the base of Pratapgad. Aware of Afzal Khan's past record of treachery—notably the murder of the ruler of Sera during a truce—"
            "Shivaji prepared carefully. Beneath his white tunic, he wore iron chainmail, concealed a steel cap under his turban, and hid a set of "
            "Wagh Nakh (steel tiger claws) and a Bichawa (scorpion dagger) in his sleeves.\n\n"
            "On 10 November 1659, during the parley, Afzal Khan embraced Shivaji and attempted to strangle him while thrusting a dagger into his side. "
            "The concealed armor stopped the blade. In self-defense, Shivaji retaliated with the Wagh Nakh, mortally wounding the general. At a pre-arranged "
            "signal, Maratha forces commanded by Kanhoji Jedhe and Moropant Pingle ambushed the Adilshahi army scattered through the valleys, capturing "
            "thousands of horses, artillery, and the entire enemy baggage train."
        )
    },
    {
        "chapter_number": 5,
        "title": "The Siege of Panhala and the Heroism of Pavan Khind (1660)",
        "content": (
            "Following the triumph at Pratapgad, Shivaji swiftly captured the massive fortress of Panhala near Kolhapur. In response, Bijapur sent "
            "a veteran commander, Siddi Jauhar, who laid a punishing siege around Panhala in mid-1660. For over five months, Shivaji and his garrison "
            "held out, but as supplies dwindled and monsoon storms lashed the mountains, a prolonged standoff became untenable.\n\n"
            "On a dark, rainy night in July 1660, Shivaji executed a daring breakout. Accompanied by a hand-picked detachment of 600 Mavala soldiers "
            "led by Sardar Baji Prabhu Deshpande, Shivaji slipped through the Adilshahi cordon. A decoy palanquin carrying a loyal barber named Shiva Kashid "
            "misled the initial pursuers, allowing Shivaji valuable time to advance toward the safety of Vishalgad fortress.\n\n"
            "When Siddi Jauhar's elite cavalry closed the gap near the narrow mountain gorge of Ghodkhind, Baji Prabhu Deshpande urged Shivaji to race "
            "to Vishalgad while he and 300 warriors held the narrow pass. Baji Prabhu pledged to fight until signal cannon shots from Vishalgad announced "
            "the king's safe arrival. For hours, against overwhelming enemy numbers, the small Maratha force defended the rocky defile. Despite sustaining "
            "multiple mortal wounds, Baji Prabhu fought until the distant boom of five cannon shots echoed across the valley. Having fulfilled his sacred "
            "duty, Baji Prabhu passed away, and Ghodkhind was forever immortalized as 'Pavan Khind' (The Sacred Pass)."
        )
    },
    {
        "chapter_number": 6,
        "title": "The Midnight Raid on Shaista Khan (1663)",
        "content": (
            "By 1660, Mughal Emperor Aurangzeb had grown deeply concerned about Maratha ascendancy and dispatched his maternal uncle, Shaista Khan, "
            "as Viceroy of the Deccan with a formidable imperial army of 70,000 troops. Shaista Khan captured Pune and occupied Shivaji's childhood residence, "
            "Lal Mahal, transforming it into his personal headquarters while unleashing economic devastation on the surrounding countryside for nearly three years.\n\n"
            "Recognizing that he could not dislodge Shaista Khan's vast garrison through a conventional assault, Shivaji engineered an audacious commando raid. "
            "On the night of 5 April 1663, during the Muslim holy month of Ramadan, Shivaji and approximately 400 chosen warriors entered Pune disguised "
            "as members of a Deccani wedding procession and soldiers guarding imperial prisoners. Knowing the layout of Lal Mahal intimately from his childhood, "
            "Shivaji's men breached a kitchen wall and entered the residential quarters.\n\n"
            "In the ensuing confusion, Shivaji confronted Shaista Khan in his bedchamber. As the viceroy attempted to escape through a window, Shivaji swung his sword, "
            "severing three of Shaista Khan's fingers. Shaista Khan's son and several guards were killed before the garrison could mobilize. Shivaji and his commandos "
            "withdrew safely into the night, using torches tied to the horns of oxen on a distant hill to mislead pursuit toward Sinhagad. The raid shattered Mughal prestige, "
            "compelling Aurangzeb to transfer the humiliated Shaista Khan to the distant province of Bengal."
        )
    },
    {
        "chapter_number": 7,
        "title": "The Treaty of Purandar and the Agra Escape (1665-1666)",
        "content": (
            "Following Shivaji's daring raid on the wealthy Mughal port of Surat in 1664 to replenish his state treasury, Aurangzeb dispatched his finest general, "
            "the veteran Rajput ruler Mirza Raja Jai Singh I, equipped with vast financial resources and imperial forces. Jai Singh employed sophisticated "
            "diplomatic encirclement and laid siege to Purandar Fort, where Maratha commander Murarbaji Deshpande fell heroically in defense.\n\n"
            "Recognizing the strategic necessity of temporary compromise to preserve his people from total destruction, Shivaji concluded the Treaty of Purandar "
            "in June 1665. Under its terms, Shivaji surrendered 23 of his 35 fortresses and agreed to visit the Mughal imperial court in Agra, assured of honorable "
            "treatment by Jai Singh.\n\n"
            "In May 1666, Shivaji arrived at Agra with his nine-year-old son, Sambhaji. At the imperial darbar, Aurangzeb treated Shivaji with calculated disrespect, "
            "placing him behind third-rank commanders (5,000-mansabdars). Shivaji loudly protested the indignity and stormed out, leading to his confinement under house arrest. "
            "Realizing his life was in grave danger, Shivaji feigned serious illness and began distributing large baskets of sweets and gifts to holy men and nobles as an act of charity. "
            "On 17 August 1666, having relaxed the guards' vigilance, Shivaji and young Sambhaji concealed themselves inside large sweetmeat baskets and slipped out of Agra. "
            "Traveling through disguised routes via Mathura, Varanasi, and the Deccan hills, Shivaji returned triumphantly to Raigad, a feat celebrated across contemporary India."
        )
    },
    {
        "chapter_number": 8,
        "title": "The Grand Coronation (Rajyabhisheka) at Raigad (1674)",
        "content": (
            "Between 1670 and 1673, Shivaji launched a brilliant counter-offensive, recapturing nearly all 23 fortresses surrendered in the Treaty of Purandar, "
            "most notably the dramatic reconquest of Kondhana (Sinhagad) by Tanaji Malusare in 1670. Despite his extensive territorial power, foreign and regional rulers "
            "often referred to Shivaji as a mere 'rebel zamindar' or insurgent chieftain because he had not been formally consecrated as an independent sovereign.\n\n"
            "To legitimize Swarajya under ancient Indian political philosophy and establish constitutional sovereignty, Shivaji decided to undergo a formal Vedic coronation. "
            "Pandit Gaga Bhatt, a revered scholar and authority on Dharmashastra from Varanasi, arrived at Raigad. After researching ancient geneaologies, he established "
            "Shivaji's descent from the solar Kshatriya lineage of the Sisodias of Mewar.\n\n"
            "On 6 June 1674, atop the majestic plateau of Raigad Fort, Shivaji was consecrated with sacred river waters and crowned with the title: "
            "'Kshatriya Kulavantas Chhatrapati Shivaji Maharaj' (Lord of the Kshatriya Clan and Paramount Sovereign). He initiated a new official calendar, "
            "the Rajyabhisheka Shaka, and minted his own independent coinage in gold (Shivrai Hon) and copper (Shivrai). The coronation formally transformed "
            "a regional resistance movement into an internationally recognized sovereign empire."
        )
    },
    {
        "chapter_number": 9,
        "title": "Administrative Genius and the Ashta Pradhan Council",
        "content": (
            "Shivaji Maharaj's enduring greatness lay not merely in his military exploits, but in his revolutionary administrative and agrarian reforms. "
            "He replaced arbitrary feudal rule with a structured, merit-based central governance system known as the 'Ashta Pradhan' (Council of Eight Ministers):\n\n"
            "1. Peshwa (Prime Minister) – General administration and state welfare.\n"
            "2. Amatya (Finance Minister) – Maintenance of state revenues and accounts.\n"
            "3. Sachiv (Secretary) – Preparation and verification of royal edicts.\n"
            "4. Mantri (Interior Minister) – Intelligence and state archives.\n"
            "5. Senapati (Commander-in-Chief) – Organization and command of the armed forces.\n"
            "6. Sumant (Foreign Minister) – Diplomatic relations and foreign intelligence.\n"
            "7. Panditrao (High Priest) – Religious affairs and social ethics.\n"
            "8. Nyayadhish (Chief Justice) – Administration of civil and criminal justice.\n\n"
            "In agrarian policy, Shivaji abolished the oppressive hereditary 'Watandari' system, where feudal landlords extorted peasant farmers. "
            "He surveyed agricultural lands using standardized measuring rods (kathi), fixed taxation strictly between 33% and 40% of actual yields, and provided state loans "
            "(tagai) for purchasing cattle and seeds during droughts. Crucially, Shivaji enforced strict military discipline: soldiers were paid cash salaries rather than "
            "land grants, and any soldier mistreating women, non-combatants, or agricultural crops faced severe court-martial penalties."
        )
    },
    {
        "chapter_number": 10,
        "title": "Naval Vision, Southern Expedition, and Enduring Legacy",
        "content": (
            "Shivaji was among the few rulers in medieval Indian history who recognized the decisive strategic value of maritime power. Observing Portuguese, "
            "British, Dutch, and Siddi vessels dominating the western coastline, he famously noted in the administrative treatise 'Adnyapatra': "
            "'He who has the navy owns the sea.' He commissioned a fleet of over 400 fighting ships—including Gurabs, Galbats, and Machwas—and constructed "
            "unbreachable marine fortresses such as Sindhudurg, Vijaydurg, and Padmadurg, anchoring foundations with molten lead directly into submarine rock.\n\n"
            "Between 1677 and 1678, Shivaji undertook his ambitious Southern Campaign ('Dakshin Digvijay'). Leading an army into the Carnatic and Tamil regions, "
            "he captured crucial fortresses such as Jinji and Vellore. This campaign proved historically vital: when Mughal Emperor Aurangzeb invaded Maharashtra "
            "a decade later with half a million troops, the Maratha kingdom was able to shift its strategic center to the fortress of Jinji, keeping the resistance alive.\n\n"
            "Chhatrapati Shivaji Maharaj passed away on 3 April 1680 at Raigad Fort at the age of fifty. He left behind an independent state spanning thousands of square miles, "
            "over 300 fortified bastions, an invincible cavalry, and an enduring civilizational philosophy. His emphasis on native self-respect, religious tolerance, "
            "welfare-centric governance, and tactical military science inspired generations of Indian freedom fighters, cementing his place as one of the greatest statesmen in world history."
        )
    }
]

# -------------------------------------------------------------------
# 2. TIMELINE EVENTS (10 Verified Chronological Events)
# -------------------------------------------------------------------
TIMELINE_EVENTS = [
    {
        "year": "1630 (19 Feb)",
        "title": "Birth of Shivaji Maharaj",
        "description": "Born at Shivneri Fort to Shahaji Bhosale and Jijabai. (An alternate date of 1627 exists in older records, but 1630 is the modern consensus)."
    },
    {
        "year": "1645",
        "title": "The Oath of Hindavi Swarajya",
        "description": "At age 15, Shivaji and his young Mavala comrades take an oath at Raireshwar Temple to establish indigenous self-rule."
    },
    {
        "year": "1646",
        "title": "Capture of Torna Fort",
        "description": "Shivaji secures his first hill fortress, Torna (Prachandgad), using unearthed treasure to construct the neighboring fortress of Rajgad."
    },
    {
        "year": "1656",
        "title": "Annexation of Jawali",
        "description": "Annexes the strategic forested valley of Jawali from the Chandrarao More family, doubling his territory and opening routes to Konkan."
    },
    {
        "year": "1659 (10 Nov)",
        "title": "The Battle of Pratapgad",
        "description": "Shivaji defeats and slays the Bijapuri general Afzal Khan in self-defense, annihilating the invading Adilshahi army in Jawali."
    },
    {
        "year": "1660 (July)",
        "title": "Breakout from Panhala and Pavan Khind",
        "description": "Shivaji escapes Siddi Jauhar's siege at Panhala while Baji Prabhu Deshpande heroically holds Ghodkhind with 300 warriors."
    },
    {
        "year": "1663 (5 Apr)",
        "title": "Midnight Raid on Lal Mahal",
        "description": "Infiltrates Shaista Khan's heavily guarded camp in Pune, severing the Mughal viceroy's fingers and shattering imperial prestige."
    },
    {
        "year": "1665 (June)",
        "title": "Treaty of Purandar",
        "description": "Concludes a tactical treaty with Mirza Raja Jai Singh, temporarily surrendering 23 forts and agreeing to visit the imperial court."
    },
    {
        "year": "1666 (17 Aug)",
        "title": "Daring Escape from Agra",
        "description": "Under house arrest by Aurangzeb, Shivaji and prince Sambhaji escape concealed inside large sweetmeat baskets."
    },
    {
        "year": "1674 (6 June)",
        "title": "Coronation (Rajyabhisheka) at Raigad",
        "description": "Formally consecrated as Chhatrapati by Pandit Gaga Bhatt, establishing an independent sovereign Maratha Empire."
    }
]

# -------------------------------------------------------------------
# 3. IMPORTANT PEOPLE (8 Historical Personalities)
# -------------------------------------------------------------------
PEOPLE = [
    {
        "name": "Jijabai Bhosale (Rajmata Jijau)",
        "role": "Mother, Mentor, and Guide",
        "description": "Daughter of Lakhuji Jadhavrao and mother of Shivaji Maharaj. She served as regent of the Pune jagir, dispensing justice and instilling values of freedom and statecraft in young Shivaji."
    },
    {
        "name": "Shahaji Bhosale",
        "role": "Father and Veteran Military Commander",
        "description": "Distinguished general who served under the Ahmadnagar and Bijapur Sultanates. His jagirs in Pune and Bangalore provided the foundational base for Shivaji's early activities."
    },
    {
        "name": "Tanaji Malusare",
        "role": "Subedar and Hero of Sinhagad",
        "description": "Close childhood companion and commander who led the daring night assault to recapture Kondhana (Sinhagad) in 1670, sacrificing his life in the victorious battle."
    },
    {
        "name": "Baji Prabhu Deshpande",
        "role": "Commander and Hero of Pavan Khind",
        "description": "Held the mountain pass of Ghodkhind with 300 Mavala soldiers against 4,000 Adilshahi cavalry in 1660, enabling Shivaji to safely reach Vishalgad."
    },
    {
        "name": "Netaji Palkar",
        "role": "First Sarnaubat (Commander-in-Chief)",
        "description": "Renowned as the 'Second Shivaji' by contemporaries due to his lightning-fast cavalry warfare across Maharashtra and the Deccan."
    },
    {
        "name": "Moropant Trimbak Pingle",
        "role": "First Peshwa (Prime Minister)",
        "description": "Master architect and chief administrator who served on Shivaji's Ashta Pradhan council, overseeing civil administration, revenue, and fort engineering."
    },
    {
        "name": "Pandit Gaga Bhatt",
        "role": "Eminent Scholar of Varanasi",
        "description": "Distinguished authority on Dharmashastra who verified Shivaji's solar Kshatriya lineage and officiated the Rajyabhisheka coronation at Raigad in 1674."
    },
    {
        "name": "Mirza Raja Jai Singh I",
        "role": "Mughal General and Ruler of Amber",
        "description": "Senior commander dispatched by Aurangzeb in 1665 who utilized diplomatic encirclement to negotiate the Treaty of Purandar with Shivaji."
    }
]

# -------------------------------------------------------------------
# 4. IMPORTANT PLACES (8 Strategic Fortresses and Sites)
# -------------------------------------------------------------------
PLACES = [
    {
        "name": "Shivneri Fort",
        "location": "Junnar, Pune District, Maharashtra",
        "description": "High-altitude hill fortress with steep escarpments and seven defensive gates where Shivaji Maharaj was born in 1630."
    },
    {
        "name": "Torna Fort (Prachandgad)",
        "location": "Velhe, Pune District, Maharashtra",
        "description": "The highest fort in the Pune region and the first major citadel captured by young Shivaji in 1646, marking the start of Swarajya."
    },
    {
        "name": "Rajgad Fort",
        "location": "Pune District, Maharashtra",
        "description": "Constructed using treasure unearthed at Torna, this majestic mountain citadel served as Shivaji's primary capital for over twenty-five years."
    },
    {
        "name": "Pratapgad Fort",
        "location": "Mahabaleshwar, Satara District, Maharashtra",
        "description": "Hill fort engineered by Moropant Pingle over the Jawali forests; site of the famous 1659 encounter with Adilshahi general Afzal Khan."
    },
    {
        "name": "Panhala Fort",
        "location": "Kolhapur District, Maharashtra",
        "description": "Expansive triangular plateau fortress besieged by Siddi Jauhar in 1660, from which Shivaji executed his legendary monsoon night escape."
    },
    {
        "name": "Sindhudurg Fort",
        "location": "Malvan Coast, Arabian Sea, Maharashtra",
        "description": "Pinnacle of Maratha marine architecture, built on Kurte island using molten lead foundations to secure naval sovereignty along the Konkan coast."
    },
    {
        "name": "Raigad Fort",
        "location": "Mahad, Raigad District, Maharashtra",
        "description": "The sovereign capital perched atop the Sahyadris; venue of Shivaji's formal coronation in 1674 and location of the royal court and Samadhi."
    },
    {
        "name": "Lal Mahal",
        "location": "Pune City, Maharashtra",
        "description": "Shivaji's childhood palace constructed by Shahaji Bhosale; site of the daring April 1663 midnight commando raid on Mughal viceroy Shaista Khan."
    }
]

# -------------------------------------------------------------------
# 5. INTERESTING FACTS (10 Educational Insights)
# -------------------------------------------------------------------
FACTS = [
    "Pioneer of the Indian Navy: Recognizing European maritime power, Shivaji built over 400 naval vessels and constructed marine fortresses like Sindhudurg and Vijaydurg.",
    "Strict Moral Code of Warfare: Shivaji strictly prohibited harming non-combatants, women, children, and religious sites during military campaigns, as acknowledged even by Mughal court historian Khafi Khan.",
    "Birth Date Historiography: While early colonial accounts cited 1627, modern historians rely on contemporary records like the Jedhe Shakavali to affirm 19 February 1630 as his birth date.",
    "Abolition of Revenue Farming: Shivaji replaced the exploitative hereditary Watandari tax-farming system with direct revenue payments strictly proportioned to agricultural harvest yields.",
    "Deflective Bastion Architecture: Fort ramparts were engineered with curved, rounded stonework so that enemy cannonballs would glance off rather than shatter the masonry.",
    "Independent Sovereign Currency: After his 1674 coronation, Shivaji issued gold coins (Shivrai Hon) and copper coins (Shivrai) inscribed in Devanagari script, signaling complete financial autonomy.",
    "Ecological Forestry Decrees: The royal administrative treatise 'Adnyapatra' strictly forbade cutting fruit-bearing trees like teak, jackfruit, and mango without owner compensation.",
    "Philosophy of Swarajya: Hindavi Swarajya was conceptualized not as a dynastic conquest, but as indigenous self-rule prioritizing peasant welfare and religious freedom.",
    "Ganimi Kawa (Guerrilla Warfare): Maratha tactics relied on extreme cavalry mobility, comprehensive knowledge of mountainous terrain, and strategic ambushes rather than rigid open-field battles.",
    "Promotion of Native Administrative Language: Shivaji commissioned the 'Rajyavyavahara Kosha', an administrative dictionary designed to replace court Persian with Sanskrit and Marathi terminology."
]

# -------------------------------------------------------------------
# 6. QUIZ QUESTIONS (15 Multiple-Choice Questions)
# -------------------------------------------------------------------
QUIZ_QUESTIONS = [
    {
        "question": "At which hill fortress was Chhatrapati Shivaji Maharaj born?",
        "option_a": "Raigad Fort",
        "option_b": "Shivneri Fort",
        "option_c": "Sinhagad Fort",
        "option_d": "Torna Fort",
        "correct_option": "B",
        "explanation": "Shivaji was born at Shivneri Fort near Junnar in western Maharashtra to Shahaji Bhosale and Jijabai."
    },
    {
        "question": "At which temple did young Shivaji take the solemn oath to establish Hindavi Swarajya in 1645?",
        "option_a": "Trimbakeshwar Temple",
        "option_b": "Raireshwar Temple",
        "option_c": "Bhimashankar Temple",
        "option_d": "Grishneshwar Temple",
        "correct_option": "B",
        "explanation": "In 1645, 15-year-old Shivaji and his Mavala comrades took the oath of Swarajya at the Raireshwar temple."
    },
    {
        "question": "Which was the first major hill fortress captured by young Shivaji in 1646?",
        "option_a": "Torna (Prachandgad)",
        "option_b": "Pratapgad",
        "option_c": "Purandar",
        "option_d": "Panhala",
        "correct_option": "A",
        "explanation": "Shivaji captured Torna Fort at age 16; the treasure found during its repairs helped finance the construction of Rajgad."
    },
    {
        "question": "Which Bijapuri general attempted to assassinate Shivaji during a personal truce parley at Pratapgad in 1659?",
        "option_a": "Shaista Khan",
        "option_b": "Afzal Khan",
        "option_c": "Siddi Jauhar",
        "option_d": "Rustam Zaman",
        "correct_option": "B",
        "explanation": "Afzal Khan met Shivaji at the base of Pratapgad and attacked him during an embrace, but Shivaji defended himself and slew the general."
    },
    {
        "question": "What concealed steel weapon did Shivaji use in self-defense against Afzal Khan?",
        "option_a": "Katar and Talwar",
        "option_b": "Wagh Nakh (Tiger Claws) and Bichawa",
        "option_c": "Dandpatta and Shield",
        "option_d": "Chakram",
        "correct_option": "B",
        "explanation": "Shivaji hid steel Wagh Nakh (tiger claws) and a Bichawa (scorpion dagger) in his sleeves, wearing chainmail beneath his tunic."
    },
    {
        "question": "Who heroically defended the mountain pass of Ghodkhind with 300 warriors to enable Shivaji's escape to Vishalgad in 1660?",
        "option_a": "Tanaji Malusare",
        "option_b": "Baji Prabhu Deshpande",
        "option_c": "Netaji Palkar",
        "option_d": "Moropant Pingle",
        "correct_option": "B",
        "explanation": "Baji Prabhu Deshpande held the pass until signal cannon shots confirmed Shivaji had reached Vishalgad safely."
    },
    {
        "question": "Which Mughal viceroy's fingers were severed during Shivaji's midnight commando raid inside Lal Mahal in 1663?",
        "option_a": "Mirza Raja Jai Singh",
        "option_b": "Shaista Khan",
        "option_c": "Dilir Khan",
        "option_d": "Prince Muazzam",
        "correct_option": "B",
        "explanation": "Shivaji led 400 commandos into Lal Mahal in Pune, severing Shaista Khan's fingers as the viceroy fled through a window."
    },
    {
        "question": "With which senior Rajput Mughal general did Shivaji negotiate the Treaty of Purandar in 1665?",
        "option_a": "Raja Jaswant Singh",
        "option_b": "Mirza Raja Jai Singh I",
        "option_c": "Raja Man Singh",
        "option_d": "Rana Raj Singh",
        "correct_option": "B",
        "explanation": "Mirza Raja Jai Singh I represented the Mughal Empire and negotiated the Treaty of Purandar with Shivaji in June 1665."
    },
    {
        "question": "How did Shivaji and his son Sambhaji escape house arrest in Agra in August 1666?",
        "option_a": "Disguised as Mughal soldiers",
        "option_b": "Concealed inside large sweetmeat baskets",
        "option_c": "Through a secret subterranean tunnel",
        "option_d": "Across the Yamuna river on boats",
        "correct_option": "B",
        "explanation": "Shivaji and young Sambhaji concealed themselves inside large baskets meant for charity gifts and slipped past the guards."
    },
    {
        "question": "Which brave commander sacrificed his life while recapturing Kondhana (Sinhagad) Fort in 1670?",
        "option_a": "Baji Prabhu Deshpande",
        "option_b": "Tanaji Malusare",
        "option_c": "Murarbaji Deshpande",
        "option_d": "Shiva Kashid",
        "correct_option": "B",
        "explanation": "Tanaji Malusare scaled the steep cliff of Kondhana and defeated the garrison, prompting the famous phrase 'Gad aala, pan sinh gela'."
    },
    {
        "question": "On which historic date was Shivaji formally crowned Chhatrapati at Raigad Fort?",
        "option_a": "6 June 1674",
        "option_b": "19 February 1674",
        "option_c": "15 August 1670",
        "option_d": "10 November 1672",
        "correct_option": "A",
        "explanation": "Shivaji's formal Vedic coronation (Rajyabhisheka) took place at Raigad on 6 June 1674, officiated by Pandit Gaga Bhatt."
    },
    {
        "question": "What was Shivaji's eight-minister administrative advisory council called?",
        "option_a": "Navaratnas",
        "option_b": "Ashta Pradhan",
        "option_c": "Ashtadiggajas",
        "option_d": "Saptaanga",
        "correct_option": "B",
        "explanation": "The Ashta Pradhan council included eight ministerial portfolios: Peshwa, Amatya, Sachiv, Mantri, Senapati, Sumant, Panditrao, and Nyayadhish."
    },
    {
        "question": "Which iconic marine fortress was constructed by Shivaji using molten lead to secure naval defense on the Konkan coast?",
        "option_a": "Janjira Fort",
        "option_b": "Sindhudurg Fort",
        "option_c": "Murud Fort",
        "option_d": "Arnala Fort",
        "correct_option": "B",
        "explanation": "Sindhudurg was built in 1664 off the Malvan coast with foundations poured with molten lead directly into submarine rock."
    },
    {
        "question": "What was the official gold coin minted by Shivaji Maharaj after his coronation in 1674?",
        "option_a": "Mohur",
        "option_b": "Shivrai Hon",
        "option_c": "Dinar",
        "option_d": "Tanka",
        "correct_option": "B",
        "explanation": "Shivaji issued gold 'Hon' and copper 'Shivrai' coins inscribed in Devanagari script to assert economic sovereignty."
    },
    {
        "question": "Which administrative Sanskrit-Marathi lexicon was commissioned by Shivaji to replace Persian court jargon?",
        "option_a": "Budhabhushanam",
        "option_b": "Rajyavyavahara Kosha",
        "option_c": "Adnyapatra",
        "option_d": "Sabhasad Bakhar",
        "correct_option": "B",
        "explanation": "The Rajyavyavahara Kosha was commissioned by Shivaji Maharaj to standardize native administrative terminology."
    }
]


# -------------------------------------------------------------------
# DATABASE SEEDING FUNCTION
# -------------------------------------------------------------------
def load_shivaji_data():
    """
    Inserts the complete historical dataset for Chhatrapati Shivaji Maharaj
    into the SQLite database using database.py functions.
    """
    # Ensure tables exist
    database.create_tables()

    # Check if Shivaji topic already exists
    topics = database.get_topics()
    topic_id = None
    for t in topics:
        if "Shivaji" in t["title"]:
            topic_id = t["id"]
            break

    # If topic does not exist, add it
    if topic_id is None:
        topic_id = database.add_topic(
            title="Chhatrapati Shivaji Maharaj",
            period="1630 - 1680 CE",
            summary=(
                "Founder of Hindavi Swarajya, master of guerrilla warfare (Ganimi Kawa), "
                "pioneer of Indian naval defense, and architect of welfare-centric administration."
            )
        )
        print(f"[OK] Created topic: Chhatrapati Shivaji Maharaj (Topic ID: {topic_id})")
    else:
        print(f"[OK] Found existing topic: Chhatrapati Shivaji Maharaj (Topic ID: {topic_id})")

    # Clear existing data for this topic to prevent duplicates when running repeatedly
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
    print(f"[OK] Inserted {len(CHAPTERS)} chapters.")

    # 2. Insert 10 Timeline Events
    for ev in TIMELINE_EVENTS:
        database.add_timeline_event(topic_id, ev["year"], ev["title"], ev["description"])
    print(f"[OK] Inserted {len(TIMELINE_EVENTS)} timeline events.")

    # 3. Insert 8 Important People
    for p in PEOPLE:
        database.add_person(topic_id, p["name"], p["role"], p["description"])
    print(f"[OK] Inserted {len(PEOPLE)} important people.")

    # 4. Insert 8 Important Places
    for pl in PLACES:
        database.add_place(topic_id, pl["name"], pl["location"], pl["description"])
    print(f"[OK] Inserted {len(PLACES)} important places.")

    # 5. Insert 10 Interesting Facts
    for f in FACTS:
        database.add_fact(topic_id, f)
    print(f"[OK] Inserted {len(FACTS)} interesting facts.")

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

    print(f"\n[SUCCESS] Chhatrapati Shivaji Maharaj dataset loaded into database successfully!")
    return topic_id


if __name__ == "__main__":
    print("Loading Chhatrapati Shivaji Maharaj dataset into SQLite database...")
    load_shivaji_data()
