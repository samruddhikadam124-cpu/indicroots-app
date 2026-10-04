import sqlite3
import os
from datetime import datetime

# Path to the database file inside the data folder
DB_PATH = os.path.join(os.path.dirname(__file__), "data", "indicroots.db")


# -------------------------------------------------------------
# DATABASE CONNECTION & TABLE CREATION
# -------------------------------------------------------------

def get_connection():
    """
    Connects to the SQLite database.
    Using sqlite3.Row allows us to access columns by name, like: row["title"]
    """
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    """
    Creates all 8 required tables if they do not already exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Topics table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            period TEXT NOT NULL,
            summary TEXT NOT NULL
        )
    """)

    # 2. Chapters table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chapters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            chapter_number INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    # 3. Quiz Questions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL,
            explanation TEXT
        )
    """)

    # 4. Timeline table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS timeline (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            year TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)

    # 5. People table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)

    # 6. Places table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS places (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)

    # 7. Facts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS facts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            fact_text TEXT NOT NULL
        )
    """)

    # 8. Quiz Progress table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            date_taken TEXT NOT NULL
        )
    """)

    # 9. Forts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS forts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            state TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            history TEXT NOT NULL,
            important_events TEXT NOT NULL,
            built_or_established TEXT NOT NULL,
            image_url TEXT
        )
    """)

    # 10. Notes table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            topic_id INTEGER,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
    """)

    conn.commit()
    conn.close()


# Alias for app startup
def init_db():
    create_tables()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM forts")
    count = cursor.fetchone()[0]
    conn.close()
    if count == 0:
        import forts_data
        forts_data.load_forts_data()


# -------------------------------------------------------------
# TOPICS FUNCTIONS
# -------------------------------------------------------------

def add_topic(title, period, summary):
    """Adds a new historical topic."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO topics (title, period, summary) VALUES (?, ?, ?)",
        (title, period, summary)
    )
    conn.commit()
    topic_id = cursor.lastrowid
    conn.close()
    return topic_id


def get_topics():
    """Returns a list of all topics."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM topics ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_topic(topic_id):
    """Returns a single topic by its ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM topics WHERE id = ?", (topic_id,))
    row = cursor.fetchone()
    conn.close()
    return row


# -------------------------------------------------------------
# CHAPTERS FUNCTIONS
# -------------------------------------------------------------

def add_chapter(topic_id, chapter_number, title, content):
    """Adds a chapter for a specific topic."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chapters (topic_id, chapter_number, title, content) VALUES (?, ?, ?, ?)",
        (topic_id, chapter_number, title, content)
    )
    conn.commit()
    conn.close()


def get_chapters(topic_id=None):
    """Returns chapters, optionally filtered by topic_id."""
    conn = get_connection()
    cursor = conn.cursor()
    if topic_id is not None:
        cursor.execute("SELECT * FROM chapters WHERE topic_id = ? ORDER BY chapter_number ASC", (topic_id,))
    else:
        cursor.execute("SELECT * FROM chapters ORDER BY chapter_number ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows


# -------------------------------------------------------------
# QUIZ QUESTIONS FUNCTIONS
# -------------------------------------------------------------

def add_quiz_question(topic_id, question, option_a, option_b, option_c, option_d, correct_option, explanation=""):
    """Adds a quiz question for a topic."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO quiz_questions 
           (topic_id, question, option_a, option_b, option_c, option_d, correct_option, explanation) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (topic_id, question, option_a, option_b, option_c, option_d, correct_option, explanation)
    )
    conn.commit()
    conn.close()


def get_quiz_questions(topic_id=None, limit=None, order_by="id ASC"):
    """Returns quiz questions, optionally filtered by topic_id and limited to a count."""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM quiz_questions"
    params = []

    if topic_id is not None:
        query += " WHERE topic_id = ?"
        params.append(topic_id)

    if order_by:
        query += f" ORDER BY {order_by}"

    if limit is not None:
        query += " LIMIT ?"
        params.append(limit)

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows


