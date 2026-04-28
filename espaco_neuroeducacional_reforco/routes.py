from flask import render_template, url_for, redirect
import espaco_neuroeducacional_reforco
from espaco_neuroeducacional_reforco import app, database
from espaco_neuroeducacional_reforco.forms import ContatoForm
from espaco_neuroeducacional_reforco.models import Mensagem

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/sobre_mim')
def sobre_mim():
    return render_template('sobre_mim.html')

@app.route('/avaliacao')
def avaliacao():
    return render_template('avaliacao.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        mensagem_recebida = Mensagem(nome=form.nome.data, email=form.email.data, telefone=form.telefone.data, mensagem=form.mensagem.data)
        database.session.add(mensagem_recebida)
        database.session.commit()
        return redirect(url_for('contato'))
    return render_template('contato.html', form=form)

@app.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')




