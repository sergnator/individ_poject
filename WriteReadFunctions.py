import sqlite3
import datetime
from MainClasses import *


def check_password(username: str, password: str):
    con = sqlite3.connect('users.sqlite')
    cur = con.cursor()
    req = f'select * from users where username = "{username}"'
    response = cur.execute(req).fetchall()
    response = list(map(str, response))
    if len(response) == 0:
        con.close()
        raise NotFoundUsername('Такого пользователя нет')

    if response[0][2] == password:
        print(1)
        data = {'username': username, 'password': response[0][2], 'date': response[0][3]}
        con.close()
        return data
    con.close()
    raise MismatchPassword('Пароль не совпадает')


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
