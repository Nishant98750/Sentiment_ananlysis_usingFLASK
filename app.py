from flask import Flask
app = Flask(__name__)
from flask import render_template

@app.route('/')
def home():
    return render_template("home_page.html")
@app.route('/user')
def users():
    return 'users'
@app.route('/user/<username>')
def username(username):
    return username