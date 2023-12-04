import datetime
import sqlite3
from MainClasses import *
import os


def check_password(username: str, password: str):
    con = sqlite3.connect('users.sqlite')
    cur = con.cursor()
    req = f'select * from users where username = "{username}"'
    response = cur.execute(req).fetchall()
    response = response[0]
    response = list(map(str, response))
    cur.close()
    con.cursor().close()
    con.close()
    if len(response) == 0:
        raise NotFoundUsername('Такого пользователя нет')

    if response[2] == password:
        data = {'id': response[0], 'username': username, 'password': response[2], 'date': response[3]}
        return data
    raise MismatchPassword('Пароль не совпадает')


def write_error(message: str):
    if 'logs_error' not in os.listdir():
        os.mkdir('logs_error')
    now = datetime.datetime.now()
    path = f"logs_error\\{now.strftime('%c').replace(':', '.').replace(' ', '_')}.txt"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(message)


def get_username_from_database(id_: int):
    con = sqlite3.connect('users.sqlite')
    cur = con.cursor()
    req = f'select * from users where id="{id_}"'
    data = cur.execute(req).fetchall()
    data = data[0]
    cur.close()
    con.close()
    return data[1]


def get_posts_from_data_base():
    con = sqlite3.connect('posts.sqlite')
    cur = con.cursor()
    req = f'select * from posts'
    data = cur.execute(req).fetchall()
    result = []
    for el in data:
        result.append({'id': str(el[0]), 'content': el[1], 'date': el[2], 'username': el[3]})
    cur.close()
    con.close()
    return result


def create_post(username: int, content: str):
    con = sqlite3.connect('posts.sqlite')
    cur = con.cursor()
    date = datetime.date.today()
    req = f'insert into posts(username, date, content) values("{username}", "{date}", "{content}")'
    cur.execute(req)
    con.commit()
    cur.close()
    con.close()


def create_user(username: str, password: str):
    date = datetime.date.today()
    con = sqlite3.connect('users.sqlite', timeout=1)
    cur = con.cursor()
    req = f'insert into users(username, password, date) values("{username}", "{password}", "{date}")'
    try:
        cur.execute(req)
        con.commit()
    except sqlite3.IntegrityError:
        cur.close()
        con.close()
        raise NicknameIsBusy('Такое имя пользователя уже используется')

    req = f'select * from users where username = "{username}"'
    response = cur.execute(req).fetchall()
    response = response[0]
    response = list(map(str, response))
    cur.close()
    con.close()
    return {'id': response[0], 'username': username, 'password': response[2], 'date': response[3]}
