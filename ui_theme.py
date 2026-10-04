"""
ui_theme.py - Shared Heritage Theme & UI Components for IndicRoots
Provides the authentic Indian history & heritage visual design system:
- Earthy color palette: Terracotta, Deep Brown, Warm Parchment, Heritage Gold, Cream
- Grouped sidebar navigation with active page highlighting
- Decorative heritage dividers & badges
- Card styling and responsive layout rules
"""

import streamlit as st
import database
import random

# ==============================================================================
# 1. CORE HERITAGE DESIGN SYSTEM CSS
# ==============================================================================
HERITAGE_CSS = """
<style>
    /* -------------------------------------------------------------
       COLOR TOKENS & SYSTEM VARIABLES
       ------------------------------------------------------------- */
    :root {
        --color-bg: #F7F1E5;           /* Warm ancient parchment */
        --color-deep-brown: #4A2E22;   /* Deep historical brown for titles */
        --color-terracotta: #9B3D24;   /* Terracotta / saffron accent */
        --color-gold: #C9922E;         /* Classical heritage gold */
        --color-text: #2B2118;         /* Rich dark readable text */
        --color-cream: #FFF9EF;        /* Cream background for cards */
        --color-border: #E2D6C5;       /* Parchment stone border */
        --color-border-dark: #CBB99F;  /* Accent border */
        --color-muted: #6E5D4F;        /* Muted secondary text */
        --color-sidebar-bg: #EFE8DA;   /* Antique parchment sidebar */
    }

    /* Base application background and typography */
    .stApp {
        background-color: var(--color-bg) !important;
        color: var(--color-text) !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    /* Main container bounds & comfortable breathing room */
    .block-container {
        max-width: 1080px;
        padding-top: 1.8rem;
        padding-bottom: 3.5rem;
    }

    /* Hide default Streamlit sidebar page list */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* -------------------------------------------------------------
       DISTINCTIVE SIDEBAR NAVIGATION
       ------------------------------------------------------------- */
    [data-testid="stSidebar"] {
        background-color: var(--color-sidebar-bg) !important;
        border-right: 1px solid var(--color-border-dark) !important;
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
        padding-left: 1.1rem;
        padding-right: 1.1rem;
    }

    /* Sidebar Brand Header */
    .sidebar-brand-box {
        text-align: center;
        padding: 0.6rem 0.4rem 0.9rem 0.4rem;
        border-bottom: 1px solid var(--color-border-dark);
        margin-bottom: 1.1rem;
    }

    .sidebar-brand-title {
        font-size: 1.65rem;
        font-weight: 800;
        color: var(--color-terracotta);
        letter-spacing: 0.5px;
        margin-bottom: 0.15rem;
    }

    .sidebar-brand-subtitle {
        font-size: 0.92rem;
        font-weight: 700;
        color: var(--color-deep-brown);
        margin-bottom: 0.2rem;
    }

    .sidebar-brand-tagline {
        font-size: 0.76rem;
        font-weight: 600;
        color: var(--color-gold);
        letter-spacing: 1.2px;
        text-transform: uppercase;
    }

    /* Navigation Group Section Headers */
    .nav-group-header {
        font-size: 0.72rem;
        font-weight: 800;
        color: var(--color-terracotta);
        letter-spacing: 1.8px;
        text-transform: uppercase;
        margin-top: 1.1rem;
        margin-bottom: 0.4rem;
        padding-left: 0.4rem;
    }

    /* Sidebar Link items */
    [data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] {
        border-radius: 6px !important;
        margin-bottom: 3px !important;
        padding: 6px 10px !important;
        transition: all 0.2s ease-in-out !important;
        color: var(--color-deep-brown) !important;
        font-weight: 500 !important;
        background-color: transparent !important;
    }

    [data-testid="stSidebar"] [data-testid="stPageLink-NavLink"]:hover {
        background-color: #E4D8C4 !important;
        color: var(--color-terracotta) !important;
        transform: translateX(2px);
    }

    /* Highlight Active Selected Page */
    [data-testid="stSidebar"] a[aria-current="page"] [data-testid="stPageLink-NavLink"],
    [data-testid="stSidebar"] a[aria-current="page"] {
        background-color: #E2D2B8 !important;
        color: var(--color-terracotta) !important;
        font-weight: 700 !important;
        border-left: 4px solid var(--color-terracotta) !important;
        box-shadow: 0 1px 3px rgba(74, 46, 34, 0.08);
    }

    /* -------------------------------------------------------------
       HERO BANNER & HERITAGE HEADINGS
       ------------------------------------------------------------- */
    .hero-container {
        position: relative;
        background-color: var(--color-cream);
        border: 2px solid var(--color-border);
        border-top: 4px solid var(--color-terracotta);
        border-radius: 12px;
        padding: 2.2rem 2.4rem;
        margin-bottom: 1.8rem;
        box-shadow: 0 4px 14px rgba(74, 46, 34, 0.06);
        background-image: linear-gradient(135deg, rgba(255, 249, 239, 0.96) 0%, rgba(247, 241, 229, 0.92) 100%);
    }

    .hero-title-main {
        font-size: 2.6rem;
        font-weight: 900;
        color: var(--color-terracotta);
        letter-spacing: -0.5px;
        margin-bottom: 0.3rem;
        line-height: 1.15;
    }

    .hero-subtitle-main {
        font-size: 1.22rem;
        font-weight: 600;
        color: var(--color-deep-brown);
        margin-bottom: 0.9rem;
    }

    .hero-description {
        font-size: 0.98rem;
        color: var(--color-text);
        line-height: 1.65;
        max-width: 820px;
    }

    /* Decorative Heritage Divider */
    .heritage-divider {
        text-align: center;
        color: var(--color-gold);
        font-size: 1.15rem;
        letter-spacing: 5px;
        margin: 1.4rem 0 1.6rem 0;
        user-select: none;
    }

    /* -------------------------------------------------------------
       HISTORICAL TOPIC CARDS
       ------------------------------------------------------------- */
    .heritage-topic-card {
        background-color: var(--color-cream);
        border: 1px solid var(--color-border);
        border-top: 3px solid var(--color-terracotta);
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 1.4rem;
        box-shadow: 0 3px 10px rgba(74, 46, 34, 0.05);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    .heritage-topic-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 18px rgba(74, 46, 34, 0.10);
        border-color: var(--color-gold);
    }

    .topic-img-frame {
        width: 100%;
        height: 180px;
        overflow: hidden;
        background-color: #E8DECF;
        border-bottom: 1px solid var(--color-border);
    }

    .topic-img-frame img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        transition: transform 0.3s ease;
    }

    .heritage-topic-card:hover .topic-img-frame img {
        transform: scale(1.03);
    }

    .topic-card-content {
        padding: 1.25rem 1.35rem;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }

    .topic-card-heading {
        font-size: 1.25rem;
        font-weight: 800;
        color: var(--color-deep-brown);
        margin-bottom: 0.4rem;
        line-height: 1.3;
    }

    .topic-period-pill {
        display: inline-block;
        background-color: #F1E5D3;
        color: var(--color-terracotta);
        font-size: 0.82rem;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 4px;
        border-left: 2px solid var(--color-terracotta);
        margin-bottom: 0.75rem;
        width: fit-content;
    }

    .topic-summary-text {
        font-size: 0.93rem;
        color: var(--color-text);
        line-height: 1.6;
        margin-bottom: 1.1rem;
        flex-grow: 1;
    }

    /* -------------------------------------------------------------
       FEATURE GRID CARDS ("EXPLORE INDICROOTS")
       ------------------------------------------------------------- */
    .feature-card {
        background-color: var(--color-cream);
        border: 1px solid var(--color-border);
        border-radius: 8px;
        padding: 1.15rem 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 6px rgba(74, 46, 34, 0.04);
        transition: all 0.2s ease;
        text-align: left;
    }

    .feature-card:hover {
        border-color: var(--color-terracotta);
        background-color: #FFFDF9;
        transform: translateY(-2px);
        box-shadow: 0 5px 12px rgba(74, 46, 34, 0.08);
    }

    .feature-card-icon {
        font-size: 1.8rem;
        margin-bottom: 0.35rem;
    }

    .feature-card-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--color-deep-brown);
        margin-bottom: 0.25rem;
    }

    .feature-card-desc {
        font-size: 0.85rem;
        color: var(--color-muted);
        line-height: 1.45;
    }

    /* -------------------------------------------------------------
       DID YOU KNOW SECTION
       ------------------------------------------------------------- */
    .did-you-know-box {
        background-color: var(--color-cream);
        border: 1px solid var(--color-border);
        border-left: 5px solid var(--color-gold);
        border-radius: 8px;
        padding: 1.25rem 1.5rem;
        margin: 1.6rem 0;
        box-shadow: 0 2px 8px rgba(74, 46, 34, 0.04);
    }

    .did-you-know-title {
        font-size: 1.12rem;
        font-weight: 800;
        color: var(--color-terracotta);
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }

    .did-you-know-text {
        font-size: 0.96rem;
        color: var(--color-text);
        line-height: 1.65;
        font-style: italic;
    }

    .did-you-know-source {
        font-size: 0.82rem;
        font-weight: 600;
        color: var(--color-muted);
        margin-top: 0.5rem;
        text-align: right;
    }

    /* -------------------------------------------------------------
       GLOBAL BUTTONS, INPUTS & FORMS
       ------------------------------------------------------------- */
    /* Primary buttons */
    .stButton > button[kind="primary"],
    .stButton > button {
        background-color: var(--color-terracotta) !important;
        color: var(--color-cream) !important;
        border: 1px solid #7E2F1B !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        letter-spacing: 0.2px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 4px rgba(74, 46, 34, 0.12) !important;
    }

    .stButton > button:hover {
        background-color: #822F19 !important;
        border-color: var(--color-gold) !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 10px rgba(74, 46, 34, 0.20) !important;
        transform: translateY(-1px);
    }

    /* Secondary / outline buttons */
    .stButton > button[kind="secondary"] {
        background-color: var(--color-cream) !important;
        color: var(--color-deep-brown) !important;
        border: 1px solid var(--color-border-dark) !important;
    }

    .stButton > button[kind="secondary"]:hover {
        background-color: #F3EBDD !important;
        color: var(--color-terracotta) !important;
        border-color: var(--color-terracotta) !important;
    }

    /* Text Inputs, Areas & Selects */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > div {
        background-color: #FFFDF9 !important;
        border: 1px solid var(--color-border) !important;
        border-radius: 6px !important;
        color: var(--color-text) !important;
        font-size: 0.95rem !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--color-gold) !important;
        box-shadow: 0 0 0 2px rgba(201, 146, 46, 0.25) !important;
    }

    /* Expanders styling */
    [data-testid="stExpander"] {
        background-color: var(--color-cream) !important;
        border: 1px solid var(--color-border) !important;
        border-radius: 8px !important;
        margin-bottom: 0.8rem !important;
    }

    /* Footer */
    .heritage-footer {
        text-align: center;
        border-top: 1px solid var(--color-border);
        padding-top: 1.8rem;
        margin-top: 2.8rem;
        color: var(--color-muted);
        font-size: 0.88rem;
        line-height: 1.7;
    }

    .heritage-footer strong {
        color: var(--color-deep-brown);
    }
</style>
"""


