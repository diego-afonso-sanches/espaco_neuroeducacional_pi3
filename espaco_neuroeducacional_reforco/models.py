from espaco_neuroeducacional_reforco import database
from datetime import datetime

class Mensagem(database.Model):
    __tablename__ = 'Mensagem'
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(120), nullable=False)
    email = database.Column(database.String(120), nullable=False)
    telefone = database.Column(database.String(11), nullable=False)
    mensagem = database.Column(database.Text, nullable=False)
    enviado_em = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Mensagem {self.id} {self.email}>'


