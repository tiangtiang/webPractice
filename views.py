__author__ = '天祥'

from init import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'tiang'}
    posts = [
        {'author': {'name': 'ling'}, 'body': 'tiang is a sb!'},
        {'author': {'name': 'annie'}, 'body': 'go to type code!!!'}
    ]
    return render_template('index.html', user = user, title = 'Home Page', posts = posts)
