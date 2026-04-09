from flask import render_template, url_for
from espaco_neuroeducacional_reforco import app

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/sobre_mim')
def sobre_mim():
    return render_template('sobre_mim.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')
