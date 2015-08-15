__author__ = '天祥'

from init import app

@app.route('/')
@app.route('/home')
def index():
    return 'Hello, World!'
