import sqlite3

from os import exists

class PostsDatabase:
    def __init__(self, username):
        self.db_path = f'./db/{username}.db'

        self.connection = sqlite3.connect(self.db_path, check_same_thread=False, isolation_level=None)

        if not exists(self.db_path):
            self.create_tables()

    def create_tables(self):
        self.connection.execute(
            'CREATE TABLE posts (\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                post_id INTEGER NOT NULL,\
                username TEXT NOT NULL,\
                body TEXT NOT NULL,\
                date TEXT DEFAULT CURRENT_TIMESTAMP,\
                UNIQUE(post_id, username)\
            );'
        )

    def insert_post(self, post_id : int, username : str, body : str):
        self.connection.execute(
            'INSERT INTO posts (post_id, username, body) VALUES (?, ?, ?);',
            (post_id, username, body)
        )

    def get_posts_for_user(self, username):
        cursor = self.connection.execute(
            'SELECT * FROM posts WHERE username = ? SORT BY date DESC;',
            (username,)
        )

        return cursor.fetchall()