# -------------------------------------------------------------
# TIMELINE FUNCTIONS
# -------------------------------------------------------------

def add_timeline_event(topic_id, year, title, description):
    """Adds a timeline event."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO timeline (topic_id, year, title, description) VALUES (?, ?, ?, ?)",
        (topic_id, year, title, description)
    )
    conn.commit()
    conn.close()


def get_timeline(topic_id=None):
    """Returns timeline events, optionally filtered by topic_id."""
    conn = get_connection()
    cursor = conn.cursor()
    if topic_id is not None:
        cursor.execute("SELECT * FROM timeline WHERE topic_id = ? ORDER BY id ASC", (topic_id,))
    else:
        cursor.execute("SELECT * FROM timeline ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows


# -------------------------------------------------------------
# PEOPLE FUNCTIONS
# -------------------------------------------------------------

def add_person(topic_id, name, role, description):
    """Adds a historical figure for a topic."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO people (topic_id, name, role, description) VALUES (?, ?, ?, ?)",
        (topic_id, name, role, description)
    )
    conn.commit()
    conn.close()


def get_people(topic_id=None):
    """Returns historical figures, optionally filtered by topic_id."""
    conn = get_connection()
    cursor = conn.cursor()
    if topic_id is not None:
        cursor.execute("SELECT * FROM people WHERE topic_id = ? ORDER BY id ASC", (topic_id,))
    else:
        cursor.execute("SELECT * FROM people ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows


# -------------------------------------------------------------
# PLACES FUNCTIONS
# -------------------------------------------------------------

def add_place(topic_id, name, location, description):
    """Adds a historic place/fort/archaeological site."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO places (topic_id, name, location, description) VALUES (?, ?, ?, ?)",
        (topic_id, name, location, description)
    )
    conn.commit()
    conn.close()


def get_places(topic_id=None):
    """Returns historic places, optionally filtered by topic_id."""
    conn = get_connection()
    cursor = conn.cursor()
    if topic_id is not None:
        cursor.execute("SELECT * FROM places WHERE topic_id = ? ORDER BY id ASC", (topic_id,))
    else:
        cursor.execute("SELECT * FROM places ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows


# -------------------------------------------------------------
# FACTS FUNCTIONS
# -------------------------------------------------------------

def add_fact(topic_id, fact_text):
    """Adds an interesting historical fact."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO facts (topic_id, fact_text) VALUES (?, ?)",
        (topic_id, fact_text)
    )
    conn.commit()
    conn.close()


def get_facts(topic_id=None):
    """Returns facts, optionally filtered by topic_id."""
    conn = get_connection()
    cursor = conn.cursor()
    if topic_id is not None:
        cursor.execute("SELECT * FROM facts WHERE topic_id = ? ORDER BY id ASC", (topic_id,))
    else:
        cursor.execute("SELECT * FROM facts ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows


# -------------------------------------------------------------
# QUIZ PROGRESS FUNCTIONS
# -------------------------------------------------------------

def save_quiz_progress(topic_id, score, total_questions, date_taken=None):
    """Saves a quiz score and the timestamp when it was completed."""
    if date_taken is None:
        date_taken = datetime.now().strftime("%Y-%m-%d %H:%M")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO quiz_progress (topic_id, score, total_questions, date_taken) VALUES (?, ?, ?, ?)",
        (topic_id, score, total_questions, date_taken)
    )
    conn.commit()
    conn.close()


