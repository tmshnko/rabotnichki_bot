import sqlite3
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "bot.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_votes (
            user_id INTEGER,
            username TEXT,
            choice TEXT,
            vote_date TEXT,
            PRIMARY KEY (user_id, vote_date)
        )
        """)
        conn.commit()

def save_vote(user_id: int, username: str, choice: str):
    today = str(date.today())

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO daily_votes (user_id, username, choice, vote_date)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(user_id, vote_date)
        DO UPDATE SET choice=excluded.choice
        """, (user_id, username, choice, today))

        conn.commit()

def get_user_vote(user_id: int):
    today = str(date.today())

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT choice FROM daily_votes
        WHERE user_id=? AND vote_date=?
        """, (user_id, today))

        return cursor.fetchone()
    
def get_today_stats():
    today = str(date.today())

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT choice, COUNT(*)
        FROM daily_votes
        WHERE vote_date=?
        GROUP BY choice
        """, (today,))

        return cursor.fetchall()
    
def clear_old_votes():
    today = str(date.today())

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM daily_votes
        WHERE vote_date != ?
        """, (today,))
        conn.commit()