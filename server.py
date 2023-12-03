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


if __name__ == '__main__':
    app.run()
