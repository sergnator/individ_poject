from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/view/<filename>')
def html_render(filename):
    return render_template(f'{filename}.html')
