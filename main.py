"""Arquivo main da API"""
from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask_cors import CORS

# imports para o firebase
import firebase_admin
from firebase_admin import firestore, credentials

# Aqui iniciamos a API
from views.heroes import HeroesHandler, HeroHandler
from views.heroes_search import HeroesSearchHandler
from views.top_heroes import TopHeroesHandler

app = Flask(__name__)
CORS(app)
API = Api(app)

# Iniciando o firebase com as credenciais que você salvou na raiz
cred = credentials.Certificate("./projeto-tuor-of-heros-firebase-adminsdk-gk6pb-73ed5118ce.json")


firebase_admin.initialize_app(credential=cred)
FIRESTORE_DB = firestore.client()


@app.before_request
def start_request():
    """Start api request"""
    if request.method == 'OPTIONS':
        return '', 200
    if not request.endpoint:
        return 'Sorry, Nothing at this URL.', 404


# Nossa classe principal


class Index(Resource):
    """ class return API index """

    def get(self):
        """return API"""
        return {"API": "Heroes"}

    # Vamos criar esse metodo somente para ficar mais facil fazer o mock dele
    # nos testes
    @staticmethod
    def get_firestore_db():
        """Get firestore db instance"""
        return FIRESTORE_DB


# Nossa primeira url
API.add_resource(Index, '/', endpoint='index')
API.add_resource(HeroesHandler, '/heroes', endpoint='heroes')
API.add_resource(HeroHandler, '/hero/<hero_id>', endpoint='hero')
API.add_resource(TopHeroesHandler, '/top-heroes', endpoint='top-heroes')
API.add_resource(HeroesSearchHandler, '/search', endpoint='search')

if __name__ == '__main__':
    # Isso é utilizado somente para executar a aplicação local. Quando
    # realizarmos o deploy para o Google App Engine, o webserver deles ira
    # iniciar a aplicação de outra forma
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
