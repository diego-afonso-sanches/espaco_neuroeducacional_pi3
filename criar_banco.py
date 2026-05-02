from espaco_neuroeducacional_reforco import database, app
from espaco_neuroeducacional_reforco.models import Mensagem

with app.app_context():
    database.create_all()