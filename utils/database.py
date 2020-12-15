"""
Concerned with storing and retrieving Dramas from a json.file
format of the json file:
"""
#import json
from .database_connection import DatabaseConnection
from typing import List, Dict

Drama = List[Dict]


def create_drama_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS dramas(name text primary key, episodes text, watched integer)')


# to make sure the file is created before starting the program


def add_drama(name: str, episodes: int) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO dramas VALUES(?,?,0)', (name, episodes))


def get_all_dramas() -> Drama:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM dramas')
        dramas = [{'name': row[0], 'episodes': row[1], 'watched': row[2]} for row in cursor.fetchall()]

    return dramas


def mark_drama_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE dramas SET watched= 1 WHERE name =?', (name,))


def delete_drama(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM dramas WHERE name=?', (name,))


