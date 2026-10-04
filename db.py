"""
IndicRoots - Database Access Layer
SQLite Database Management and Query Services
"""

import sqlite3
import os
from datetime import datetime
from typing import List, Dict, Any, Optional

DB_FILE = os.path.join(os.path.dirname(__file__), "indicroots.db")

def get_connection() -> sqlite3.Connection:
    """Creates a connection to the SQLite database with dictionary-like row factory."""
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# ----------------- TOPICS -----------------

def get_all_topics() -> List[Dict[str, Any]]:
    """Retrieve all topic records."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM topics ORDER BY display_order ASC")
        return [dict(row) for row in cursor.fetchall()]

def get_topic_by_id(topic_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a single topic by ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM topics WHERE id = ?", (topic_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

# ----------------- HISTORY MODULES -----------------

def get_chapters(topic_id: str) -> List[Dict[str, Any]]:
    """Fetch chapters for a specific topic in chronological / sequence order."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM chapters WHERE topic_id = ? ORDER BY chapter_number ASC",
            (topic_id,)
        )
        return [dict(row) for row in cursor.fetchall()]

def get_people(topic_id: str) -> List[Dict[str, Any]]:
    """Fetch key historical personalities for a topic."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM people WHERE topic_id = ? ORDER BY display_order ASC, name ASC",
            (topic_id,)
        )
        return [dict(row) for row in cursor.fetchall()]

def get_places(topic_id: str) -> List[Dict[str, Any]]:
    """Fetch strategic & archaeological places for a topic."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM places WHERE topic_id = ? ORDER BY display_order ASC, name ASC",
            (topic_id,)
        )
        return [dict(row) for row in cursor.fetchall()]

def get_facts(topic_id: str) -> List[Dict[str, Any]]:
    """Fetch curated historical facts & insights for a topic."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM facts WHERE topic_id = ? ORDER BY id ASC",
            (topic_id,)
        )
        return [dict(row) for row in cursor.fetchall()]

# ----------------- TIMELINE -----------------

def get_timeline_events(topic_id: Optional[str] = None, sort_order: str = "ASC", search_query: str = "") -> List[Dict[str, Any]]:
    """Fetch timeline events with optional topic filter, search string, and sort order."""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = """
            SELECT t.id, t.topic_id, t.year_display, t.sort_year, t.title, 
                   t.location, t.description, t.importance,
                   p.title as topic_title, p.icon as topic_icon, p.accent_color
            FROM timeline_events t
            JOIN topics p ON t.topic_id = p.id
            WHERE 1=1
        """
        params = []
        if topic_id and topic_id != "all":
            query += " AND t.topic_id = ?"
            params.append(topic_id)
        if search_query:
            query += " AND (t.title LIKE ? OR t.description LIKE ? OR t.location LIKE ? OR t.year_display LIKE ?)"
            wildcard = f"%{search_query.strip()}%"
            params.extend([wildcard, wildcard, wildcard, wildcard])
        
        direction = "DESC" if sort_order.upper() == "DESC" else "ASC"
        query += f" ORDER BY t.sort_year {direction}"
        
        cursor.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]

# ----------------- QUIZ -----------------

def get_quiz_questions(topic_id: Optional[str] = None, limit: int = 15) -> List[Dict[str, Any]]:
    """Fetch randomized quiz questions for the selected topic (or all topics)."""
    with get_connection() as conn:
        cursor = conn.cursor()
        if topic_id and topic_id != "all":
            cursor.execute(
                """SELECT q.*, t.title as topic_title, t.icon as topic_icon 
                   FROM quiz_questions q
                   JOIN topics t ON q.topic_id = t.id
                   WHERE q.topic_id = ? 
                   ORDER BY RANDOM() LIMIT ?""",
                (topic_id, limit)
            )
        else:
            cursor.execute(
                """SELECT q.*, t.title as topic_title, t.icon as topic_icon 
                   FROM quiz_questions q
                   JOIN topics t ON q.topic_id = t.id
                   ORDER BY RANDOM() LIMIT ?""",
                (limit,)
            )
        return [dict(row) for row in cursor.fetchall()]

def record_quiz_result(topic_id: str, score: int, total_questions: int) -> int:
    """Store completed quiz results in the database."""
    percentage = round((score / total_questions) * 100, 1) if total_questions > 0 else 0
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO quiz_history (topic_id, timestamp, score, total_questions, percentage)
               VALUES (?, ?, ?, ?, ?)""",
            (topic_id, now_str, score, total_questions, percentage)
        )
        conn.commit()
        return cursor.lastrowid

