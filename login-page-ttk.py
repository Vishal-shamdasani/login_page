import sqlite3

conn=sqlite3.connect("user_db.db")

cor=conn.cursor()
cor.execute('''
CREATE TABLE IF NOT EXISTS users (
            USERNAME TEXT PRIMARY KEY,
            PASSWORD TEXT NOT NULL,
            NAME TEXT NOT NULL,
            AGE INTEGER NOT NULL,
            EMAIL TEXT NOT NULL)
''')

cor.execute('''
INSERT INTO users (USERNAME,PASSWORD,NAME,AGE,EMAIL) VALUES
            ('USER1','PAS123','BOB',34,'user1@gmail.com'),
            ('USER2','PAS456','tim',34,'user2@gmail.com'),
            ('USER3','PAS789','jeff',34,'user3@gmail.com')
            ''')

conn.commit()
conn.close()