"""
app.py - Main Entry Point & Home Dashboard for IndicRoots
A polished, college-level educational web application and digital archive
for Indian history and heritage.
"""

import os
import streamlit as st
import database
import ui_theme

# -------------------------------------------------------------
# 1. PAGE CONFIGURATION & HERITAGE STYLING
# -------------------------------------------------------------
st.set_page_config(
    page_title="IndicRoots — Indian History & Heritage",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ensure database tables and starter data exist
database.init_db()

# Apply the unified IndicRoots heritage design system
ui_theme.inject_heritage_css()

# Render distinctive grouped sidebar navigation
ui_theme.render_sidebar(active_page="home")


# -------------------------------------------------------------
# 2. HOME PAGE HERO SECTION
# -------------------------------------------------------------
hero_banner_path = os.path.join(os.path.dirname(__file__), "assets", "images", "hero", "hero_banner.jpg")

hero_col_left, hero_col_right = st.columns([1.1, 1], gap="medium")

with hero_col_left:
    st.markdown("""
    <div class="hero-container" style="height: 100%; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: 0.85rem; font-weight: 700; color: var(--color-gold); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 0.4rem;">
            ✦ Digital Heritage Archive ✦
        </div>
        <div class="hero-title-main">🪷 IndicRoots</div>
        <div class="hero-subtitle-main">Discover India's History, Knowledge & Heritage</div>
        <div class="hero-description">
            Journey through millennia of civilizational brilliance, legendary leaders, ancient architectural marvels, and monumental historical turning points. From the planned urban avenues of the Harappan era to the formidable Maratha hill fortresses and the 1857 war of independence.
        </div>
        <div style="margin-top: 1.2rem; display: flex; gap: 0.6rem; flex-wrap: wrap;">
            <span style="background-color: #EFE3D0; color: #7E2F1B; font-size: 0.8rem; font-weight: 700; padding: 4px 10px; border-radius: 4px; border: 1px solid #D8C7B0;">🏛️ 4 Major Historical Eras</span>
            <span style="background-color: #EFE3D0; color: #7E2F1B; font-size: 0.8rem; font-weight: 700; padding: 4px 10px; border-radius: 4px; border: 1px solid #D8C7B0;">📖 40 Study Chapters</span>
            <span style="background-color: #EFE3D0; color: #7E2F1B; font-size: 0.8rem; font-weight: 700; padding: 4px 10px; border-radius: 4px; border: 1px solid #D8C7B0;">🏰 20 Interactive Forts</span>
            <span style="background-color: #EFE3D0; color: #7E2F1B; font-size: 0.8rem; font-weight: 700; padding: 4px 10px; border-radius: 4px; border: 1px solid #D8C7B0;">🧠 60 Quiz Questions</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with hero_col_right:
    if os.path.exists(hero_banner_path):
        st.image(
            hero_banner_path,
            caption="Ancient Indian Fortresses, Architecture & Civilizational Heritage",
            use_container_width=True
        )
    else:
        st.markdown("""
        <div style="height: 100%; min-height: 260px; background-color: #EADFCF; border: 2px dashed #CBB99F; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #6E5D4F; font-size: 1.1rem; font-weight: 600;">
            📜 Ancient Indian Fortresses & Heritage Panorama
        </div>
        """, unsafe_allow_html=True)

# Subtle decorative heritage divider
ui_theme.render_heritage_divider()


# -------------------------------------------------------------
# 3. SEARCH BAR
# -------------------------------------------------------------
st.markdown("""
<div style="margin-bottom: 0.3rem;">
    <span style="font-size: 1.05rem; font-weight: 700; color: var(--color-deep-brown);">🔍 Search IndicRoots Archive</span>
    <span style="font-size: 0.84rem; color: var(--color-muted); margin-left: 0.5rem;">Explore topics, chapters, and historical records</span>
</div>
""", unsafe_allow_html=True)

search_query = st.text_input(
    label="Search IndicRoots Archive",
    placeholder="Type a historical person, place, battle, fort, or event (e.g. Shivaji, Great Bath, Raigad, Mangal Pandey)...",
    label_visibility="collapsed",
    key="home_search_input"
)

# Search Results Display (Preserves original search logic)
if search_query and search_query.strip():
    results = database.search_content(search_query.strip())
    total_hits = len(results["topics"]) + len(results["chapters"]) + len(results["facts"])

    if total_hits == 0:
        st.info("No matching records found. Try searching with a broader keyword (e.g., 'fort', 'battle', 'temple', 'emperor').")
    else:
        st.markdown(f"#### 📜 Archive Search Results for *\"{search_query.strip()}\"* ({total_hits} found)")

        # Matching Topics
        if results["topics"]:
            st.markdown("##### 🏛️ Historical Topics")
            for t in results["topics"]:
                st.markdown(f"""
                <div style="background-color: var(--color-cream); border: 1px solid var(--color-border); border-left: 4px solid var(--color-terracotta); border-radius: 6px; padding: 0.75rem 1rem; margin-bottom: 0.5rem;">
                    <strong>{t['title']}</strong> <span style="color: var(--color-muted); font-size: 0.85rem;">({t['period']})</span><br>
                    <span style="font-size: 0.92rem; color: var(--color-text);">{t['summary']}</span>
                </div>
                """, unsafe_allow_html=True)

        # Matching Chapters
        if results["chapters"]:
            st.markdown("##### 📖 Study Chapters")
            for c in results["chapters"]:
                with st.expander(f"Chapter {c['chapter_number']}: {c['title']} — ({c['topic_title']})"):
                    preview = c["content"][:380] + "..." if len(c["content"]) > 380 else c["content"]
                    st.write(preview)
                    if st.button("Read Full Chapter in Reader 📖", key=f"btn_search_read_{c['id']}"):
                        st.session_state["selected_topic_id"] = c["topic_id"]
                        st.switch_page("pages/chapters.py")

        # Matching Facts
        if results["facts"]:
            st.markdown("##### 💡 Historical Facts")
            for f in results["facts"]:
                st.markdown(f"""
                <div style="background-color: var(--color-cream); border: 1px solid var(--color-border); border-left: 3px solid var(--color-gold); border-radius: 6px; padding: 0.6rem 0.9rem; margin-bottom: 0.4rem; font-size: 0.92rem;">
                    <span style="color: var(--color-terracotta); font-weight: 700;">[{f['topic_title']}]</span> {f['fact_text']}
                </div>
                """, unsafe_allow_html=True)

    ui_theme.render_heritage_divider()


# -------------------------------------------------------------
# 4. HISTORICAL TOPIC CARDS
# -------------------------------------------------------------
st.markdown("""
<div style="margin-top: 1rem; margin-bottom: 0.2rem;">
    <h2 style="font-size: 1.85rem; font-weight: 800; color: var(--color-deep-brown); margin-bottom: 0.15rem;">
        🏛️ Foundational Historical Topics
    </h2>
    <div style="font-size: 0.96rem; color: var(--color-muted); margin-bottom: 1.2rem;">
        Immerse yourself in authentic curated studies spanning ancient civil engineering, martial defense, and the freedom struggle.
    </div>
</div>
""", unsafe_allow_html=True)

topics = database.get_topics()

# Image and icon mapping for the four topics
TOPIC_META = {
    "Chhatrapati Shivaji Maharaj": {
        "icon": "⚔️",
        "image": os.path.join(os.path.dirname(__file__), "assets", "images", "topics", "shivaji.jpg"),
        "alt": "Raigad Fort and Maratha Architecture"
    },
    "Chhatrapati Sambhaji Maharaj": {
        "icon": "🛡️",
        "image": os.path.join(os.path.dirname(__file__), "assets", "images", "topics", "sambhaji.jpg"),
        "alt": "Deccan Hill Fortresses and Night Ramparts"
    },
    "Harappan Civilization": {
        "icon": "🏺",
        "image": os.path.join(os.path.dirname(__file__), "assets", "images", "topics", "harappan.jpg"),
        "alt": "Ancient Indus Valley Urban Architecture and Ruins"
    },
    "The Revolt of 1857": {
        "icon": "🔥",
        "image": os.path.join(os.path.dirname(__file__), "assets", "images", "topics", "revolt1857.jpg"),
        "alt": "Historical Archival Depiction of the 1857 Uprising"
    }
}

# Display in a 2x2 responsive grid
col_left, col_right = st.columns(2, gap="large")

for idx, topic in enumerate(topics):
    col = col_left if idx % 2 == 0 else col_right
    meta = TOPIC_META.get(topic["title"], {"icon": "📜", "image": "", "alt": "Topic Image"})
    img_path = meta["image"]
    t_id = topic["id"]

    with col:
        # Visual Image Frame
        if img_path and os.path.exists(img_path):
            st.image(img_path, caption=meta["alt"], use_container_width=True)
        else:
            st.markdown("""
            <div style="height: 180px; background-color: #E8DECF; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #6E5D4F; font-size: 1rem; font-weight: 600;">
                📜 Historical Illustration
            </div>
            """, unsafe_allow_html=True)

        # Card Details
        st.markdown(f"""
        <div style="background-color: var(--color-cream); border: 1px solid var(--color-border); border-top: 3px solid var(--color-terracotta); border-radius: 8px; padding: 1.15rem 1.25rem; margin-top: -0.5rem; margin-bottom: 0.6rem;">
            <div style="font-size: 1.25rem; font-weight: 800; color: var(--color-deep-brown); margin-bottom: 0.35rem;">
                {meta['icon']} {topic['title']}
            </div>
            <div style="display: inline-block; background-color: #F1E5D3; color: var(--color-terracotta); font-size: 0.8rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; border-left: 2px solid var(--color-terracotta); margin-bottom: 0.7rem;">
                📅 {topic['period']}
            </div>
            <div style="font-size: 0.92rem; color: var(--color-text); line-height: 1.6; margin-bottom: 0.4rem;">
                {topic['summary']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Explore Button
        if st.button(f"Explore {topic['title']} →", key=f"btn_explore_topic_{t_id}", use_container_width=True, type="primary"):
            st.session_state["selected_topic_id"] = t_id
            st.switch_page("pages/history.py")

        st.write("")  # Visual breathing space


# -------------------------------------------------------------
# 5. DID YOU KNOW SECTION (Authentic facts from SQLite)
# -------------------------------------------------------------
ui_theme.render_heritage_divider()

fact_data = ui_theme.get_random_fact_from_db()

st.markdown(f"""
<div class="did-you-know-box">
    <div class="did-you-know-title">
        💡 Did You Know?
        <span style="font-size: 0.82rem; font-weight: 600; color: var(--color-gold); margin-left: auto;">Historical Fact Archive</span>
    </div>
    <div class="did-you-know-text">
        "{fact_data['fact_text']}"
    </div>
    <div class="did-you-know-source">
        — From topic study: <strong>{fact_data['topic_title']}</strong>
    </div>
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------------------
# 6. FEATURE SECTION: "Explore IndicRoots"
# -------------------------------------------------------------
st.markdown("""
<div style="margin-top: 1.8rem; margin-bottom: 1.2rem;">
    <h2 style="font-size: 1.85rem; font-weight: 800; color: var(--color-deep-brown); margin-bottom: 0.15rem;">
        🧭 Explore IndicRoots Learning Hub
    </h2>
    <div style="font-size: 0.96rem; color: var(--color-muted);">
        Interactive educational tools designed for college students and history enthusiasts.
    </div>
</div>
""", unsafe_allow_html=True)

# 6 Feature cards in a 3-column x 2-row layout
f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-icon">🏰</div>
        <div class="feature-card-title">Explore Forts</div>
        <div class="feature-card-desc">Interactive geographic map displaying 20 historic Indian forts with coordinates, history, and military significance.</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/forts.py", label="Open Forts Map →", icon="🏰", use_container_width=True)

with f_col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-icon">🧠</div>
        <div class="feature-card-title">Test Your Knowledge</div>
        <div class="feature-card-desc">Challenge yourself with randomized 15-question multiple-choice quizzes with instant grading and explanations.</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/quiz.py", label="Take a Quiz →", icon="🧠", use_container_width=True)

with f_col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-icon">📝</div>
        <div class="feature-card-title">My Notes</div>
        <div class="feature-card-desc">Create, search, edit, and organize persistent study notes linked to historical eras or recorded as general takeaways.</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/notes.py", label="View My Notes →", icon="📝", use_container_width=True)

st.write("")

f_col4, f_col5, f_col6 = st.columns(3)

with f_col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-icon">🗓️</div>
        <div class="feature-card-title">Historical Timeline</div>
        <div class="feature-card-desc">Chronological journey across foundational milestones from ancient Bronze Age urbanism to 19th-century movements.</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/timeline.py", label="View Timeline →", icon="🗓️", use_container_width=True)

with f_col5:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-icon">📖</div>
        <div class="feature-card-title">Read Chapters</div>
        <div class="feature-card-desc">Dedicated reader mode to read in-depth, structured historical chapters with smooth previous/next navigation.</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/chapters.py", label="Open Chapters Reader →", icon="📖", use_container_width=True)

with f_col6:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-icon">📊</div>
        <div class="feature-card-title">Track Progress</div>
        <div class="feature-card-desc">Comprehensive learning dashboard tracking quiz scores, mastery levels, and complete historical attempt history.</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/progress.py", label="View My Progress →", icon="📊", use_container_width=True)


# -------------------------------------------------------------
# 7. HERITAGE FOOTER
# -------------------------------------------------------------
ui_theme.render_heritage_divider()

st.markdown("""
<div class="heritage-footer">
    <strong>IndicRoots</strong> — College Educational Web Project in Indian History<br>
    Built with <strong>Python</strong>, <strong>Streamlit</strong>, and <strong>SQLite</strong> • Fully Local & Offline-Ready<br>
    <em>Dedicated to authentic, accessible, and respectful historical learning.</em>
</div>
""", unsafe_allow_html=True)
