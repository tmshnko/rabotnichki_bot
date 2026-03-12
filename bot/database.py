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

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS daily_message (
                vote_date TEXT PRIMARY KEY,
                chat_id INTEGER,
                message_id INTEGER
            );""")
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

def save_daily_message(chat_id: int, message_id: int):
    from datetime import date
    today = str(date.today())

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT OR REPLACE INTO daily_message (vote_date, chat_id, message_id)
        VALUES (?, ?, ?)
        """, (today, chat_id, message_id))
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
    
def get_daily_message():
    from datetime import date
    today = str(date.today())

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT chat_id, message_id
        FROM daily_message
        WHERE vote_date=?
        """, (today,))
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

def get_today_votes():
    from datetime import date
    today = str(date.today())

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT username, choice
        FROM daily_votes
        WHERE vote_date=?
        """, (today,))
        return cursor.fetchall()