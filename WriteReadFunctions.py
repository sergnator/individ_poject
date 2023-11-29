import datetime
import sqlite3
from MainClasses import *
import os


def check_password(username: str, password: str):
    con = sqlite3.connect('users.sqlite')
    cur = con.cursor()
    req = f'select * from users where username = "{username}"'
    response = cur.execute(req).fetchall()
    response = list(map(str, response))
    if len(response) == 0:
        raise NotFoundUsername('Такого пользователя нет')

    if response[0][2] == password:
        print(1)
        data = {'username': username, 'password': response[0][2], 'date': response[0][3]}
        return data
    raise MismatchPassword('Пароль не совпадает')


def write_error(message: str):
    if 'logs_error' not in os.listdir():
        os.mkdir('logs_error')
    now = datetime.datetime.now()
    path = f"logs_error\\{now.strftime('%c').replace(':', '.').replace(' ', '_')}.txt"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(message)


def create_user(username: str, password: str):
    date = datetime.date.today()
    con = sqlite3.connect('users.sqlite')
    cur = con.cursor()
    req = f'insert into users(username, password, date) values({username}, {password}, {date})'
    try:
        cur.execute(req)
    except sqlite3.IntegrityError:
        raise NicknameIsBusy('Такое имя пользователя уже используется')
    con.commit()
    con.close()


create_user(input(), input())
