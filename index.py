import json
from random import randint
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

counter = 0


@app.route('/member')
def memeber():
    with open('templates/news.json', 'r', encoding='utf-8') as js_f:
        js_file = json.load(js_f)['persons']
    return render_template('member.html', title='Колония марса', data=js_file)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
