import sqlite3
from MainClasses import *


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


check_password(input(), input())