def get_quiz_progress_stats() -> Dict[str, Any]:
    """Calculate overall quiz performance metrics."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                COUNT(*) as total_attempts,
                AVG(percentage) as avg_percentage,
                MAX(percentage) as best_percentage
            FROM quiz_history
        """)
        row = cursor.fetchone()
        
        # Latest attempt
        cursor.execute("""
            SELECT score, total_questions, percentage, timestamp, topic_id
            FROM quiz_history 
            ORDER BY id DESC LIMIT 1
        """)
        latest_row = cursor.fetchone()

        # Topic breakdown
        cursor.execute("""
            SELECT 
                h.topic_id,
                COALESCE(t.title, 'Mixed Topics') as topic_title,
                COALESCE(t.icon, '🔀') as topic_icon,
                COUNT(*) as attempts,
                AVG(h.percentage) as avg_pct,
                MAX(h.percentage) as max_pct
            FROM quiz_history h
            LEFT JOIN topics t ON h.topic_id = t.id
            GROUP BY h.topic_id
        """)
        topic_stats = [dict(r) for r in cursor.fetchall()]

        total_attempts = row["total_attempts"] if row and row["total_attempts"] else 0
        avg_percentage = round(row["avg_percentage"], 1) if row and row["avg_percentage"] is not None else 0.0
        best_percentage = round(row["best_percentage"], 1) if row and row["best_percentage"] is not None else 0.0

        return {
            "total_attempts": total_attempts,
            "avg_percentage": avg_percentage,
            "best_percentage": best_percentage,
            "latest": dict(latest_row) if latest_row else None,
            "topic_stats": topic_stats
        }

def get_quiz_history(limit: int = 50) -> List[Dict[str, Any]]:
    """Retrieve historical quiz attempts with topic metadata."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                h.id, h.topic_id, h.timestamp, h.score, h.total_questions, h.percentage,
                COALESCE(t.title, 'All Topics') as topic_title,
                COALESCE(t.icon, '🔀') as topic_icon
            FROM quiz_history h
            LEFT JOIN topics t ON h.topic_id = t.id
            ORDER BY h.id DESC
            LIMIT ?
        """, (limit,))
        return [dict(row) for row in cursor.fetchall()]

def clear_quiz_history() -> None:
    """Clear all quiz history records."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM quiz_history")
        conn.commit()

# ----------------- SEARCH -----------------

def global_search(query: str) -> Dict[str, List[Dict[str, Any]]]:
    """Execute a comprehensive search across chapters, people, places, facts, and timeline."""
    if not query or len(query.strip()) < 2:
        return {"chapters": [], "people": [], "places": [], "facts": [], "timeline": []}

    term = f"%{query.strip()}%"
    results: Dict[str, List[Dict[str, Any]]] = {}

    with get_connection() as conn:
        cursor = conn.cursor()

        # Search Chapters
        cursor.execute("""
            SELECT c.id, c.topic_id, c.title, c.subtitle, c.content, t.title as topic_title, t.icon as topic_icon
            FROM chapters c
            JOIN topics t ON c.topic_id = t.id
            WHERE c.title LIKE ? OR c.content LIKE ? OR c.subtitle LIKE ?
            LIMIT 6
        """, (term, term, term))
        results["chapters"] = [dict(r) for r in cursor.fetchall()]

        # Search People
        cursor.execute("""
            SELECT p.id, p.topic_id, p.name, p.role_title, p.lifespan, p.bio, p.achievements, t.title as topic_title, t.icon as topic_icon
            FROM people p
            JOIN topics t ON p.topic_id = t.id
            WHERE p.name LIKE ? OR p.role_title LIKE ? OR p.bio LIKE ? OR p.achievements LIKE ?
            LIMIT 6
        """, (term, term, term, term))
        results["people"] = [dict(r) for r in cursor.fetchall()]

        # Search Places
        cursor.execute("""
            SELECT pl.id, pl.topic_id, pl.name, pl.location, pl.significance, pl.description, t.title as topic_title, t.icon as topic_icon
            FROM places pl
            JOIN topics t ON pl.topic_id = t.id
            WHERE pl.name LIKE ? OR pl.location LIKE ? OR pl.significance LIKE ? OR pl.description LIKE ?
            LIMIT 6
        """, (term, term, term, term))
        results["places"] = [dict(r) for r in cursor.fetchall()]

        # Search Facts
        cursor.execute("""
            SELECT f.id, f.topic_id, f.headline, f.detail, f.category, t.title as topic_title, t.icon as topic_icon
            FROM facts f
            JOIN topics t ON f.topic_id = t.id
            WHERE f.headline LIKE ? OR f.detail LIKE ? OR f.category LIKE ?
            LIMIT 6
        """, (term, term, term))
        results["facts"] = [dict(r) for r in cursor.fetchall()]

        # Search Timeline
        cursor.execute("""
            SELECT te.id, te.topic_id, te.year_display, te.sort_year, te.title, te.location, te.description, t.title as topic_title, t.icon as topic_icon
            FROM timeline_events te
            JOIN topics t ON te.topic_id = t.id
            WHERE te.title LIKE ? OR te.description LIKE ? OR te.year_display LIKE ? OR te.location LIKE ?
            LIMIT 6
        """, (term, term, term, term))
        results["timeline"] = [dict(r) for r in cursor.fetchall()]

    return results
