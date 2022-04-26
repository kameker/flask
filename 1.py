from flask import Flask, url_for
from random import sample

app = Flask(__name__)


@app.route('/')
def _():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    text = ["Человечество вырастает из детства.",

            "Человечеству мала одна планета.",

            "Мы сделаем обитаемыми безжизненные пока планеты.",

            "И начнем с Марса!",

            "Присоединяйся!"]
    return '</br>'.join(text)


@app.route('/image_mars')
def image_mars():
    return f'''<h1>Жди нас, Марс!</h1><img src="{url_for('static', filename='img/MARS.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                <head>
                <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <h2 class="title"> <span>Человечество вырастет из детства</span> </h2>
                    <h3 class="title2"> <span2>Человечеству мала одна планета</span2> </h3>
                    <h3 class="title3"> <span3>Мы сделаем обитаемыми пока безжизненые планеты</span3> </h3>
                    <h4 class="title4"> <span4>И начнём мы с марса</span4> </h4>
                    <h5 class="title5"> <span5>И начнём мы с марса</span5> </h5>
                  </body>
                </html>"""


@app.route('/choice/<planet>')
def choice(planet):
    words = ["мир;", "труд;", "колония;", "планета;", "вода;"]
    lwords = sample(words, 5)
    return f"""<!doctype html>
                    <html lang="en">
                    <head>
                    <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                      </head>
                      <body>
                        <h1>Моё предложение: {planet}</h1>
                        <h2 class="title"> <span>{lwords[0]}</span> </h2>
                        <h3 class="title2"> <span2>{lwords[1]}</span2> </h3>
                        <h3 class="title3"> <span3>{lwords[2]}</span3> </h3>
                      </body>
                    </html>"""

@app.route('/result/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                        <html lang="en">
                        <head>
                        <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h2>Претендент на участие в миссии {nickname}: </h2>
                            <h3 class="title"> <span>Поздравляем! вам рейтинг после {level} этапа отбора</span> </h3>
                            <h4 class="title2">составляет {rating}!</h4>
                            <h5 class="title3"><span2>Желаем удачи!</span2></h5>
                          </body>
                        </html>"""
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
