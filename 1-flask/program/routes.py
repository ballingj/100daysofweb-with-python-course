from program import app
import requests

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/100days')
def hundred_days():
    return render_template('100days.html')

@app.route('/table')
def table():
    data = [
        {
        "nsfw": "Jane",
        "religious": False,
        "political": False,
        "racist": False,
        "sexist": False,
        "explicit": False
        },
        {
        "nsfw": "John",
        "religious": False,
        "political": False,
        "racist": False,
        "sexist": False,
        "explicit": False
        },
        {
        "nsfw": "James",
        "religious": False,
        "political": False,
        "racist": False,
        "sexist": False,
        "explicit": False
        },
    ]

    return render_template('table.html', data=data)

@app.route('/advice')
def advice():
    res = requests.get("https://api.adviceslip.com/advice", headers={"Accept": "application/json"})
    print(res.text)

    # output the response in json format
    data = res.json()

    return render_template('advice.html', data=data["slip"]["advice"])


@app.route('/joke')
def joke():
    res = requests.get("https://icanhazdadjoke.com", headers={"Accept": "application/json"})
    print(res.text)

    # output the response in json format
    data = res.json()

    return render_template('joke.html', data=data["joke"])