def inject_heritage_css():
    """Injects the unified IndicRoots heritage CSS stylesheet."""
    st.markdown(HERITAGE_CSS, unsafe_allow_html=True)


def render_sidebar(active_page="home"):
    """
    Renders the custom IndicRoots sidebar navigation.
    Organized into three clean groups:
    - EXPLORE (Home, History, Chapters Reader, Forts Map, Timeline)
    - LEARN (Quiz, Progress, My Notes)
    - INFO (About)
    """
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-brand-box">
            <div class="sidebar-brand-title">🪷 IndicRoots</div>
            <div class="sidebar-brand-subtitle">Indian History</div>
            <div class="sidebar-brand-tagline">Knowledge • Heritage • Learning</div>
        </div>
        """, unsafe_allow_html=True)

        # Group 1: EXPLORE
        st.markdown('<div class="nav-group-header">EXPLORE</div>', unsafe_allow_html=True)
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link("pages/history.py", label="History", icon="📚")
        st.page_link("pages/chapters.py", label="Chapters Reader", icon="📖")
        st.page_link("pages/forts.py", label="Forts Map", icon="🏰")
        st.page_link("pages/timeline.py", label="Timeline", icon="🗓️")

        # Group 2: LEARN
        st.markdown('<div class="nav-group-header">LEARN</div>', unsafe_allow_html=True)
        st.page_link("pages/quiz.py", label="Quiz", icon="🧠")
        st.page_link("pages/progress.py", label="Progress", icon="📊")
        st.page_link("pages/notes.py", label="My Notes", icon="📝")

        # Group 3: INFO
        st.markdown('<div class="nav-group-header">INFO</div>', unsafe_allow_html=True)
        st.page_link("pages/about.py", label="About", icon="📖")

        st.markdown("""
        <div style="margin-top: 1.6rem; border-top: 1px solid var(--color-border-dark); padding-top: 0.9rem; text-align: center;">
            <span style="font-size: 0.78rem; color: var(--color-muted);">
                📜 Offline-Ready • Python + SQLite
            </span>
        </div>
        """, unsafe_allow_html=True)


def render_heritage_divider():
    """Renders the subtle Indian-inspired decorative divider."""
    st.markdown('<div class="heritage-divider">──────── ❖ ────────</div>', unsafe_allow_html=True)


def get_random_fact_from_db():
    """Fetches an authentic historical fact stored in SQLite."""
    try:
        conn = database.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT f.fact_text, t.title AS topic_title
            FROM facts f
            JOIN topics t ON f.topic_id = t.id
            ORDER BY RANDOM() LIMIT 1
        """)
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"fact_text": row["fact_text"], "topic_title": row["topic_title"]}
    except Exception:
        pass
    
    # Fallback if DB fetch fails
    return {
        "fact_text": "The Harappan civilization featured sophisticated urban sanitation systems, covered street drains, and standardized baked bricks over 4,500 years ago.",
        "topic_title": "Harappan Civilization"
    }
