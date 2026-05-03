import pytest
from espaco_neuroeducacional_reforco import app, database
from espaco_neuroeducacional_reforco.models import Mensagem
from espaco_neuroeducacional_reforco.forms import ContatoForm

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False  # Desabilitar CSRF para testes
    with app.test_client() as client:
        with app.app_context():
            database.create_all()
        yield client
        with app.app_context():
            database.drop_all()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Espa' in response.data  # Assumindo que o template tem 'Espaço Neuroeducacional' ou similar

def test_sobre_mim(client):
    response = client.get('/sobre_mim')
    assert response.status_code == 200

def test_avaliacao(client):
    response = client.get('/avaliacao')
    assert response.status_code == 200

def test_localizacao(client):
    response = client.get('/localizacao')
    assert response.status_code == 200

def test_contato_get(client):
    response = client.get('/contato')
    assert response.status_code == 200
    assert b'form' in response.data

def test_contato_post_valid(client):
    data = {
        'nome': 'Teste Nome',
        'email': 'teste@example.com',
        'telefone': '12345678901',
        'mensagem': 'Esta é uma mensagem de teste com pelo menos 10 caracteres.'
    }
    response = client.post('/contato', data=data, follow_redirects=True)
    assert response.status_code == 200
    # Verificar se a mensagem foi salva
    with app.app_context():
        mensagem = Mensagem.query.first()
        assert mensagem is not None
        assert mensagem.nome == 'Teste Nome'
        assert mensagem.email == 'teste@example.com'

def test_contato_post_invalid(client):
    data = {
        'nome': '',
        'email': 'invalid-email',
        'telefone': '',
        'mensagem': 'Short'
    }
    response = client.post('/contato', data=data)
    assert response.status_code == 200
    # Verificar se não foi salva
    with app.app_context():
        mensagens = Mensagem.query.all()
        assert len(mensagens) == 0

def test_model_mensagem():
    with app.app_context():
        database.create_all()
        mensagem = Mensagem(nome='Nome', email='email@test.com', telefone='123', mensagem='Mensagem longa')
        database.session.add(mensagem)
        database.session.commit()
        assert mensagem.id is not None
        assert str(mensagem) == '<Mensagem 1 email@test.com>'
        database.drop_all()

def test_form_contato():
    with app.app_context():
        form = ContatoForm()
        assert form.nome is not None
        assert form.email is not None
        assert form.telefone is not None
        assert form.mensagem is not None
        assert form.enviar is not None
