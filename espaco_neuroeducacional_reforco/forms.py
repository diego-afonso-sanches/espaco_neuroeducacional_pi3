from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional

class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(message="Nome é obrigatório"), Length(max=120)])
    email = StringField('E-mail', validators=[DataRequired(message="E-mail é obrigatório"), Email(message="E-mail inválido"), Length(max=120)])
    telefone = StringField('Telefone', validators=[Optional(), Length(max=11)])
    mensagem = TextAreaField('Mensagem', validators=[DataRequired(message="Mensagem é obrigatória"), Length(min=10, message="A mensagem deve ter ao menos 10 caracteres.")])
    enviar = SubmitField('Enviar')