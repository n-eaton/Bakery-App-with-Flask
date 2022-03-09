from app import app
from flask import render_template



@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/about')
def about():
    return  render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cupcakes')
def cupcakes():
    return render_template('cupcakes.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')