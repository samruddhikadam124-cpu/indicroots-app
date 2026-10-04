"""
IndicRoots - Configuration & Constants
"""

APP_TITLE = "IndicRoots — Indian Heritage & History"
APP_ICON = "🪷"
APP_LAYOUT = "wide"

# Heritage Color Palette
COLORS = {
    "saffron_primary": "#E06D14",
    "saffron_light": "#F58220",
    "gold_accent": "#D4AF37",
    "gold_light": "#FFD700",
    "terracotta": "#8C2D19",
    "terracotta_light": "#B33927",
    "bg_dark": "#121217",
    "bg_surface": "#1A1A24",
    "bg_card": "#21212E",
    "text_parchment": "#F5EFEB",
    "text_muted": "#B8B5B0",
    "border_gold": "rgba(212, 175, 55, 0.28)",
}

# Supported Main Topics
TOPICS = {
    "shivaji": {
        "id": "shivaji",
        "title": "Chhatrapati Shivaji Maharaj",
        "icon": "⚔️",
        "period": "1630 – 1680 CE",
        "tagline": "Founder of Hindavi Swarajya & Master of Ganimi Kawa",
        "accent": "#E06D14"
    },
    "sambhaji": {
        "id": "sambhaji",
        "title": "Chhatrapati Sambhaji Maharaj",
        "icon": "🛡️",
        "period": "1657 – 1689 CE",
        "tagline": "The Undefeated Monarch, Sanskrit Polymath & Dharmaveer",
        "accent": "#B33927"
    },
    "harappa": {
        "id": "harappa",
        "title": "Harappan Civilization",
        "icon": "🏺",
        "period": "c. 3300 – 1300 BCE",
        "tagline": "Pioneers of Bronze Age Urban Planning & Sanitary Engineering",
        "accent": "#D4AF37"
    },
    "revolt1857": {
        "id": "revolt1857",
        "title": "The Revolt of 1857",
        "icon": "🔥",
        "period": "1857 – 1858 CE",
        "tagline": "India's First War of Independence & Shattering of Company Rule",
        "accent": "#C9381E"
    }
}

# Main Navigation items
NAV_ITEMS = [
    ("Home", "🏠"),
    ("History", "📖"),
    ("Timeline", "⏳"),
    ("Quiz", "🎯"),
    ("Progress", "📊"),
    ("About", "ℹ️")
]
