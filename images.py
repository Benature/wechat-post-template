import sqlite3
import os
import requests
from urllib.parse import unquote
from config import Authorization
from pathlib import Path


class ImageHost:

    def __init__(self, db_name='image_host.db'):
        self.db_name = db_name
        self.initialize_database()
        self.header = {
            # "Content-Type": "multipart/form-data",
            "Authorization": Authorization
        }

    def initialize_database(self):
        Path("temp").mkdir(parents=True, exist_ok=True)
        if not os.path.exists(self.db_name):
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS images (
                    url TEXT PRIMARY KEY,
                    file_path TEXT,
                    file_id INTERGER,
                    width INTEGER,
                    height INTEGER,
                    filename TEXT,
                    storename TEXT,
                    size INTEGER,
                    path TEXT,
                    hash TEXT,
                    delete_link TEXT,
                    page TEXT
                )
            ''')
            conn.commit()
            conn.close()

    def upload(self, fn):
        self.initialize_database()

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM images WHERE file_path=?', (fn, ))
        existing_entry = cursor.fetchone()

        if existing_entry:
            conn.close()
            return existing_entry[0]  # Return URL from the database

        with open(unquote(fn), 'rb') as f:
            files = {'smfile': f}
            res = requests.post("https://sm.ms/api/v2/upload",
                                headers=self.header,
                                files=files)

        if res.status_code == 200:
            # print(res.content)
            resj = res.json()
            if resj['code'] == "image_repeated":
                url = resj['images']
                data = dict(url=url)
            else:
                data = res.json()['data']
                data['delete_link'] = data['delete']
                del data['delete']
            data.update(dict(file_path=fn))

            sql = f'''
                INSERT INTO images ({', '.join(data.keys())})
                VALUES ({', '.join(['?'] * len(data))})
            '''
            cursor.execute(sql, list(data.values()))
            conn.commit()
            conn.close()
            return data['url']
        else:
            conn.close()
            return None
