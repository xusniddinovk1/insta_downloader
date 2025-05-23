import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_user(self, full_name, username, chat_id, lang):
        self.cur.execute("""INSERT INTO users(full_name, username, chat_id, lang) values (?, ?, ?, ?)""",
                         (full_name, username, chat_id, lang))
        self.conn.commit()

    # def update_user_data(self, chat_id, key, value):
    #     self.cur.execute(f"""UPDATE user SET {key} = ? WHERE chat_id = ?""", (value, chat_id))
    #     self.conn.commit()

    def get_user_by_chat_id(self, chat_id):
        self.cur.execute("""SELECT * FROM users WHERE chat_id = ?""", (chat_id,))
        user = dict_fetchone(self.cur)
        return user


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))

db = Database('insta_save.db')