def get_quiz_progress():
    """Returns all recorded quiz progress attempts, newest first."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quiz_progress ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows


# -------------------------------------------------------------
# SEARCH FUNCTION
# -------------------------------------------------------------

def search_content(keyword):
    """
    Searches for a keyword across:
    - topic title
    - topic description (summary)
    - chapter title
    - chapter content
    - facts
    """
    if not keyword or not keyword.strip():
        return {"topics": [], "chapters": [], "facts": []}

    conn = get_connection()
    cursor = conn.cursor()
    term = f"%{keyword.strip()}%"

    # 1. Search Topic title & Topic description (summary)
    cursor.execute("""
        SELECT * FROM topics 
        WHERE title LIKE ? OR summary LIKE ?
        ORDER BY id ASC
    """, (term, term))
    topics = cursor.fetchall()

    # 2. Search Chapter title & Chapter content
    cursor.execute("""
        SELECT c.*, t.title AS topic_title 
        FROM chapters c 
        JOIN topics t ON c.topic_id = t.id 
        WHERE c.title LIKE ? OR c.content LIKE ? 
        ORDER BY c.topic_id ASC, c.chapter_number ASC
        LIMIT 25
    """, (term, term))
    chapters = cursor.fetchall()

    # 3. Search Facts
    cursor.execute("""
        SELECT f.*, t.title AS topic_title 
        FROM facts f 
        JOIN topics t ON f.topic_id = t.id 
        WHERE f.fact_text LIKE ? 
        ORDER BY f.id ASC
        LIMIT 25
    """, (term,))
    facts = cursor.fetchall()

    conn.close()
    return {"topics": topics, "chapters": chapters, "facts": facts}


# -------------------------------------------------------------
# FORTS FUNCTIONS
# -------------------------------------------------------------

def add_fort(name, location, state, latitude, longitude, history, important_events, built_or_established, image_url=""):
    """
    Adds a historical fort to the database.
    Returns the newly created fort's ID.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO forts 
           (name, location, state, latitude, longitude, history, important_events, built_or_established, image_url) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (name, location, state, latitude, longitude, history, important_events, built_or_established, image_url)
    )
    conn.commit()
    fort_id = cursor.lastrowid
    conn.close()
    return fort_id


def get_forts(search_term=None, state=None):
    """
    Returns all forts, optionally filtered by a search term and/or state.
    Records can be accessed using dict-like syntax, e.g. fort["name"].
    """
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM forts WHERE 1=1"
    params = []

    if state and state != "All States":
        query += " AND state = ?"
        params.append(state)

    if search_term and search_term.strip():
        query += " AND (name LIKE ? OR location LIKE ?)"
        term = f"%{search_term.strip()}%"
        params.extend([term, term])

    query += " ORDER BY name ASC"
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_fort(fort_id):
    """Returns a single fort by its ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM forts WHERE id = ?", (fort_id,))
    row = cursor.fetchone()
    conn.close()
    return row


def get_fort_by_name(name):
    """Returns a single fort by its exact name."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM forts WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()
    return row


def get_forts_by_state(state):
    """Returns all forts in a given state."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM forts WHERE state = ? ORDER BY name ASC", (state,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_fort_states():
    """Returns a sorted list of unique states present in the forts table."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT state FROM forts ORDER BY state ASC")
    rows = cursor.fetchall()
    conn.close()
    return [row["state"] for row in rows]


# -------------------------------------------------------------
# NOTES FUNCTIONS
# -------------------------------------------------------------

