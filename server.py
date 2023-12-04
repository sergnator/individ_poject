import json

from flask import Flask, request, url_for, render_template

from WriteReadFunctions import *

app = Flask(__name__)


@app.route('/view/<filename>')
def html_render(filename):
    return render_template(f'{filename}.html')


@app.route('/')
def main():
    return html_render('index')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        data_of_user = check_password(data['username'], data['passwrod'])
    except BasePostsException:
        return '-1'
    return data_of_user['id']


@app.route('/registration', methods=['POST'])
def registration():
    data = request.get_json()
    try:
        data_of_user = create_user(data['username'], data['passwrod'])
    except BasePostsException:

        return '-1'

    return data_of_user['id']


@app.route('/posts')
def get_posts():
    response = get_posts_from_data_base()
    response = map(str, response)
    response = map(lambda x: x.replace("'", '"'), response)
    response = '/n'.join(response)
    return response


@app.route('/username', methods=['POST'])
def get_username():
    data = request.get_data()
    data_of_user = get_username_from_database(int(data))
    return data_of_user


@app.route('/newPost', methods=['POST'])
def new_post():
    data = request.get_json()

    username = get_username_from_database(data['id_of_user'])
    content = data['content']
    create_post(username, content)
    return '1'


if __name__ == '__main__':
    app.run()
