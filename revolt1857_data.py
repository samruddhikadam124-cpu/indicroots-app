"""
revolt1857_data.py - Historical Data Module for the Revolt of 1857
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
        "title": "Background and the Expansion of Company Rule",
        "content": (
            "The Great Uprising of 1857 was not an isolated or sudden outburst; it was the culmination of a century of simmering "
            "grievances following the establishment of British East India Company (EIC) political hegemony. Beginning with the Battle "
            "of Plassey in 1757 and the Battle of Buxar in 1764, a commercial charter corporation gradually transformed into an imperial "
            "ruling apparatus, progressively annexing independent Indian states and subordinating regional sovereigns.\n\n"
            "As British rule expanded across the subcontinent, it disrupted traditional administrative structures, marginalized local "
            "aristocracies, and established an extractive colonial economy. The uprising represented a historic convergence where "
            "discontented native soldiers (sepoys), dispossessed feudal nobility, impoverished peasants, and urban artisans found "
            "common cause against an alien governing power.\n\n"
            "Historians emphasize that 1857 was a multifaceted movement. While British colonial authorities labeled it merely the "
            "'Sepoy Mutiny' to downplay its popular breadth, Indian nationalist historians, notably V. D. Savarkar, later characterized "
            "it as 'India's First War of Independence.' Modern scholarly consensus acknowledges both viewpoints, defining it as a major "
            "popular anti-colonial revolt combining military mutiny, aristocratic restoration, and widespread peasant rebellion."
        )
    },
    {
        "chapter_number": 2,
        "title": "Political Causes and the Doctrine of Lapse",
        "content": (
            "A primary catalyst for elite discontent was the aggressive expansionist policy pursued by Governor-General Lord Dalhousie "
            "(1848–1856). Central to his program was the controversial 'Doctrine of Lapse', an administrative policy declaring that any "
            "princely state under British paramountcy whose ruler died without a natural male heir would automatically be annexed by the "
            "Company, rejecting the long-standing Indian custom of adopting heirs.\n\n"
            "Under this doctrine, the British annexed several historic kingdoms, including Satara (1848), Sambalpur (1849), Nagpur (1854), "
            "and the principality of Jhansi (1853). The refusal to recognize young Anand Rao (later Damodar Rao), the adopted son of Maharaja "
            "Gangadhar Rao, alienated Rani Lakshmibai and sparked deep resentment across Bundelkhand.\n\n"
            "The political crisis reached a boiling point in February 1856 with the annexation of the wealthy kingdom of Awadh (Oudh). "
            "Because Awadh had natural heirs and had served as a loyal British ally, Dalhousie bypassed the Doctrine of Lapse and annexed the "
            "state on pretext of 'chronic misgovernance', exiling Nawab Wajid Ali Shah to Calcutta. This annexation caused profound distress, "
            "dispossessing thousands of landed taluqdars and enraging roughly seventy-five thousand Bengal Army sepoys recruited from Awadh."
        )
    },
    {
        "chapter_number": 3,
        "title": "Economic Ruin and Agrarian Distress",
        "content": (
            "Underlying the political discontent was severe, pervasive economic distress created by colonial revenue mechanisms and trade policies. "
            "The introduction of British land revenue settlements—notably the Permanent Settlement (Zamindari) in Bengal and Bihar, and the "
            "Ryotwari and Mahalwari systems in Central and Northern India—imposed rigid, exorbitant cash assessments that took no account of "
            "crop failures or drought.\n\n"
            "Peasants unable to pay cash taxes were forced into the clutches of moneylenders (mahajans), leading to widespread foreclosures "
            "and the loss of ancestral lands. In Awadh, British Inam Commissions confiscated thousands of tax-free estates held by traditional "
            "landlords (taluqdars), dissolving reciprocal rural patronage networks and driving both landlords and tenant farmers into collective poverty.\n\n"
            "Simultaneously, the British Industrial Revolution devastated traditional Indian manufacturing. Through the imposition of high tariffs "
            "on Indian handloom exports entering Britain and zero tariffs on machine-made British textiles entering India, domestic weavers, "
            "spinners, and metallurgical artisans were pauperized. Millions of displaced urban craftspeople were driven back to overcrowded "
            "agricultural fields, fueling deep systemic hostility toward the colonial administration."
        )
    },
    {
        "chapter_number": 4,
        "title": "Military Grievances and Socio-Religious Anxieties",
        "content": (
            "The military backbone of the East India Company's rule was the native sepoy army, predominantly recruited in northern India from "
            "high-caste Brahmin and Rajput families of Awadh and the Gangetic plains. Despite their vital role in winning British campaigns across "
            "India and abroad, Indian soldiers faced systemic racial discrimination, receiving inferior wages, poor food, and denial of foreign service "
            "allowances (bhatta), while promotions were capped strictly below the rank of Subedar.\n\n"
            "Socio-religious anxieties intensified in 1856 with the passage of Lord Canning's General Service Enlistment Act, which mandated that "
            "all newly recruited sepoys must serve overseas whenever ordered. To orthodox high-caste Hindu soldiers, crossing the ocean "
            "(the taboo of 'Kala Pani') implied ritual pollution and loss of caste, creating widespread suspicion that the British deliberately "
            "sought to subvert their social standing.\n\n"
            "These fears were compounded by the aggressive activities of Christian evangelical missionaries in public spaces, cantonments, and prisons, "
            "alongside social reform legislation such as the Abolition of Sati (1829) and the Hindu Widows' Remarriage Act (1856). While progressive "
            "in retrospective humanitarian terms, conservative sections of Indian society perceived these interventions as an imperial assault "
            "designed to dismantle indigenous religious institutions."
        )
    },
    {
        "chapter_number": 5,
        "title": "The Cartridge Controversy and Mangal Pandey",
        "content": (
            "The immediate spark that ignited the uprising was the introduction of the new Enfield Pattern 1853 rifled musket to replace the "
            "antiquated Brown Bess smoothbore musket. To load the Enfield rifle, soldiers were required to bite off the greased tip of a paper "
            "cartridge containing gunpowder and bullet before pouring the powder down the rifle barrel.\n\n"
            "In January 1857, a rumor originated at the Dum Dum arsenal near Calcutta that the cartridge paper was lubricated with grease derived "
            "from cattle tallow (sacred to Hindus) and pig lard (forbidden to Muslims). The rumor spread like wildfire across Bengal Army cantonments. "
            "Subsequent historical research confirmed that animal fats had indeed been used in early trial batches of grease without regard for "
            "Indian religious sensitivities. Although British officials quickly altered the grease composition and permitted soldiers to lubricate "
            "cartridges with wax and ghee, trust was irreparably shattered.\n\n"
            "On 29 March 1857, at the Barrackpore parade ground near Calcutta, a twenty-nine-year-old sepoy named Mangal Pandey of the 34th Bengal "
            "Native Infantry took up arms in open revolt. Calling upon his comrades to protect their religion, he fired upon his British adjutant "
            "and sergeant-major. Mangal Pandey was eventually overpowered, tried by court-martial, and hanged on 8 April 1857. His defiance electrified "
            "garrisons across northern India, transforming him into an early martyr of the resistance."
        )
    },
    {
        "chapter_number": 6,
        "title": "The Outbreak at Meerut and the March to Delhi (May 1857)",
        "content": (
            "The decisive military eruption occurred at the major military cantonment of Meerut, roughly forty miles northeast of Delhi. "
            "On 24 April 1857, eighty-five troopers of the 3rd Native Cavalry refused to handle the greased cartridges during firing drills. "
            "On 9 May, in an open parade, the soldiers were publicly degraded, stripped of their uniforms, shackled in heavy iron fetters, and "
            "sentenced to ten years of rigorous imprisonment.\n\n"
            "The following evening, Sunday, 10 May 1857, while British officers were attending church, native infantry and cavalry regiments broke into "
            "open mutiny. Joined by crowds of townspeople, sepoys attacked the cantonment, killed several European officers, broke open the military jails "
            "to liberate their imprisoned comrades, and seized arms and ammunition magazines. With spontaneous resolve, the rebel soldiers raised "
            "the rallying cry 'Chalo Dilli!' (March to Delhi).\n\n"
            "Riding through the night, the Meerut cavalry crossed the Yamuna river bridge of boats and entered Delhi on the morning of 11 May. "
            "The Delhi garrison joined the revolt. The sepoys surrounded the historic Red Fort, entered the Diwan-i-Khas, and proclaimed the reluctant, "
            "eighty-two-year-old Mughal poet-emperor, Bahadur Shah Zafar (Bahadur Shah II), as the supreme symbolic Emperor of India (Shahenshah-e-Hindustan). "
            "This action transformed what might have been an isolated garrison mutiny into a legitimate nationwide political revolution."
        )
    },
    {
        "chapter_number": 7,
        "title": "The War in Kanpur and Lucknow",
        "content": (
            "In Kanpur (Cawnpore), the rebellion found leadership in Nana Saheb (Dhondu Pant), the adopted son of the exiled Maratha Peshwa Baji Rao II. "
            "When the British government discontinued his father's pension, Nana Saheb was deeply alienated. Supported by his brilliant military general "
            "Tatya Tope and his diplomatic advisor Azimullah Khan, Nana Saheb besieged the entrenchments of British Major-General Hugh Wheeler in June 1857.\n\n"
            "Following an offer of safe passage to Allahabad, the British garrison surrendered at Sati Chaura Ghat, where chaotic firing broke out, resulting "
            "in the deaths of most British soldiers. The surviving European women and children were confined at the Bibighar residence and tragically killed "
            "shortly before British relief forces commanded by General Henry Havelock recaptured the city, prompting brutal, indiscriminate British reprisals "
            "across the Gangetic plains.\n\n"
            "Concurrently in Awadh, the resistance was organized by Begum Hazrat Mahal, the resolute wife of the deposed Nawab Wajid Ali Shah. "
            "She rallied Hindu and Muslim taluqdars, crowned her minor son Birjis Qadr, and laid siege to the fortified British Residency in Lucknow "
            "in June 1857. For nearly five months, rebel forces held the Residency under intense bombardment until Sir Colin Campbell broke through "
            "in November 1857, though guerrilla warfare across the rural Awadh countryside persisted well into 1858."
        )
    },
    {
        "chapter_number": 8,
        "title": "The Central Indian Campaign: Rani Lakshmibai of Jhansi",
        "content": (
            "In Central India, the struggle reached its epic climax under the leadership of Rani Lakshmibai of Jhansi. Born Manikarnika (Manu) Tambe "
            "in Varanasi and raised in the Bithoor court, she assumed administrative governance of Jhansi following the June 1857 sepoy revolt, "
            "resolutely declaring: 'Meri Jhansi nahi doongi!' (I shall not surrender my Jhansi).\n\n"
            "In March 1858, British Major-General Sir Hugh Rose laid siege to the massive granite fortress of Jhansi with veteran troops and heavy artillery. "
            "For two weeks, the Rani directed the defense, with civilian women and men assisting on the ramparts. A relief force of twenty thousand fighters "
            "led by Tatya Tope was defeated outside the walls. When the city defenses were breached on 3 April, Rani Lakshmibai executed a legendary escape "
            "at midnight, riding on horseback with her young adopted son Damodar Rao strapped to her back, accompanied by loyal Afghan and Maratha guards.\n\n"
            "Rejoining Tatya Tope and Rao Saheb at Kalpi, they executed a masterstroke: capturing the impregnable fortress of Gwalior from the loyalist Sindhia "
            "rulers in June 1858. On 18 June 1858, while fighting heroically in warrior attire at Kotah-ki-Serai outside Gwalior, Rani Lakshmibai was martyred "
            "in cavalry combat. In his official dispatch, General Hugh Rose paid tribute to his fallen adversary, writing that she was 'the bravest, the best, "
            "and the only man among the rebels.'"
        )
    },
    {
        "chapter_number": 9,
        "title": "Eastern Resistance and Guerrilla Operations: Kunwar Singh and Tatya Tope",
        "content": (
            "In western Bihar, the uprising was led by the remarkable eighty-year-old chieftain of Jagdishpur, Veer Kunwar Singh. Despite his advanced age, "
            "Kunwar Singh possessed masterclass military acumen. Joining the mutinous Dinapore sepoys in July 1857, he liberated the town of Arrah and established "
            "an independent administration.\n\n"
            "Pursued by British detachments under Vincent Eyre, Kunwar Singh retreated into the dense jungles and fought a brilliant guerrilla campaign "
            "across Bihar, Rewa, and eastern Uttar Pradesh, capturing Azamgarh in March 1858. While retreating across the Ganga river back toward Jagdishpur, "
            "his left wrist was shattered by a British cannon shot; in an act of legendary resolve, Kunwar Singh severed his own hand with his sword to prevent "
            "gangrene and offered it to the river. Returning to Jagdishpur, he routed Captain Le Grand's forces on 23 April 1858, passing away undefeated "
            "three days later in his ancestral fortress.\n\n"
            "Meanwhile, following the fall of Gwalior, Tatya Tope led an extraordinary guerrilla campaign spanning thousands of miles across Central India, "
            "Bundelkhand, and the Aravalli hills for nearly a year, baffling several pursuing British columns under generals Rose, Napier, and Roberts. "
            "Betrayed by a trusted feudal ally, Raja Man Singh of Narwar, Tatya Tope was captured while sleeping in the Paron forests in April 1859 and executed "
            "at Shivpuri, bravely mounting the gallows without remorse."
        )
    },
    {
        "chapter_number": 10,
        "title": "British Retribution, Consequences, and Historical Transformation",
        "content": (
            "The suppression of the 1857 uprising by mid-1858 was accompanied by savage British retribution. Across Delhi, Kanpur, Allahabad, and Lucknow, "
            "British forces under officers like General James Neill carried out indiscriminate summary executions, hanging thousands of suspected rebels "
            "and blowing captured sepoys from cannons. The aged emperor Bahadur Shah Zafar was subjected to a show trial in the Red Fort, convicted of treason, "
            "and exiled to Rangoon (Yangon, Burma), where he passed away in 1862, ending the three-hundred-year Mughal dynasty.\n\n"
            "Despite its military defeat, the Revolt of 1857 triggered a monumental constitutional transformation in British colonial governance:\n"
            "1. Liquidation of the Company: The British Parliament enacted the Government of India Act 1858, dissolving the East India Company and transferring "
            "direct administrative authority over India to the British Crown, headed by a cabinet minister styled the Secretary of State for India.\n"
            "2. Queen Victoria's Proclamation (1 November 1858): Pledged non-interference in Indian religious practices, abandoned the hated Doctrine of Lapse, "
            "and promised equal legal treatment for Indian subjects, though racial hierarchy in practice remained entrenched.\n"
            "3. Military Reorganization: The Indian Army was restructured along the 'martial races' doctrine, deliberately balancing diverse regional and caste "
            "regiments to prevent collective mutiny, with European soldiers maintaining exclusive control over artillery.\n\n"
            "In modern Indian historical consciousness, 1857 represents the foundational watershed that shattered the myth of European invincibility, "
            "inspiring the organized national freedom movement of the twentieth century."
        )
    }
]

# -------------------------------------------------------------------
# 2. TIMELINE EVENTS (10 Verified Chronological Milestones)
# -------------------------------------------------------------------
TIMELINE_EVENTS = [
    {
        "year": "1848 - 1856",
        "title": "Implementation of the Doctrine of Lapse",
        "description": "Lord Dalhousie annexes Satara (1848), Sambalpur (1849), Jhansi (1853), and Nagpur (1854), denying customary rights to adopted heirs."
    },
    {
        "year": "1856 (Feb)",
        "title": "Annexation of Awadh (Oudh)",
        "description": "British East India Company deposes Nawab Wajid Ali Shah on charges of misgovernance, alienating taluqdars and 75,000 native sepoys."
    },
    {
        "year": "1856",
        "title": "General Service Enlistment Act and Enfield Rifles",
        "description": "Lord Canning mandates overseas service for new recruits; introduction of the Enfield P-53 musket with greased paper cartridges."
    },
    {
        "year": "1857 (29 March)",
        "title": "Mangal Pandey's Defiance at Barrackpore",
        "description": "Sepoy Mangal Pandey of the 34th Bengal Native Infantry revolts against the greased cartridge, shooting British officers at parade."
    },
    {
        "year": "1857 (10 May)",
        "title": "The Outbreak at Meerut Cantonment",
        "description": "Following the court-martial of 85 cavalrymen, sepoys rise in open mutiny, liberate comrades, and march overnight shouting 'Chalo Dilli'."
    },
    {
        "year": "1857 (11 May)",
        "title": "Bahadur Shah Zafar Proclaimed Emperor",
        "description": "Insurgent soldiers reach Delhi's Red Fort, declaring the aged poet-emperor Bahadur Shah Zafar the symbolic leader of the rebellion."
    },
    {
        "year": "1857 (June)",
        "title": "Uprisings in Kanpur and Lucknow",
        "description": "Nana Saheb leads the resistance in Kanpur; Begum Hazrat Mahal crowns Birjis Qadr and organizes the siege of the Lucknow Residency."
    },
    {
        "year": "1858 (March - April)",
        "title": "The Siege and Defense of Jhansi",
        "description": "Sir Hugh Rose besieges Jhansi; Rani Lakshmibai leads a two-week defense before executing a midnight equestrian breakout to Kalpi."
    },
    {
        "year": "1858 (18 June)",
        "title": "Battlefield Martyrdom of Rani Lakshmibai",
        "description": "The Queen of Jhansi falls heroically in battle at Kotah-ki-Serai outside Gwalior, earning the respect of her British adversaries."
    },
    {
        "year": "1858 (1 November)",
        "title": "Queen Victoria's Proclamation",
        "description": "Formal dissolution of the British East India Company; direct governance of India transferred to the British Crown."
    }
]

# -------------------------------------------------------------------
# 3. IMPORTANT PEOPLE (8 Key Historical Personalities)
# -------------------------------------------------------------------
PEOPLE = [
    {
        "name": "Rani Lakshmibai of Jhansi",
        "role": "Queen of Jhansi and Military Leader",
        "description": "Born Manikarnika Tambe, she defied Lord Dalhousie's Doctrine of Lapse, heroically defended Jhansi citadel, captured Gwalior Fort with Tatya Tope, and fell in battle at Kotah-ki-Serai."
    },
    {
        "name": "Mangal Pandey",
        "role": "Sepoy of the 34th Bengal Native Infantry",
        "description": "A soldier whose armed defiance against the Enfield greased cartridges on 29 March 1857 at Barrackpore parade ground sparked the revolutionary movement across northern cantonments."
    },
    {
        "name": "Bahadur Shah Zafar (Bahadur Shah II)",
        "role": "Last Mughal Emperor and Symbolic Sovereign",
        "description": "The 82-year-old poet-monarch residing in Delhi's Red Fort who was proclaimed Shahenshah-e-Hindustan by insurgent sepoys, lending royal legitimacy to the resistance."
    },
    {
        "name": "Nana Saheb (Dhondu Pant)",
        "role": "Leader of the Uprising in Kanpur",
        "description": "Adopted son of exiled Peshwa Baji Rao II who took command in Kanpur after the British discontinued his father's pension, organizing civil and military resistance."
    },
    {
        "name": "Tatya Tope (Ramachandra Pandurang)",
        "role": "General and Master of Guerrilla Warfare",
        "description": "Brilliant commander who fought alongside Nana Saheb in Kanpur, aided Rani Lakshmibai in capturing Gwalior, and led an elusive year-long guerrilla campaign across Central India."
    },
    {
        "name": "Begum Hazrat Mahal",
        "role": "Queen Regent and Leader of Awadh",
        "description": "First wife of the deposed Nawab Wajid Ali Shah who mobilized Hindu and Muslim taluqdars, crowned her young son Birjis Qadr, and commanded the siege of the British Residency in Lucknow."
    },
    {
        "name": "Veer Kunwar Singh",
        "role": "Chieftain of Jagdishpur (Bihar)",
        "description": "The 80-year-old warrior king of Bhojpur, Bihar, who outmaneuvered British columns across Bihar and eastern UP, famously severing his own injured hand in the Ganga before dying undefeated."
    },
    {
        "name": "General Sir Hugh Rose",
        "role": "British Field Commander (Central India)",
        "description": "Veteran British general who commanded the Central India Field Force against Jhansi, Kalpi, and Gwalior, famous for praising Rani Lakshmibai as 'the bravest and best among the rebels.'"
    }
]

# -------------------------------------------------------------------
# 4. IMPORTANT PLACES (8 Strategic Centres and Battlefields)
# -------------------------------------------------------------------
PLACES = [
    {
        "name": "Barrackpore",
        "location": "Near Kolkata, West Bengal (Hooghly River)",
        "description": "Major British military cantonment where sepoy Mangal Pandey openly revolted against his commanding officers on 29 March 1857, initiating the resistance."
    },
    {
        "name": "Meerut Cantonment",
        "location": "Meerut, Western Uttar Pradesh",
        "description": "Garrison town where 85 cavalry troopers were fettered for refusing cartridges, triggering the general mutiny of 10 May 1857 and the historic march to Delhi."
    },
    {
        "name": "The Red Fort (Lal Qila), Delhi",
        "location": "Old Delhi, Yamuna Riverbank",
        "description": "Historic Mughal palace-citadel where mutinous sepoys gathered on 11 May 1857, declaring Bahadur Shah Zafar the symbolic sovereign of a liberated India."
    },
    {
        "name": "The British Residency, Lucknow",
        "location": "Lucknow, Awadh, Uttar Pradesh",
        "description": "Colonial administrative compound besieged for five months by rebel sepoys and citizens under Begum Hazrat Mahal; its bullet-riddled ruins stand preserved today."
    },
    {
        "name": "Kanpur (Cawnpore)",
        "location": "Central Uttar Pradesh on the Ganga River",
        "description": "Strategic garrison metropolis where Nana Saheb and Tatya Tope besieged British forces under Hugh Wheeler, site of the tragic Sati Chaura and Bibighar episodes."
    },
    {
        "name": "Jhansi Fort",
        "location": "Jhansi, Bundelkhand, Uttar Pradesh",
        "description": "Hilltop granite fortress with 22 bastions where Rani Lakshmibai directed a two-week defense against Sir Hugh Rose before escaping on horseback to Kalpi."
    },
    {
        "name": "Gwalior Fort",
        "location": "Gwalior, Madhya Pradesh",
        "description": "Towering sandstone citadel captured in a daring June 1858 offensive by Rani Lakshmibai and Tatya Tope; scene of the Rani's martyrdom at nearby Kotah-ki-Serai."
    },
    {
        "name": "Jagdishpur",
        "location": "Bhojpur District, Western Bihar",
        "description": "Ancestral fortress of Veer Kunwar Singh, which served as the operational headquarters for his anti-colonial guerrilla campaigns across Bihar."
    }
]

# -------------------------------------------------------------------
# 5. INTERESTING FACTS (10 Verified Historical Facts)
# -------------------------------------------------------------------
FACTS = [
    "Enfield P-53 Cartridge Composition: The paper cartridges were sealed with a grease mixture containing beef tallow and pork lard, offensive to both Hindu and Muslim dietary prohibitions.",
    "The Mystery of the Chapatis: In early 1857, thousands of unleavened bread cakes (chapatis) and red lotus flowers were secretly circulated from village to village as untraceable symbols of solidarity.",
    "Jhalkaribai's Battlefield Disguise: Jhalkaribai, a Dalit warrior and commander of the women's Durga Dal, disguised herself as Rani Lakshmibai to mislead British troops, enabling the Rani's safe escape.",
    "Veer Kunwar Singh's Self-Amputation: When struck in the wrist by a cannonball while crossing the Ganga, 80-year-old Kunwar Singh severed his own arm with his sword to prevent poison, offering it to the river.",
    "Dissolution of the East India Company: The 1857 revolt permanently ended 250 years of commercial and political governance by the East India Company, placing India directly under the British Crown.",
    "Exile of the Last Mughal Poet: Following his trial, 82-year-old Bahadur Shah Zafar was exiled to Rangoon, Burma, where he died in 1862 and was buried in an unmarked grave.",
    "Military Restructuring ('Martial Races'): Post-1857, the British drastically reduced recruitments from Awadh and Bengal, shifting to communities categorized under the colonial 'martial races' doctrine.",
    "Abolition of the Doctrine of Lapse: Queen Victoria's Proclamation of 1 November 1858 formally abandoned the Doctrine of Lapse, guaranteeing princely states the right to adopt heirs.",
    "Strategic Role of the Electric Telegraph: British commanders acknowledged that the recently installed electric telegraph line helped suppress the revolt by enabling rapid military intelligence coordination.",
    "Complex Historiography: Modern historians recognize that 1857 was neither a purely military mutiny nor a fully unified national revolution, but a complex, multi-layered anti-colonial struggle."
]

# -------------------------------------------------------------------
# 6. QUIZ QUESTIONS (15 Multiple-Choice Questions)
# -------------------------------------------------------------------
QUIZ_QUESTIONS = [
    {
        "question": "Which Governor-General introduced the controversial 'Doctrine of Lapse' that annexed Jhansi and Nagpur?",
        "option_a": "Lord Dalhousie",
        "option_b": "Lord Canning",
        "option_c": "Lord Wellesley",
        "option_d": "Lord Cornwallis",
        "correct_option": "A",
        "explanation": "Lord Dalhousie (1848–1856) implemented the Doctrine of Lapse, annexing states whose rulers died without a natural male heir."
    },
    {
        "question": "On what pretext did the British East India Company annex the wealthy kingdom of Awadh in 1856?",
        "option_a": "Doctrine of Lapse",
        "option_b": "Chronic Misgovernance",
        "option_c": "Non-payment of subsidiary tribute",
        "option_d": "Open rebellion against the Crown",
        "correct_option": "B",
        "explanation": "Awadh was annexed in February 1856 on charges of 'chronic misgovernance', exiling Nawab Wajid Ali Shah."
    },
    {
        "question": "On 29 March 1857, which sepoy of the 34th Bengal Native Infantry sparked the uprising at Barrackpore?",
        "option_a": "Tatya Tope",
        "option_b": "Mangal Pandey",
        "option_c": "Bakht Khan",
        "option_d": "Ishwar Pande",
        "correct_option": "B",
        "explanation": "Mangal Pandey openly rebelled against the greased cartridge at Barrackpore parade ground, calling on his comrades to resist."
    },
    {
        "question": "On which date did sepoys at the Meerut cantonment mutiny, break open prisons, and march to Delhi?",
        "option_a": "29 March 1857",
        "option_b": "10 May 1857",
        "option_c": "23 June 1857",
        "option_d": "15 August 1857",
        "correct_option": "B",
        "explanation": "On Sunday, 10 May 1857, Meerut sepoys revolted, liberated 85 imprisoned comrades, and marched overnight to Delhi."
    },
    {
        "question": "Whom did the insurgent sepoys proclaim as the symbolic Emperor of India upon reaching Delhi on 11 May 1857?",
        "option_a": "Nana Saheb",
        "option_b": "Bahadur Shah Zafar",
        "option_c": "Wajid Ali Shah",
        "option_d": "Birjis Qadr",
        "correct_option": "B",
        "explanation": "The 82-year-old Mughal poet-emperor Bahadur Shah Zafar was proclaimed Shahenshah-e-Hindustan (Emperor of India)."
    },
    {
        "question": "Who was the adopted son of Peshwa Baji Rao II who led the uprising in Kanpur after his pension was stopped?",
        "option_a": "Tatya Tope",
        "option_b": "Nana Saheb (Dhondu Pant)",
        "option_c": "Kanhoji Angre",
        "option_d": "Appa Saheb",
        "correct_option": "B",
        "explanation": "Nana Saheb led the uprising in Kanpur after the British government discontinued his father's annual pension."
    },
    {
        "question": "Which queen regent led the resistance in Awadh, crowning her minor son Birjis Qadr and defending Lucknow?",
        "option_a": "Rani Lakshmibai",
        "option_b": "Begum Hazrat Mahal",
        "option_c": "Rani Avantibai",
        "option_d": "Kasturba Gandhi",
        "correct_option": "B",
        "explanation": "Begum Hazrat Mahal rallied Hindu and Muslim taluqdars in Awadh, crowning Birjis Qadr and holding the Lucknow Residency under siege."
    },
    {
        "question": "Which 80-year-old chieftain of Jagdishpur, Bihar, severed his own wounded hand in the Ganga and died undefeated?",
        "option_a": "Tatya Tope",
        "option_b": "Veer Kunwar Singh",
        "option_c": "Amar Singh",
        "option_d": "Maulvi Ahmadullah Shah",
        "correct_option": "B",
        "explanation": "Veer Kunwar Singh of Jagdishpur led armed resistance across Bihar and eastern UP, defeating British forces until his death in 1858."
    },
    {
        "question": "What was the famous declaration made by Rani Lakshmibai upon hearing of Dalhousie's annexation order for Jhansi?",
        "option_a": "Inquilab Zindabad",
        "option_b": "Meri Jhansi nahi doongi!",
        "option_c": "Jai Hind",
        "option_d": "Swaraj is my birthright",
        "correct_option": "B",
        "explanation": "Rani Lakshmibai famously asserted: 'Meri Jhansi nahi doongi!' (I shall not surrender my Jhansi!)."
    },
    {
        "question": "What was Rani Lakshmibai's birth name before her marriage to Maharaja Gangadhar Rao of Jhansi?",
        "option_a": "Manikarnika Tambe",
        "option_b": "Ahilyabai Holkar",
        "option_c": "Tarabai Bhosale",
        "option_d": "Rani Chennamma",
        "correct_option": "A",
        "explanation": "She was born Manikarnika (Manu) Tambe in Varanasi and was raised in the Bithoor household of the exiled Peshwa."
    },
    {
        "question": "Which military commander led an elusive year-long guerrilla campaign across Central India and Bundelkhand?",
        "option_a": "Bakht Khan",
        "option_b": "Tatya Tope",
        "option_c": "Mangal Pandey",
        "option_d": "Kunwar Singh",
        "correct_option": "B",
        "explanation": "Tatya Tope coordinated operations across thousands of miles, eluding multiple British armies until betrayed in April 1859."
    },
    {
        "question": "Which rifle model's greased cartridge triggered widespread religious panic among Hindu and Muslim sepoys in early 1857?",
        "option_a": "Brown Bess Flintlock",
        "option_b": "Enfield Pattern 1853",
        "option_c": "Lee-Enfield .303",
        "option_d": "Martini-Henry",
        "correct_option": "B",
        "explanation": "The Enfield Pattern 1853 rifled musket used paper cartridges greased with animal tallow that soldiers had to bite open."
    },
    {
        "question": "Which British general led the Central India Field Force and praised Rani Lakshmibai as 'the bravest and best among the rebels'?",
        "option_a": "General James Neill",
        "option_b": "Major-General Sir Hugh Rose",
        "option_c": "Colin Campbell",
        "option_d": "Henry Havelock",
        "correct_option": "B",
        "explanation": "Sir Hugh Rose commanded British forces at Jhansi and Gwalior, paying tribute to Rani Lakshmibai in his post-battle dispatch."
    },
    {
        "question": "Which British parliamentary act formally dissolved the East India Company and transferred rule to the British Crown in 1858?",
        "option_a": "Pitt's India Act",
        "option_b": "Government of India Act 1858",
        "option_c": "Regulating Act of 1773",
        "option_d": "Charter Act of 1833",
        "correct_option": "B",
        "explanation": "The Government of India Act 1858 liquidated the East India Company and placed India under direct administration of the Crown."
    },
    {
        "question": "To which city was the last Mughal Emperor, Bahadur Shah Zafar, exiled following the suppression of the 1857 uprising?",
        "option_a": "London",
        "option_b": "Rangoon (Yangon, Burma)",
        "option_c": "Port Blair (Andaman Islands)",
        "option_d": "Colombo (Ceylon)",
        "correct_option": "B",
        "explanation": "Bahadur Shah Zafar was exiled to Rangoon, Burma, where he died in 1862 and was buried in an unmarked grave."
    }
]


# -------------------------------------------------------------------
# DATABASE SEEDING FUNCTION
# -------------------------------------------------------------------
def load_revolt1857_data():
    """
    Inserts the complete historical dataset for the Revolt of 1857
    into the SQLite database without modifying previous datasets.
    """
    # Ensure tables exist
    database.create_tables()

    # Check if Revolt 1857 topic already exists
    topics = database.get_topics()
    topic_id = None
    for t in topics:
        if "1857" in t["title"]:
            topic_id = t["id"]
            break

    # If topic does not exist, add it
    if topic_id is None:
        topic_id = database.add_topic(
            title="The Revolt of 1857",
            period="1857 - 1858 CE",
            summary=(
                "India's First War of Independence uniting soldiers, dispossessed monarchs, and peasants, "
                "permanently ending East India Company rule."
            )
        )
        print(f"[OK] Created topic: The Revolt of 1857 (Topic ID: {topic_id})")
    else:
        print(f"[OK] Found existing topic: The Revolt of 1857 (Topic ID: {topic_id})")

    # Clear old data for 1857 only, preserving other topics completely
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
    print(f"[OK] Inserted {len(CHAPTERS)} chapters for the Revolt of 1857.")

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

    print(f"\n[SUCCESS] The Revolt of 1857 dataset loaded into database successfully!")
    return topic_id


if __name__ == "__main__":
    print("Loading The Revolt of 1857 dataset into SQLite database...")
    load_revolt1857_data()
