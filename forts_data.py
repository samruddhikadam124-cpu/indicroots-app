"""
forts_data.py - Historical Forts Dataset for IndicRoots
Contains curated historical records, coordinates, construction periods,
histories, and key events for 20 iconic Indian forts.
"""

import sys
import os

# Ensure workspace root is in sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import database

FORTS_DATA = [
    # -------------------------------------------------------------
    # MAHARASHTRA FORTS (12 Forts)
    # -------------------------------------------------------------
    {
        "name": "Raigad Fort",
        "location": "Mahad, Raigad District",
        "state": "Maharashtra",
        "latitude": 18.2346,
        "longitude": 73.4414,
        "built_or_established": "Originally known as Rairi under the More family of Jawali; extensively fortified and transformed by Chhatrapati Shivaji Maharaj from 1656 onwards.",
        "history": (
            "Perched atop a rugged wedge-shaped plateau in the Sahyadri mountains at an altitude of 820 meters above sea level, "
            "Raigad was selected by Chhatrapati Shivaji Maharaj as the capital of the nascent sovereign Maratha state (Hindavi Swarajya). "
            "Surrounded by sheer scarps plunging over 700 meters into deep valley gorges, Raigad was engineered by chief architect "
            "Hiroji Indulkar to be virtually impregnable, featuring grand royal palaces, the public assembly court (Raj Sabha), "
            "a market boulevard, and sacred water reservoirs such as Ganga Sagar."
        ),
        "important_events": (
            "1. Grand Coronation (Rajyabhisheka) of Chhatrapati Shivaji Maharaj on 6 June 1674, formalizing Hindavi Swarajya.\n"
            "2. Passing of Chhatrapati Shivaji Maharaj on 3 April 1680 and erection of his sacred Samadhi.\n"
            "3. Coronation of Chhatrapati Sambhaji Maharaj in January 1681.\n"
            "4. Heroic resistance against the prolonged Mughal siege led by Zulfiqar Khan in 1689."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Raigad_Fort_Panorama.jpg/800px-Raigad_Fort_Panorama.jpg"
    },
    {
        "name": "Shivneri Fort",
        "location": "Junnar, Pune District",
        "state": "Maharashtra",
        "latitude": 19.1983,
        "longitude": 73.8617,
        "built_or_established": "Fortified since the 1st millennium CE under the Satavahana era; held successively by the Yadavas, Bahmanis, and Ahmadnagar Nizamshahi.",
        "history": (
            "Shivneri is a triangular hill fortress near Junnar, celebrated throughout Indian history as the birthplace of Chhatrapati Shivaji Maharaj. "
            "Guarded by seven successive concentric fortified gateways (including Maha Darwaza, Pir Darwaza, and Hathi Darwaza), the fort "
            "contains ancient rock-cut Buddhist and Brahmanical caves, freshwater cisterns named Ganga and Jamuna, and the shrine of Goddess Shivai Devi, "
            "after whom Rajmata Jijabai named her newborn son."
        ),
        "important_events": (
            "1. Birth of Chhatrapati Shivaji Maharaj on 19 February 1630.\n"
            "2. Formative childhood sanctuary where young Shivaji received early cultural and ethical guidance from Rajmata Jijabai.\n"
            "3. Crucial military bastion contested between Ahmadnagar, Bijapur, the Mughals, and Maratha forces throughout the 17th century."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Shivneri_fort_main_entrance.jpg/800px-Shivneri_fort_main_entrance.jpg"
    },
    {
        "name": "Pratapgad Fort",
        "location": "Mahabaleshwar, Satara District",
        "state": "Maharashtra",
        "latitude": 17.9351,
        "longitude": 73.5794,
        "built_or_established": "Commissioned by Chhatrapati Shivaji Maharaj and completed in 1656 under the supervision of Prime Minister Moropant Trimbak Pingle.",
        "history": (
            "Constructed atop a prominent spur 1,080 meters above sea level to command the dense Jawali forests and the strategic passes connecting "
            "the Deccan tableland with coastal Konkan. The fortress is divided into two distinct zones: the Upper Fort built on the crest "
            "of the hill containing the royal court and temple of Bhavani Mata, and the Lower Fort protected by formidable bastions and double ramparts."
        ),
        "important_events": (
            "1. Epic Battle of Pratapgad on 10 November 1659, where Shivaji Maharaj neutralized the mighty Adilshahi general Afzal Khan in a legendary personal encounter.\n"
            "2. Decisive routing of the invading Bijapuri army in the surrounding dense foothills, securing the Maratha kingdom's southern frontier.\n"
            "3. Consecration of the historic Bhavani Temple with an idol sculpted from Gandaki stone brought from Nepal."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Pratapgad_Fort_overview.jpg/800px-Pratapgad_Fort_overview.jpg"
    },
    {
        "name": "Sinhagad Fort",
        "location": "Haveli Taluka, Pune District",
        "state": "Maharashtra",
        "latitude": 18.3663,
        "longitude": 73.7558,
        "built_or_established": "Ancient stronghold known anciently as Kondhana; documented history dates back over two millennia, later fortified under the Rashtrakutas, Yadavas, and Bahmanis.",
        "history": (
            "Perched on an isolated cliff of the Bhuleshwar range rising 1,312 meters above sea level, Sinhagad ('The Lion's Fort') commanded "
            "all major trade routes connecting Pune with the Sahyadri passes. Characterized by almost vertical basalt escarpments, its natural "
            "defenses were reinforced with strategic bastions and two main gateways: the Kalyan Darwaza facing south and the Pune Darwaza facing north."
        ),
        "important_events": (
            "1. Daring midnight assault in February 1670 led by Subedar Tanaji Malusare, who scaled the precipitous cliff with his Mavala warriors.\n"
            "2. Fierce duel in which Tanaji Malusare defeated the Mughal garrison commander Udaybhan Rathod before succumbing to mortal wounds, prompting Shivaji's famous lament: 'Gad aala, pan sinh gela' ('The fort is won, but the lion is lost').\n"
            "3. Renaming of the fort from Kondhana to Sinhagad in honour of Tanaji's sacrifice."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sinhagad_Fort_Pune.jpg/800px-Sinhagad_Fort_Pune.jpg"
    },
    {
        "name": "Rajgad Fort",
        "location": "Bhor Taluka, Pune District",
        "state": "Maharashtra",
        "latitude": 18.2464,
        "longitude": 73.6828,
        "built_or_established": "Originally known as Murumbdev; extensively reconstructed, fortified, and crowned as the primary capital by Chhatrapati Shivaji Maharaj from 1647.",
        "history": (
            "Rising to 1,376 meters, Rajgad ('King of Forts') served as the principal capital of Chhatrapati Shivaji Maharaj for over twenty-five "
            "consecutive years before the administration transitioned to Raigad. The fortress features three sprawling, heavily fortified spurs "
            "(machees)—Padmavati Machi, Suvela Machi, and Sanjivani Machi—radiating from the central high citadel (Bale Killa)."
        ),
        "important_events": (
            "1. Center of Maratha governance and strategic planning from 1647 to 1672.\n"
            "2. Birth of Rajaram Maharaj in 1670.\n"
            "3. Safe sanctuary to which Shivaji Maharaj returned following his audacious escape from Mughal custody in Agra in 1666.\n"
            "4. Resting place of Maharani Saibai's memorial monument on Padmavati Machi."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Rajgad_Fort_Bale_Killa.jpg/800px-Rajgad_Fort_Bale_Killa.jpg"
    },
    {
        "name": "Torna Fort",
        "location": "Velhe Taluka, Pune District",
        "state": "Maharashtra",
        "latitude": 18.2764,
        "longitude": 73.6231,
        "built_or_established": "Built in the 13th century by followers of the Shiva Menghai sect; captured by young Shivaji in 1646.",
        "history": (
            "Torna, also revered as 'Prachandgad' ('The Colossal Fort') due to its immense perimeter and soaring elevation of 1,403 meters, "
            "is the highest hill fort in Pune district. Its sweeping defensive spurs, Budhla Machi and Zunjar Machi, feature razor-sharp ridges "
            "overlooking yawning precipices that offered unmatched observation across the surrounding valleys."
        ),
        "important_events": (
            "1. First fort captured by the 16-year-old Shivaji in 1646, marking the founding spark of Hindavi Swarajya.\n"
            "2. Discovery of concealed treasure pots during restoration, the entire proceeds of which were reinvested to construct Rajgad Fort.\n"
            "3. Historic theater of multiple sieges during the 27-year Maratha War of Independence against Aurangzeb."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Torna_Fort_Ridge.jpg/800px-Torna_Fort_Ridge.jpg"
    },
    {
        "name": "Purandar Fort",
        "location": "Saswad, Pune District",
        "state": "Maharashtra",
        "latitude": 18.2789,
        "longitude": 73.9794,
        "built_or_established": "Origins trace to the 11th century Yadava dynasty; developed and fortified under the Bahmanis, Nizamshahi, and Marathas.",
        "history": (
            "Purandar is a dramatic twin-fort fortress complex consisting of Purandar (the upper and lower levels) and Vajragad (Rudra Mahal), "
            "rising 1,387 meters into the sky. It served as a premier defensive bastion and royal retreat for the Marathas, controlling access "
            "from the plains into the Sahyadri heartland."
        ),
        "important_events": (
            "1. Birth of the second Maratha Chhatrapati, Sambhaji Maharaj, on 14 May 1657.\n"
            "2. Epic siege in 1665 by Mughal commander Diler Khan and the legendary last stand of fort commander Murarbaji Deshpande.\n"
            "3. Negotiation and signing of the historic Treaty of Purandar (June 1665) between Shivaji Maharaj and Mirza Raja Jai Singh."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Purandar_fort_view.jpg/800px-Purandar_fort_view.jpg"
    },
    {
        "name": "Panhala Fort",
        "location": "Panhala, Kolhapur District",
        "state": "Maharashtra",
        "latitude": 16.8122,
        "longitude": 74.1136,
        "built_or_established": "Constructed between 1178 and 1209 CE by the Shilahara monarch Bhoja II; later fortified by the Bahmanis, Adilshahi, and Marathas.",
        "history": (
            "Strategically commanding a vital mountain pass linking the Deccan plateau to the ports of the Konkan coast, Panhala boasts a circumference "
            "of over 14 kilometers with monumental defensive architecture, including the massive triple gate (Teen Darwaza), the granaries of "
            "Ambarkhana, and the Sajja Kothi pavilion."
        ),
        "important_events": (
            "1. Five-month siege of Panhala by Siddi Jauhar in 1660, culminating in Shivaji Maharaj's midnight escape to Vishalgad through torrential monsoon rain.\n"
            "2. Legendary rearguard sacrifice of Baji Prabhu Deshpande and Mavala warriors at Ghodkhind (Pawan Khind) holding off Bijapuri pursuers.\n"
            "3. Center of administration and royal residence for the Kolhapur branch of the Maratha Empire under Maharani Tarabai."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Panhala_Fort_Teen_Darwaza.jpg/800px-Panhala_Fort_Teen_Darwaza.jpg"
    },
    {
        "name": "Sindhudurg Fort",
        "location": "Malvan Coast, Sindhudurg District",
        "state": "Maharashtra",
        "latitude": 16.0425,
        "longitude": 73.4608,
        "built_or_established": "Commissioned by Chhatrapati Shivaji Maharaj in 1664; designed by master architect Hiroji Indulkar and completed in 1667.",
        "history": (
            "Constructed on a rocky islet (Kurte Island) half a kilometer off the Malvan coast, Sindhudurg stands as one of India's most extraordinary "
            "naval fortresses. Built to defend the coast against foreign sea powers (Portuguese, British, and the Siddis of Janjira), its 3-kilometer-long "
            "ramparts required over 70,000 kilograms of molten lead poured into stone foundations to withstand pounding Arabian Sea tides."
        ),
        "important_events": (
            "1. Commissioned as the premier ocean bastion and dockyard of the nascent Maratha Royal Navy.\n"
            "2. Preserves the sacred impressions of Chhatrapati Shivaji Maharaj's foot and hand preserved in lime plaster.\n"
            "3. Houses the Shri Shivrajeshwar Temple, dedicated to Shivaji Maharaj and built by his son Chhatrapati Rajaram in 1695."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Sindhudurg_Fort_aerial.jpg/800px-Sindhudurg_Fort_aerial.jpg"
    },
    {
        "name": "Vijaydurg Fort",
        "location": "Devgad Taluka, Sindhudurg District",
        "state": "Maharashtra",
        "latitude": 16.5592,
        "longitude": 73.3344,
        "built_or_established": "Originally constructed in 1205 CE by Shilahara ruler Bhoja II; extensively expanded, triple-walled, and fortified by Shivaji Maharaj in 1653.",
        "history": (
            "Known as the 'Gibraltar of the East', Vijaydurg ('Victory Fort') occupies a narrow promontory at the mouth of the Vaghotan estuary. "
            "Surrounded by water on three sides, it features a unique underwater masonry barrier constructed across the estuary mouth that "
            "damaged and grounded enemy ships with deeper drafts attempting to approach the fort."
        ),
        "important_events": (
            "1. Prime naval dockyard and headquarters of the Maratha Navy under Grand Admiral Kanhoji Angre.\n"
            "2. Repelled joint British and Portuguese naval bombardments throughout the early 18th century without capitulating.\n"
            "3. Historic observation site of the 1868 solar eclipse by British astronomer Norman Lockyer, during which the element helium was first discovered."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Vijaydurg_Fort_Ramparts.jpg/800px-Vijaydurg_Fort_Ramparts.jpg"
    },
    {
        "name": "Lohagad Fort",
        "location": "Maval, Pune District",
        "state": "Maharashtra",
        "latitude": 18.7042,
        "longitude": 73.4775,
        "built_or_established": "Occupied since the Satavahana era; fortified across the Chalukya, Rashtrakuta, Yadava, and Bahmani eras; secured by Shivaji Maharaj in 1648.",
        "history": (
            "Perched at 1,033 meters, Lohagad ('Iron Fort') is an imposing hill bastion commanding the ancient trade route between the Konkan ports "
            "and the Deccan plateau through the Bhor Ghat pass. Renowned for its distinctive western promontory, the Vinchu Kata ('Scorpion's Tail'), "
            "which extends for 1,500 meters like a natural fortified bastion into the valley."
        ),
        "important_events": (
            "1. Captured by Shivaji Maharaj in 1648 and utilized to house the Maratha state treasury.\n"
            "2. Extensive architectural renovations by Peshwa statesman Nana Phadnavis in the late 18th century, who constructed its four imposing gateways (Ganesh, Narayan, Hanuman, and Maha Darwaza).\n"
            "3. Strategically paired with the adjacent fort of Visapur to safeguard the Western Ghat passes."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Lohagad_Fort_Vinchu_Kata.jpg/800px-Lohagad_Fort_Vinchu_Kata.jpg"
    },
    {
        "name": "Murud-Janjira Fort",
        "location": "Murud, Raigad District",
        "state": "Maharashtra",
        "latitude": 18.3006,
        "longitude": 72.9644,
        "built_or_established": "Originally established as a wooden stockade by Koli fishermen in the 15th century; transformed into an impregnable stone marine fortress by the Siddis in the 16th century.",
        "history": (
            "Situated on an oval rock island in the Arabian Sea off the coast of Murud, Janjira (derived from Arabic 'Jazeera' meaning island) "
            "is renowned as one of the most formidable marine citadels in world history. Featuring 19 round stone bastions and curtain walls rising "
            "directly from the seawater, the fort contained palaces, residential quarters, mosques, and two large freshwater lakes inside its saltwater perimeter."
        ),
        "important_events": (
            "1. Famous for never being conquered in its 350-year history despite repeated sieges by the Marathas, Portuguese, and British.\n"
            "2. Subject of legendary siege campaigns by Chhatrapati Shivaji Maharaj and Chhatrapati Sambhaji Maharaj (who attempted to build a stone causeway across the sea to storm it).\n"
            "3. Houses historic third-largest cannon in India, Kalal Bangadi, made of five metals."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Murud_Janjira_sea_fort.jpg/800px-Murud_Janjira_sea_fort.jpg"
    },

    # -------------------------------------------------------------
    # OTHER PROMINENT INDIAN FORTS (8 Forts across India)
    # -------------------------------------------------------------
    {
        "name": "Red Fort",
        "location": "Old Delhi",
        "state": "Delhi",
        "latitude": 28.6562,
        "longitude": 77.2410,
        "built_or_established": "Commissioned by Mughal Emperor Shah Jahan in 1638 and completed in 1648 under the architectural supervision of Ustad Ahmad Lahori.",
        "history": (
            "Constructed of red sandstone on the banks of the Yamuna River as the grand fortified palace of the new imperial capital Shahjahanabad. "
            "The UNESCO World Heritage Site covers 254 acres and features octagonal layout geometry, Diwan-i-Aam (Hall of Public Audience), "
            "Diwan-i-Khas (Hall of Private Audience where the Peacock Throne once stood), and the monumental Lahori and Delhi Gates."
        ),
        "important_events": (
            "1. Sacked by Nadir Shah of Persia in 1739, who carried off the Peacock Throne and Koh-i-Noor diamond.\n"
            "2. Epicenter of the Revolt of 1857 when mutinous sepoys entered Delhi and declared Bahadur Shah Zafar as the Emperor of Hindustan.\n"
            "3. Venue of the historic Indian National Army (INA) Red Fort trials in 1945–1946.\n"
            "4. Site of the Prime Minister's national flag address every year on Independence Day since 15 August 1947."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Red_Fort_in_Delhi_03-2016_img3.jpg/800px-Red_Fort_in_Delhi_03-2016_img3.jpg"
    },
    {
        "name": "Agra Fort",
        "location": "Agra",
        "state": "Uttar Pradesh",
        "latitude": 27.1795,
        "longitude": 78.0211,
        "built_or_established": "Ancient brick citadel known as Badalgarh; completely rebuilt in red sandstone by Mughal Emperor Akbar from 1565 to 1573.",
        "history": (
            "A crescent-shaped walled fortress enclosing 94 acres alongside the Yamuna River, Agra Fort was the premier seat of imperial power "
            "for four generations of Mughal rulers (Akbar, Jahangir, Shah Jahan, and Aurangzeb). The UNESCO World Heritage Site showcases an architectural "
            "transition from Akbar's red sandstone synthesis of Hindu-Islamic motifs to Shah Jahan's ornate white marble pavilions."
        ),
        "important_events": (
            "1. Historic confrontation in May 1666 when Chhatrapati Shivaji Maharaj stood defiantly in Aurangzeb's royal court before making his daring escape.\n"
            "2. Confinement of Emperor Shah Jahan by his son Aurangzeb in the Muasamman Burj pavilion overlooking the Taj Mahal (1658–1666).\n"
            "3. Intense military operations and defense of European civilians during the Revolt of 1857."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Agra_Fort_Delhi_Gate.jpg/800px-Agra_Fort_Delhi_Gate.jpg"
    },
    {
        "name": "Gwalior Fort",
        "location": "Gwalior",
        "state": "Madhya Pradesh",
        "latitude": 26.2295,
        "longitude": 78.1692,
        "built_or_established": "Founded in the 6th-8th century CE; principal palace fortifications built under Tomar ruler Raja Man Singh Tomar (1486–1516).",
        "history": (
            "Praised by Mughal Emperor Babur as 'the pearl among gems of the fortresses of Hind', Gwalior Fort occupies a steep isolated sandstone "
            "hillock rising 100 meters above the plains. It is renowned for the Man Mandir Palace with its turquoise and yellow glazed ceramic tilework "
            "depicting ducks, elephants, and peacocks, alongside towering rock-cut Tirthankara statues chiseled along its cliff faces."
        ),
        "important_events": (
            "1. Seat of the Tomar dynasty, Delhi Sultanate, Mughals, and Scindia Maratha dynasty.\n"
            "2. Focal point during the Revolt of 1857, where Rani Lakshmibai of Jhansi and Tatya Tope captured the fort in June 1858.\n"
            "3. Site of the decisive Battle of Kotah-ki-Serai near the fort where Rani Lakshmibai attained martyrdom fighting British forces."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Gwalior_Fort_Man_Mandir_Palace.jpg/800px-Gwalior_Fort_Man_Mandir_Palace.jpg"
    },
    {
        "name": "Chittorgarh Fort",
        "location": "Chittorgarh, Mewar Region",
        "state": "Rajasthan",
        "latitude": 24.8879,
        "longitude": 74.6451,
        "built_or_established": "Built by the Maurya rulers in the 7th century CE; developed as the premier capital of the Sisodia Rajput rulers of Mewar.",
        "history": (
            "The largest fort complex in India, Chittorgarh covers nearly 700 acres atop an elevated 180-meter plateau. It incorporates 84 ancient "
            "water reservoirs, seven fortified gates, the 9-storey Vijay Stambha (Tower of Victory built by Rana Kumbha in 1448), and the Kirti Stambha. "
            "It is recognized as a UNESCO World Heritage Site for its monumental Rajput chivalric architecture."
        ),
        "important_events": (
            "1. First famous siege by Alauddin Khalji in 1303, culminating in the heroic defense by Rana Ratan Singh and Jauhar led by Rani Padmini.\n"
            "2. Second siege by Sultan Bahadur Shah of Gujarat in 1535, marked by the sacrifice of Rani Karnavati.\n"
            "3. Third monumental siege by Emperor Akbar in 1567–1568, defended heroically by Jaimal Rathore and Patta Chundawat."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Chittorgarh_Fort_Tower_of_Victory.jpg/800px-Chittorgarh_Fort_Tower_of_Victory.jpg"
    },
    {
        "name": "Mehrangarh Fort",
        "location": "Jodhpur",
        "state": "Rajasthan",
        "latitude": 26.2978,
        "longitude": 73.0185,
        "built_or_established": "Founded in 1459 CE by Rao Jodha, ruler of the Rathore clan and founder of Jodhpur.",
        "history": (
            "Rising 125 meters above the surrounding 'Blue City' on a sheer rocky ridge known as Bhakurcheeria, Mehrangarh ('Citadel of the Sun') "
            "features massive defensive walls up to 36 meters high and 21 meters wide. It contains opulent palaces with exquisite sandstone tracery, "
            "including Sheesh Mahal, Phool Mahal, and Moti Mahal, alongside an internationally acclaimed museum of royal artefacts and artillery."
        ),
        "important_events": (
            "1. Capital and seat of the Rathore rulers of Marwar for over five centuries.\n"
            "2. Successfully withstood repeated artillery sieges by invading Jaipur and Maratha armies, with cannonball battle scars preserved at the Dedh Kamgra Gate.\n"
            "3. Preserves historic handprints of royal women commemorated at the Loha Pol gate before performing Sati."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Mehrangarh_Fort_Jodhpur_Rajasthan.jpg/800px-Mehrangarh_Fort_Jodhpur_Rajasthan.jpg"
    },
    {
        "name": "Golconda Fort",
        "location": "Hyderabad",
        "state": "Telangana",
        "latitude": 17.3833,
        "longitude": 78.4011,
        "built_or_established": "Originally constructed of mud in the 11th century under the Kakatiya dynasty; rebuilt and fortified in granite by the Qutb Shahi kings (1518–1687).",
        "history": (
            "A sprawling citadel consisting of four distinct forts enclosed by an 11-kilometer outer wall with 87 semi-circular bastions. "
            "Renowned worldwide for its acoustic engineering (a single handclap beneath the Fateh Darwaza dome echoes distinctly to the highest pavilion "
            "of Bala Hissar a kilometer away) and its historic diamond vault which controlled trade in the famed Golconda mines."
        ),
        "important_events": (
            "1. Global source and trading vault for world-famous diamonds including the Koh-i-Noor, Hope Diamond, and Daria-i-Noor.\n"
            "2. Historic diplomatic alliance forged here in 1677 between Chhatrapati Shivaji Maharaj and Sultan Abul Hasan Qutb Shah.\n"
            "3. Heroic eight-month resistance in 1687 against the imperial army of Aurangzeb, which fell only due to bribery of an inner gatekeeper."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Golconda_Fort_Hyderabad_overview.jpg/800px-Golconda_Fort_Hyderabad_overview.jpg"
    },
    {
        "name": "Bidar Fort",
        "location": "Bidar",
        "state": "Karnataka",
        "latitude": 17.9231,
        "longitude": 77.5256,
        "built_or_established": "Ancient fort rebuilt and transformed into a grand royal capital by Sultan Ahmad Shah Bahmani in 1428 CE.",
        "history": (
            "Renowned for its ingenious defensive design, Bidar Fort is protected by a triple-tiered moat chiseled directly out of solid red laterite rock. "
            "Enclosed within its 5.5-kilometer perimeter are royal monuments including the Persian-style Rangeen Mahal with mother-of-pearl inlay work, "
            "Tarkash Mahal, Gagan Mahal, and the subterranean Karez water supply engineering system utilizing gravity-fed aquifers."
        ),
        "important_events": (
            "1. Capital of the Bahmani Sultanate and subsequent Barid Shahi dynasty during the golden age of Deccan architecture.\n"
            "2. Historic construction of the Mahmud Gawan Madrasa in 1472, attracting scholars from across Asia.\n"
            "3. Conquered by Aurangzeb in 1656 after a rigorous 27-day artillery bombardment, marking Mughal expansion into northern Karnataka."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Bidar_Fort_Walls_and_Moat.jpg/800px-Bidar_Fort_Walls_and_Moat.jpg"
    },
    {
        "name": "Daulatabad Fort",
        "location": "Daulatabad, Chhatrapati Sambhajinagar District",
        "state": "Maharashtra",
        "latitude": 19.9427,
        "longitude": 75.2132,
        "built_or_established": "Founded in 1187 CE by Yadava king Bhillama V as Devagiri; later renamed and modified under the Delhi Sultanate, Bahmanis, and Nizamshahi.",
        "history": (
            "Considered one of the most impregnable medieval hill fortresses in the world, Daulatabad ('City of Fortune') was constructed on a conical "
            "hill 200 meters high. The lower perimeter was artificially scarped into a vertical 50-meter drop surrounded by a deep moat filled with crocodiles, "
            "accessible only via a drawbridge leading into the 'Andhari'—a pitch-black subterranean maze designed to trap and eliminate invaders."
        ),
        "important_events": (
            "1. Sultan Muhammad bin Tughlaq ordered the historic and tragic transfer of the Delhi Sultanate's entire capital and population here in 1327.\n"
            "2. Center of military resistance organized by military genius Malik Ambar in the early 17th century.\n"
            "3. Houses the 64-meter-tall Chand Minar minaret erected by Alauddin Bahmani in 1445."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Daulatabad_Fort_Devagiri.jpg/800px-Daulatabad_Fort_Devagiri.jpg"
    }
]


def load_forts_data():
    """
    Loads all 20 historical forts into the SQLite database.
    Idempotent: Clears or checks existing records to prevent duplicates when executed multiple times.
    """
    database.init_db()
    conn = database.get_connection()
    cursor = conn.cursor()

    print("[INFO] Loading Forts dataset into SQLite database...")

    # Clear existing forts table data to guarantee 0 duplicates
    cursor.execute("DELETE FROM forts")
    conn.commit()
    conn.close()

    inserted_count = 0
    for fort in FORTS_DATA:
        database.add_fort(
            name=fort["name"],
            location=fort["location"],
            state=fort["state"],
            latitude=fort["latitude"],
            longitude=fort["longitude"],
            history=fort["history"],
            important_events=fort["important_events"],
            built_or_established=fort["built_or_established"],
            image_url=fort["image_url"]
        )
        inserted_count += 1

    print(f"[SUCCESS] Successfully inserted {inserted_count} historical forts into SQLite database!")
    return inserted_count


if __name__ == "__main__":
    count = load_forts_data()
    print(f"Total forts currently in database: {count}")