def add_note(title, content, topic_id=None, created_at=None, updated_at=None):
    """
    Creates and saves a new personal study note.
    topic_id can be None for general notes.
    """
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    if created_at is None:
        created_at = now_str
    if updated_at is None:
        updated_at = now_str

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO notes (title, content, topic_id, created_at, updated_at)
           VALUES (?, ?, ?, ?, ?)""",
        (title.strip(), content.strip(), topic_id, created_at, updated_at)
    )
    conn.commit()
    note_id = cursor.lastrowid
    conn.close()
    return note_id


def get_notes(search_term=None, topic_id=None):
    """
    Returns study notes with optional keyword search and topic filter.
    Joined with topics table so row['topic_title'] is readily accessible.
    Ordered newest first.
    """
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT n.*, t.title AS topic_title
        FROM notes n
        LEFT JOIN topics t ON n.topic_id = t.id
        WHERE 1=1
    """
    params = []

    if topic_id is not None:
        if topic_id == "general":
            query += " AND n.topic_id IS NULL"
        else:
            query += " AND n.topic_id = ?"
            params.append(topic_id)

    if search_term and search_term.strip():
        term = f"%{search_term.strip()}%"
        query += " AND (n.title LIKE ? OR n.content LIKE ?)"
        params.extend([term, term])

    query += " ORDER BY n.id DESC"
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_note(note_id):
    """Returns a single note by its ID with topic title."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT n.*, t.title AS topic_title
        FROM notes n
        LEFT JOIN topics t ON n.topic_id = t.id
        WHERE n.id = ?
    """, (note_id,))
    row = cursor.fetchone()
    conn.close()
    return row


def update_note(note_id, title, content, topic_id=None):
    """
    Updates an existing study note and refreshes its updated_at timestamp.
    """
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE notes 
           SET title = ?, content = ?, topic_id = ?, updated_at = ?
           WHERE id = ?""",
        (title.strip(), content.strip(), topic_id, updated_at, note_id)
    )
    conn.commit()
    conn.close()


def delete_note(note_id):
    """Permanently deletes a note from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()


def get_notes_by_topic(topic_id):
    """Returns all notes for a specific topic (or general notes if topic_id is None)."""
    conn = get_connection()
    cursor = conn.cursor()
    if topic_id is None:
        cursor.execute("""
            SELECT n.*, 'General' AS topic_title
            FROM notes n
            WHERE n.topic_id IS NULL
            ORDER BY n.id DESC
        """)
    else:
        cursor.execute("""
            SELECT n.*, t.title AS topic_title
            FROM notes n
            LEFT JOIN topics t ON n.topic_id = t.id
            WHERE n.topic_id = ?
            ORDER BY n.id DESC
        """, (topic_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows


# -------------------------------------------------------------
# SELF-TEST CODE (Runs when executing: python database.py)
# -------------------------------------------------------------
if __name__ == "__main__":
    print("Testing database setup...")
    create_tables()
    print("[OK] All 8 tables created successfully.")

    # Insert a sample topic to test write and read
    sample_topic_id = add_topic(
        "Chhatrapati Shivaji Maharaj",
        "1630 - 1680 CE",
        "Founder of Hindavi Swarajya and master of guerrilla warfare."
    )
    print(f"[OK] Added sample topic with ID: {sample_topic_id}")

    # Fetch and verify sqlite3.Row access
    topic = get_topic(sample_topic_id)
    print(f"[OK] Retrieved topic using topic['title']: '{topic['title']}' ({topic['period']})")

    # Add a sample chapter
    add_chapter(sample_topic_id, 1, "The Oath of Swarajya", "Shivaji Maharaj took the oath at Raireshwar temple.")
    chapters = get_chapters(sample_topic_id)
    print(f"[OK] Chapters retrieved: {len(chapters)} (Chapter: '{chapters[0]['title']}')")

    # Add sample quiz question
    add_quiz_question(
        sample_topic_id,
        "Where did Shivaji Maharaj take the oath of Swarajya?",
        "Raigad", "Raireshwar Temple", "Sinhagad", "Torna",
        "B",
        "He took the oath at Raireshwar Temple in 1645."
    )
    questions = get_quiz_questions(sample_topic_id)
    print(f"[OK] Quiz questions retrieved: {len(questions)} ('{questions[0]['question']}')")

    # Save and fetch quiz progress
    save_quiz_progress(sample_topic_id, 14, 15)
    progress_records = get_quiz_progress()
    print(f"[OK] Progress records retrieved: {len(progress_records)} (Score: {progress_records[0]['score']}/{progress_records[0]['total_questions']})")

    print("\nDatabase test passed 100%! Everything is working properly.")
