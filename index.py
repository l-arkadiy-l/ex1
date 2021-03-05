import json
from random import randint
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

images = ['static/images/Artceram.jpg', 'static/images/AXOR.jpg', 'static/images/AZZURRA.jpg']
counter = 0

@app.route('/member')
def memeber():
    with open('templates/news.json', 'r', encoding='utf-8') as js_f:
        js_file = json.load(js_f)['persons']
        random = randint(0, len(js_file) - 1)
        ans = js_file[random]
        name = ans['name']
        surname = ans['surname']
        image = ans['image']
        job = ans['job']
        print(image, name, surname, job)
    return render_template('member.html',title='Колония марса', list_person=[name, surname, job], image=url_for('static', filename=f'images/{image}'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
