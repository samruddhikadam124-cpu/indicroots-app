"""
sambhaji_data.py - Historical Data Module for Chhatrapati Sambhaji Maharaj
Contains:
- 10 Chapters
- 10 Timeline Events
- 8 Key People
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
        "title": "Birth, Bereavement, and Early Mentorship",
        "content": (
            "Sambhaji Bhosale was born on 14 May 1657 at the hill fortress of Purandar. He was the eldest son of Chhatrapati "
            "Shivaji Maharaj and his principal consort, Maharani Saibai. Tragically, when Sambhaji was barely two years old, "
            "his mother passed away in September 1659, just weeks prior to the fateful confrontation between Shivaji Maharaj and "
            "Adilshahi general Afzal Khan.\n\n"
            "Following his mother's death, the young prince was brought up under the direct tutelage of his paternal grandmother, "
            "Rajmata Jijabai. Jijabai, who had molded Shivaji's worldview, assumed maternal responsibility for Sambhaji's upbringing. "
            "She ensured he received an exceptional education befitting a royal heir, encompassing not only martial disciplines such as "
            "horsemanship, archery, and swordsmanship, but also rigorous grounding in Sanskrit literature, administrative ethics, and statecraft.\n\n"
            "Growing up amidst the formative struggles of Hindavi Swarajya, Sambhaji witnessed key political deliberations firsthand. "
            "His early environment instilled in him both a scholarly intellect and an unbending commitment to the sovereign cause of the Maratha realm."
        )
    },
    {
        "chapter_number": 2,
        "title": "The Agra Expedition and Childhood Diplomacy (1666)",
        "content": (
            "In 1665, following the Treaty of Purandar between Shivaji Maharaj and Mughal commander Mirza Raja Jai Singh, young Sambhaji "
            "was formally recognized by the imperial court as a commander of five thousand horsemen (5,000-mansabdar). In May 1666, at just "
            "nine years of age, Sambhaji accompanied his father to the imperial Mughal capital of Agra for an audience with Emperor Aurangzeb.\n\n"
            "At the imperial darbar, the Mughal sovereign treated Shivaji with open disregard, sparking Shivaji's vocal protest and their "
            "subsequent house arrest. Despite his tender age, Sambhaji observed imperial court dynamics, espionage, and political posturing. "
            "When Shivaji executed their legendary escape on 17 August 1666 concealed within large sweetmeat baskets, Sambhaji was smuggled "
            "out alongside his father.\n\n"
            "To evade intense imperial pursuit across northern India, Shivaji temporarily left Sambhaji in the care of trusted Brahmin "
            "associates in Mathura, spreading rumors that the young prince had succumbed to illness during the journey. Months later, once safe "
            "routes were secured, Sambhaji was safely escorted back to Raigad, having displayed remarkable resilience throughout this harrowing ordeal."
        )
    },
    {
        "chapter_number": 3,
        "title": "Literary Scholarship and Sanskrit Works",
        "content": (
            "A distinctive facet of Sambhaji Maharaj's life was his exceptional scholarly erudition, a trait often overlooked in purely "
            "military accounts. Fluent in Sanskrit, Marathi, Brajbhasha, Persian, and Hindi, Sambhaji was a prolific polymath who authored "
            "classical literary and political treatises during his adolescence.\n\n"
            "Around the age of fourteen, while residing at Shringarpur in the Konkan, he authored 'Budhabhushanam' (Ornament of the Wise), "
            "an elaborate socio-political treatise written in classical Sanskrit. Drawing upon ancient texts such as Kautilya's Arthashastra, "
            "the Kamandakiya Nitisara, and the Mahabharata, 'Budhabhushanam' offers comprehensive counsel on royal conduct, treasury management, "
            "fortress defense, judicial administration, and the strategic deployment of diplomatic envoys.\n\n"
            "Beyond Sanskrit political philosophy, Sambhaji composed poetry in Brajbhasha, authoring works such as 'Nakhshikh' (a poetic description "
            "of divine beauty), 'Nayikabhed', and 'Saatsatak'. Throughout his reign, he remained an ardent patron of poets, scholars, and temple "
            "endowments, maintaining close intellectual camaraderie with eminent literary figures such as Kavi Kalash."
        )
    },
    {
        "chapter_number": 4,
        "title": "Succession Crisis and Ascension to the Throne (1680-1681)",
        "content": (
            "Chhatrapati Shivaji Maharaj passed away at Raigad on 3 April 1680. At the time of his father's death, Sambhaji was stationed "
            "at the fortress of Panhala in southern Maharashtra. Taking advantage of the communication gap and longstanding court factionalism, "
            "a faction of senior ministers led by Annaji Datto and Moropant Pingle attempted to place Shivaji's younger son, the ten-year-old "
            "Rajaram, on the throne, keeping Shivaji's demise secret from Sambhaji.\n\n"
            "Informed of these developments, Sambhaji acted with decisive political judgment. He secured the strategic fortress of Panhala, "
            "won over the provincial army commanders, and gained the decisive backing of Commander-in-Chief (Sarnaubat) Hambirrao Mohite. "
            "Hambirrao, despite being Rajaram's maternal uncle, recognized Sambhaji's rightful seniority and exceptional military capabilities, "
            "swearing total allegiance to the elder prince.\n\n"
            "With the army united behind him, Sambhaji marched to Raigad without bloodshed. He treated Rajaram with familial affection and "
            "magnanimity while neutralizing rebellious ministerial conspiracies. On 16 January 1681, Sambhaji was formally crowned the second "
            "Chhatrapati of the Maratha Empire atop Raigad Fort amidst traditional Vedic rituals."
        )
    },
    {
        "chapter_number": 5,
        "title": "Internal Administration and Agrarian Policies",
        "content": (
            "Upon his accession, Chhatrapati Sambhaji preserved the institutional framework established by Shivaji Maharaj while adapting "
            "governance to meet the existential demands of prolonged wartime mobilization. He appointed Nilopant Moreshwar Pingle as Peshwa "
            "and elevated his trusted companion, Kavi Kalash, to the position of Chhandogamatya (Minister of Diplomacy and Religious Affairs).\n\n"
            "In rural administration, Sambhaji maintained strict oversight over regional tax collectors (Deshmukhs and Kulkarnis). "
            "He issued firm royal decrees forbidding revenue officers and passing military detachments from seizing peasant livestock, seeds, "
            "or fodder without fair market compensation. Aware that the peasantry formed the economic backbone of Swarajya, his administration "
            "extended agricultural loans (tagai) and granted tax remissions to drought-affected villages.\n\n"
            "Furthermore, Sambhaji displayed keen interest in civil works, directing the repair and expansion of fortress water-harvesting cisterns "
            "and maintaining commercial tariffs on foreign trading companies operating in Mumbai and Goa. His governance reflected a determined effort "
            "to protect civilian livelihoods even while the empire fought a continuous multi-front war."
        )
    },
    {
        "chapter_number": 6,
        "title": "The Imperial Threat: Prince Akbar and Aurangzeb's Invasion",
        "content": (
            "In early 1681, a major political crisis shook the Mughal Empire. Prince Sultan Muhammad Akbar, the fourth son of Emperor Aurangzeb, "
            "rebelled against his father's orthodox religious intolerance and discriminatory policies, notably the re-imposition of the Jizya tax. "
            "Facing overwhelming imperial armies in Rajasthan, Prince Akbar sought political asylum with Chhatrapati Sambhaji.\n\n"
            "Demonstrating extraordinary diplomatic audacity, Sambhaji granted refuge to the fugitive Mughal prince in June 1681, housing him with "
            "royal honors at Pali near the base of Sarasgad. Sambhaji envisioned a grand coalition uniting Maratha forces with dissenting Rajput clans "
            "and moderate Mughal factions to challenge Aurangzeb's autocratic rule in Delhi.\n\n"
            "Furious at this alliance and alarmed by Maratha defiance, Emperor Aurangzeb made a momentous decision: in late 1681, he mobilized the entire "
            "Mughal imperial court and an unprecedented army exceeding five hundred thousand soldiers, moving south to the Deccan. Aurangzeb vowed never "
            "to return to northern India until he had completely annihilated the Maratha state, initiating an eight-year conflict of attrition that would "
            "consume his empire."
        )
    },
    {
        "chapter_number": 7,
        "title": "The Burhanpur Raid and Defensive Campaigns (1681-1682)",
        "content": (
            "Even as Aurangzeb's massive armies began descending toward the Deccan, Sambhaji adopted an aggressive offensive-defensive strategy. "
            "Rather than passively waiting for imperial forces to besiege Maratha mountain fortresses, he executed preemptive strikes against wealthy "
            "Mughal commercial centers.\n\n"
            "In January 1681, Sambhaji and Sarnaubat Hambirrao Mohite launched a lightning cavalry raid over two hundred miles into the rich Mughal "
            "trading metropolis of Burhanpur in Khandesh. Burhanpur was a vital imperial treasury and manufacturing hub. Maratha forces bypassed Mughal "
            "frontier garrisons, entered the suburbs of the city, and secured immense wealth, including gold, horses, and luxury goods, without harming "
            "unarmed civilians.\n\n"
            "The revenue acquired from Burhanpur replenished the Maratha state treasury, funding fort fortifications and military provisions for "
            "several years. Throughout 1682, when Mughal forces under Prince Azam and Commander Shihab-ud-Din attempted incursions into Konkan and "
            "Khandesh, Sambhaji's mobile detachments intercepted supply lines, ambushed baggage trains, and forced imperial contingents to retreat "
            "in exhaustion."
        )
    },
    {
        "chapter_number": 8,
        "title": "The Janjira Siege and the Goa Campaign (1682-1683)",
        "content": (
            "Sambhaji recognized that maritime dominance along the Konkan coastline was critical for Swarajya's survival. To neutralize the "
            "Siddis of Janjira, who acted as naval auxiliaries for the Mughals and raided coastal villages, Sambhaji laid siege to the island fortress "
            "of Janjira in 1682. In an audacious engineering endeavor, he directed his engineers to construct a stone-and-timber causeway extending "
            "nearly two kilometers into the open sea to bridge the mainland to the fort, forcing the Siddi defenders into desperate resistance.\n\n"
            "In 1683, the Portuguese colonial administration in Goa entered into an unholy alliance with Aurangzeb, allowing Mughal supply vessels "
            "to berth in Portuguese harbors and threatening the southern flank of the Maratha kingdom. In response, Sambhaji launched a devastating "
            "counter-offensive into Goa in November 1683.\n\n"
            "Sambhaji personally led Maratha troops wading through the swollen Mandovi River at low tide, storming the key river fortress of "
            "Santo Estevão (St. Stephen's Island). He routed Portuguese forces, captured Chapora and Alorna, and pushed the Portuguese Viceroy, "
            "Francisco de Távora, to the brink of total defeat. The Viceroy in panic ordered the tomb of St. Francis Xavier opened in Old Goa to pray "
            "for divine deliverance. Only a sudden imperial Mughal troop advance into northern Konkan compelled Sambhaji to conclude peace terms "
            "and redirect his cavalry northward."
        )
    },
    {
        "chapter_number": 9,
        "title": "A War of Attrition, Betrayal, and Capture (1684-1689)",
        "content": (
            "Between 1684 and 1688, the conflict in the Deccan escalated into an exhausting war of attrition. Aurangzeb conquered the neighboring "
            "Sultanates of Bijapur (1686) and Golconda (1687), redirecting his entire imperial military machine exclusively against Sambhaji. "
            "Despite being heavily outnumbered, Sambhaji successfully maintained Maratha territorial integrity, fighting across multiple fronts "
            "without losing a single major battle.\n\n"
            "However, the relentless warfare took a severe toll on Maratha resources. In 1687, at the fiercely contested Battle of Wai, Maratha "
            "forces defeated the Mughal army of Sarja Khan, but suffered an irreplaceable loss when Sarnaubat Hambirrao Mohite was struck down by a cannonball. "
            "Concurrently, factional jealousy and discontent among certain orthodox nobles toward Sambhaji's trusted minister, Kavi Kalash, weakened internal harmony.\n\n"
            "In early 1689, following a strategic military conference at Vishalgad, Sambhaji and Kavi Kalash stayed at the riverside village of "
            "Sangameshwar in the Konkan with a small personal escort. Local conspirators from the Shirke clan, who bore personal grudges against the king, "
            "betrayed his exact coordinates to the Mughal commander Muqarrab Khan (Shaikh Nizam). In a rapid, stealthy cross-country march through the "
            "Amba Ghat, Muqarrab Khan surrounded the village. Despite valiant personal resistance, Sambhaji and Kavi Kalash were captured in early February 1689."
        )
    },
    {
        "chapter_number": 10,
        "title": "Martyrdom at Tulapur and Enduring Historical Legacy",
        "content": (
            "Brought in heavy chains to the imperial Mughal encampment at Bahadurgad, Sambhaji Maharaj and Kavi Kalash were paraded before the imperial court. "
            "Aurangzeb offered Sambhaji his life on strict conditions: surrender all Maratha hill fortresses, disclose the locations of the hidden state treasures, "
            "name the Mughal nobles who had secretly communicated with him, and embrace Islam.\n\n"
            "With unflinching defiance, Sambhaji rejected every demand, refusing to compromise the sovereignty of Swarajya or his ancestral faith. "
            "Infuriated by his unbroken composure, Aurangzeb subjected Sambhaji and Kavi Kalash to weeks of excruciating torture—blinding them with hot irons, "
            "extracting their nails, and peeling their flesh. Throughout this ordeal, Sambhaji maintained his resolve, uttering not a single plea for mercy.\n\n"
            "On 11 March 1689 (the auspicious Hindu new year of Gudhi Padwa), Sambhaji Maharaj was executed on the riverbanks of Tulapur, near the confluence "
            "of the Bhima and Indrayani rivers. Aurangzeb believed that killing the Maratha king would extinguish the rebellion; instead, it achieved the opposite. "
            "Sambhaji's supreme sacrifice electrified the Maratha nation, uniting nobles, soldiers, and peasants into a ferocious, decentralized war of independence "
            "led by Rajaram, Maharani Tarabai, Santaji Ghorpade, and Dhanaji Jadhav. This protracted struggle ultimately broke the Mughal Empire, immortalizing Sambhaji as 'Dharmaveer'."
        )
    }
]

# -------------------------------------------------------------------
# 2. TIMELINE EVENTS (10 Chronological Events)
# -------------------------------------------------------------------
TIMELINE_EVENTS = [
    {
        "year": "1657 (14 May)",
        "title": "Birth of Sambhaji Maharaj",
        "description": "Born at Purandar Fort to Chhatrapati Shivaji Maharaj and Maharani Saibai."
    },
    {
        "year": "1666 (May - August)",
        "title": "Agra Expedition and Escape",
        "description": "At age 9, appointed 5,000-mansabdar in Agra; escapes house arrest alongside Shivaji Maharaj concealed in sweet baskets."
    },
    {
        "year": "1671",
        "title": "Composition of Budhabhushanam",
        "description": "At age fourteen, Sambhaji authors his Sanskrit masterwork on statecraft, royal ethics, and warfare at Shringarpur."
    },
    {
        "year": "1680 (April)",
        "title": "Passing of Shivaji Maharaj",
        "description": "Following Shivaji's demise, Sambhaji manages court intrigues from Panhala and secures army loyalty."
    },
    {
        "year": "1681 (16 Jan)",
        "title": "Coronation as Second Chhatrapati",
        "description": "Formally crowned at Raigad Fort amidst traditional Vedic rituals as sovereign of the Maratha Empire."
    },
    {
        "year": "1681 (Jan - Feb)",
        "title": "Lightning Raid on Burhanpur",
        "description": "Sambhaji and Hambirrao Mohite execute a surprise cavalry raid on the wealthy Mughal hub of Burhanpur, acquiring vast supplies."
    },
    {
        "year": "1681 (June)",
        "title": "Asylum to Prince Akbar",
        "description": "Grants political asylum to Aurangzeb's rebel son Prince Sultan Muhammad Akbar, prompting Aurangzeb's Deccan invasion."
    },
    {
        "year": "1683 (Nov - Dec)",
        "title": "The Goa Campaign",
        "description": "Launches a counter-offensive against the Portuguese, storming Santo Estevão island and pushing Portuguese Goa to near surrender."
    },
    {
        "year": "1687",
        "title": "Battle of Wai and Loss of Hambirrao",
        "description": "Maratha forces defeat the Mughal army of Sarja Khan, but Commander-in-Chief Hambirrao Mohite is martyred in battle."
    },
    {
        "year": "1689 (11 March)",
        "title": "Martyrdom at Tulapur",
        "description": "After resisting weeks of torture, Sambhaji is executed at Tulapur, cementing his legacy as Dharmaveer and sparking the 20-year freedom war."
    }
]

# -------------------------------------------------------------------
# 3. IMPORTANT PEOPLE (8 Key Historical Personalities)
# -------------------------------------------------------------------
PEOPLE = [
    {
        "name": "Maharani Yesubai",
        "role": "Queen Consort and Guardian of Swarajya",
        "description": "Daughter of Pilaji Shirke and devoted wife of Sambhaji Maharaj. She held the royal seal during crises, led the defense of Raigad in 1689, and preserved Maratha dynastic continuity through 30 years of Mughal captivity."
    },
    {
        "name": "Hambirrao Mohite",
        "role": "Sarnaubat (Commander-in-Chief)",
        "description": "Maternal uncle of Sambhaji Maharaj and legendary supreme commander. He ensured Sambhaji's peaceful succession in 1680, led the Burhanpur raid, and fell heroically in victory at the Battle of Wai (1687)."
    },
    {
        "name": "Kavi Kalash (Kabji)",
        "role": "Chhandogamatya and Trusted Minister",
        "description": "Eminent poet and scholar from Kannauj who served as Sambhaji's closest confidant and diplomat. He managed state correspondence, composed inspiring verses, and stood steadfast beside Sambhaji during trial and martyrdom."
    },
    {
        "name": "Prince Sultan Muhammad Akbar",
        "role": "Rebel Mughal Prince",
        "description": "Fourth son of Emperor Aurangzeb who revolted against his father's orthodox bigotry in 1681 and sought royal sanctuary with Sambhaji, triggering the massive Mughal invasion of the Deccan."
    },
    {
        "name": "Emperor Aurangzeb",
        "role": "Mughal Emperor (Alamgir)",
        "description": "Mughal sovereign who moved his entire court and grand army to the Deccan in 1681, spending the final 25 years of his life in a futile war of attrition against Maratha independence."
    },
    {
        "name": "Nilopant Moreshwar Pingle",
        "role": "Peshwa (Prime Minister)",
        "description": "Son of Moropant Pingle who served as Sambhaji's Peshwa, managing civil administration, tax registers, and civilian supplies across the Maratha heartland."
    },
    {
        "name": "Francisco de Távora (Count of Alvor)",
        "role": "Portuguese Viceroy of Goa",
        "description": "Colonial administrator who allied with the Mughals against Sambhaji, suffering near-total defeat during Sambhaji's retaliatory assault across Goa in late 1683."
    },
    {
        "name": "Muqarrab Khan (Shaikh Nizam)",
        "role": "Mughal Military Commander",
        "description": "Experienced commander in Aurangzeb's service who executed the rapid cross-mountain march to ambush and capture Sambhaji and Kavi Kalash at Sangameshwar in 1689."
    }
]

# -------------------------------------------------------------------
# 4. IMPORTANT PLACES (8 Strategic Fortresses and Sites)
# -------------------------------------------------------------------
PLACES = [
    {
        "name": "Purandar Fort",
        "location": "Saswad, Pune District, Maharashtra",
        "description": "High-altitude hill fortress where Prince Sambhaji was born on 14 May 1657; scene of the 1665 treaty signed between Shivaji Maharaj and Mirza Raja Jai Singh."
    },
    {
        "name": "Raigad Fort",
        "location": "Mahad, Raigad District, Maharashtra",
        "description": "The capital of Hindavi Swarajya where Sambhaji was formally crowned the second Chhatrapati on 16 January 1681 and guided state administration."
    },
    {
        "name": "Panhala Fort",
        "location": "Kolhapur District, Maharashtra",
        "description": "Expansive triangular plateau fortress where Sambhaji was stationed during Shivaji Maharaj's passing and from which he consolidated army allegiance in 1680."
    },
    {
        "name": "Burhanpur",
        "location": "Khandesh, Madhya Pradesh",
        "description": "Major Mughal imperial trade and mint city along the Tapti River, targeted by Sambhaji and Hambirrao Mohite in a surprise cavalry raid in January 1681."
    },
    {
        "name": "Santo Estevão (St. Stephen's Island)",
        "location": "Mandovi River, Ilhas de Goa",
        "description": "Portuguese riverine island fort stormed by Sambhaji's amphibious cavalry assault during the dramatic Goa campaign of November 1683."
    },
    {
        "name": "Janjira Fort",
        "location": "Murud Coast, Raigad District, Maharashtra",
        "description": "Island citadel of the Siddis besieged by Sambhaji in 1682, featuring his ambitious project to construct a 2-km stone causeway through ocean waters."
    },
    {
        "name": "Sangameshwar",
        "location": "Ratnagiri District, Konkan, Maharashtra",
        "description": "Riverside market town where Sambhaji Maharaj and Kavi Kalash were ambushed and captured by Muqarrab Khan in early February 1689 following an intelligence leak."
    },
    {
        "name": "Tulapur",
        "location": "Confluence of Bhima and Indrayani Rivers, Pune District",
        "description": "Sacred site on the riverbanks where Sambhaji Maharaj and Kavi Kalash attained supreme martyrdom on 11 March 1689; venue of Sambhaji's Samadhi memorial."
    }
]

# -------------------------------------------------------------------
# 5. INTERESTING FACTS (10 Historical Facts)
# -------------------------------------------------------------------
FACTS = [
    "Literary Polymath: At age 14, Sambhaji authored 'Budhabhushanam' in Sanskrit, followed by three poetic works in Brajbhasha: 'Nakhshikh', 'Nayikabhed', and 'Saatsatak'.",
    "Undefeated Military Record: In his nine-year reign, Sambhaji led over 120 military engagements against Mughals, Portuguese, Siddis, and regional forces without losing a single battle.",
    "Diplomatic Refuge to Prince Akbar: In 1681, Sambhaji boldly granted asylum to Aurangzeb's rebel son Prince Akbar, seeking to build an alliance between Marathas and dissenting Rajput/Mughal nobles.",
    "The 2-km Sea Causeway at Janjira: To overcome the island defenses of the Siddi pirates in 1682, Sambhaji ordered his engineers to construct a stone-and-timber causeway directly into ocean waves.",
    "Linguistic Fluency: Sambhaji was fluent in multiple languages including Sanskrit, Marathi, Brajbhasha, Persian, Hindi, and Kannada, enabling him to examine diplomatic correspondence personally.",
    "Humbling the Portuguese Viceroy: Sambhaji's 1683 assault on Goa pushed Viceroy Francisco de Távora to place his baton of office at the shrine of St. Francis Xavier in desperate prayer for relief.",
    "Protection of Peasant Rights: Sambhaji issued strict decrees forbidding army detachments from confiscating peasant grain, plough-bullocks, or straw, penalizing corrupt revenue officials.",
    "Origin of the Title Dharmaveer: The people of Maharashtra revered him with the title 'Dharmaveer' (Champion of the Faith) for refusing to compromise his convictions despite weeks of torture.",
    "Catalyst for Decentralized Resistance: Sambhaji's execution backfired on Aurangzeb; it united Marathas into a 20-year decentralized people's war that ultimately bankrupted the Mughal Empire.",
    "Naval and Coastline Fortifications: Maintained maritime security along the Konkan by strengthening sea citadels like Sindhudurg, Vijaydurg, and Padmadurg against foreign colonial encroachments."
]

# -------------------------------------------------------------------
# 6. QUIZ QUESTIONS (15 Multiple-Choice Questions)
# -------------------------------------------------------------------
QUIZ_QUESTIONS = [
    {
        "question": "At which fortress was Prince Sambhaji born on 14 May 1657?",
        "option_a": "Shivneri Fort",
        "option_b": "Purandar Fort",
        "option_c": "Raigad Fort",
        "option_d": "Sinhagad Fort",
        "correct_option": "B",
        "explanation": "Sambhaji was born at Purandar Fort to Chhatrapati Shivaji Maharaj and Maharani Saibai."
    },
    {
        "question": "Who assumed primary responsibility for Sambhaji's upbringing after his mother Saibai's early death in 1659?",
        "option_a": "Maharani Soyarabai",
        "option_b": "Rajmata Jijabai",
        "option_c": "Maharani Putalabai",
        "option_d": "Tarabai",
        "correct_option": "B",
        "explanation": "His grandmother, Rajmata Jijabai, raised young Sambhaji, educating him in statecraft, diplomacy, and Sanskrit."
    },
    {
        "question": "In which classical language did a 14-year-old Prince Sambhaji author the statecraft treatise 'Budhabhushanam'?",
        "option_a": "Marathi",
        "option_b": "Sanskrit",
        "option_c": "Persian",
        "option_d": "Prakrit",
        "correct_option": "B",
        "explanation": "Sambhaji composed 'Budhabhushanam' in classical Sanskrit, analyzing royal duties, treasury administration, and military tactics."
    },
    {
        "question": "On which historic date was Sambhaji formally crowned as the second Chhatrapati at Raigad?",
        "option_a": "6 June 1674",
        "option_b": "16 January 1681",
        "option_c": "15 August 1680",
        "option_d": "11 March 1689",
        "correct_option": "B",
        "explanation": "Sambhaji Maharaj was consecrated as Chhatrapati at Raigad Fort on 16 January 1681."
    },
    {
        "question": "Which supreme military commander (Sarnaubat) backed Sambhaji during the 1680 succession crisis?",
        "option_a": "Netaji Palkar",
        "option_b": "Hambirrao Mohite",
        "option_c": "Santaji Ghorpade",
        "option_d": "Tanaji Malusare",
        "correct_option": "B",
        "explanation": "Hambirrao Mohite gave decisive military backing to Sambhaji, recognizing his rightful succession and martial capability."
    },
    {
        "question": "Which rebel Mughal prince sought and received political asylum from Chhatrapati Sambhaji in 1681?",
        "option_a": "Prince Dara Shikoh",
        "option_b": "Prince Sultan Muhammad Akbar",
        "option_c": "Prince Khusrau",
        "option_d": "Prince Murad Bakhsh",
        "correct_option": "B",
        "explanation": "Prince Sultan Muhammad Akbar rebelled against his father Aurangzeb's orthodox policies and was sheltered by Sambhaji."
    },
    {
        "question": "Which wealthy Mughal commercial and mint city in Khandesh did Sambhaji raid in January 1681?",
        "option_a": "Surat",
        "option_b": "Burhanpur",
        "option_c": "Aurangabad",
        "option_d": "Ahmednagar",
        "correct_option": "B",
        "explanation": "Sambhaji and Hambirrao Mohite launched a surprise cavalry raid on Burhanpur, acquiring immense treasury stores."
    },
    {
        "question": "Who was the Sanskrit poet from Kannauj who served as Sambhaji's closest companion and diplomat (Chhandogamatya)?",
        "option_a": "Gaga Bhatt",
        "option_b": "Kavi Kalash",
        "option_c": "Paramananda",
        "option_d": "Ramdas Swami",
        "correct_option": "B",
        "explanation": "Kavi Kalash served as minister and companion to Sambhaji, standing by his side through battles and eventual martyrdom."
    },
    {
        "question": "Against which European colonial power did Sambhaji lead the decisive campaign of 1683?",
        "option_a": "The British at Bombay",
        "option_b": "The Portuguese at Goa",
        "option_c": "The Dutch at Vengurla",
        "option_d": "The French at Pondicherry",
        "correct_option": "B",
        "explanation": "Sambhaji counter-attacked Portuguese Goa in late 1683 after they colluded with Mughal supply ships, storming Santo Estevão island."
    },
    {
        "question": "What engineering endeavor did Sambhaji undertake in 1682 to capture the island fort of Janjira?",
        "option_a": "Digging a submarine tunnel",
        "option_b": "Constructing a 2-km stone-and-timber sea causeway",
        "option_c": "Building floating wooden towers",
        "option_d": "Deploying hot-air balloons",
        "correct_option": "B",
        "explanation": "Sambhaji directed engineers to build a 2-kilometer stone causeway into the ocean to bridge the mainland to Janjira."
    },
    {
        "question": "Which famous battle in 1687 resulted in a Maratha victory but cost the life of Commander Hambirrao Mohite?",
        "option_a": "Battle of Pratapgad",
        "option_b": "Battle of Wai",
        "option_c": "Battle of Sangameshwar",
        "option_d": "Battle of Purandar",
        "correct_option": "B",
        "explanation": "At the Battle of Wai (1687), Maratha forces routed Sarja Khan's army, but Sarnaubat Hambirrao Mohite was martyred by a cannonball."
    },
    {
        "question": "At which Konkan riverside village were Sambhaji Maharaj and Kavi Kalash ambushed and captured in 1689?",
        "option_a": "Tulapur",
        "option_b": "Sangameshwar",
        "option_c": "Mahad",
        "option_d": "Alibaug",
        "correct_option": "B",
        "explanation": "Sambhaji and Kavi Kalash were captured at Sangameshwar after local conspirators betrayed their coordinates to Muqarrab Khan."
    },
    {
        "question": "At which location along the Bhima river did Chhatrapati Sambhaji Maharaj attain martyrdom on 11 March 1689?",
        "option_a": "Tulapur",
        "option_b": "Dehu",
        "option_c": "Alandi",
        "option_d": "Paithan",
        "correct_option": "A",
        "explanation": "Sambhaji Maharaj was executed at Tulapur near Pune, having refused all of Aurangzeb's ultimatums."
    },
    {
        "question": "What reverent title was bestowed upon Sambhaji Maharaj by the people for his steadfast sacrifice?",
        "option_a": "Navaratna",
        "option_b": "Dharmaveer",
        "option_c": "Maharajadhiraja",
        "option_d": "Sena Dhurandhar",
        "correct_option": "B",
        "explanation": "He is venerated across Maharashtra as 'Dharmaveer' (Champion of the Faith) for refusing to renounce his convictions under torture."
    },
    {
        "question": "Who was Sambhaji Maharaj's queen consort who defended Raigad in 1689 and spent 30 years in Mughal captivity?",
        "option_a": "Maharani Tarabai",
        "option_b": "Maharani Yesubai",
        "option_c": "Maharani Soyarabai",
        "option_d": "Maharani Saibai",
        "correct_option": "B",
        "explanation": "Maharani Yesubai displayed extraordinary courage, guiding Maratha policy and protecting the royal lineage while in captivity."
    }
]


# -------------------------------------------------------------------
# DATABASE SEEDING FUNCTION
# -------------------------------------------------------------------
def load_sambhaji_data():
    """
    Inserts the complete historical dataset for Chhatrapati Sambhaji Maharaj
    into the SQLite database without modifying or deleting existing topics.
    """
    # Ensure tables exist
    database.create_tables()

    # Check if Sambhaji topic already exists
    topics = database.get_topics()
    topic_id = None
    for t in topics:
        if "Sambhaji" in t["title"]:
            topic_id = t["id"]
            break

    # If topic does not exist, add it
    if topic_id is None:
        topic_id = database.add_topic(
            title="Chhatrapati Sambhaji Maharaj",
            period="1657 - 1689 CE",
            summary=(
                "Second Chhatrapati of the Maratha Empire, polymath scholar, and commander who "
                "defended Swarajya against prolonged imperial Mughal invasions without a battlefield defeat."
            )
        )
        print(f"[OK] Created topic: Chhatrapati Sambhaji Maharaj (Topic ID: {topic_id})")
    else:
        print(f"[OK] Found existing topic: Chhatrapati Sambhaji Maharaj (Topic ID: {topic_id})")

    # Clear old data for Sambhaji only, preserving other topics completely
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
    print(f"[OK] Inserted {len(CHAPTERS)} chapters for Sambhaji Maharaj.")

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

    print(f"\n[SUCCESS] Chhatrapati Sambhaji Maharaj dataset loaded into database successfully!")
    return topic_id


if __name__ == "__main__":
    print("Loading Chhatrapati Sambhaji Maharaj dataset into SQLite database...")
    load_sambhaji_data()
