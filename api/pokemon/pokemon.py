from flask_restx import Api, Resource
from flask import Blueprint
from psycopg2 import sql
from api.db.pool_management import get_curs

pokemon_bp = Blueprint('pokemon', __name__)

pokemon = Api(pokemon_bp)


@pokemon.route('/pokemon')
class Pokemon(Resource):
    def get(self):
        with get_curs() as curs:
            curs.execute("SELECT * FROM POKEMON")
            result = curs.fetchall()
        if not result:
            return {'message': 'database unavailable'}, 404
        return result, 200



@pokemon.route('/pokemon/<int:id>')
class Pokemon(Resource):
    def get(self, id):
        with get_curs() as curs:
            curs.execute(sql.SQL("SELECT * FROM POKEMON WHERE ID = %s "), (id,))
            result = curs.fetchall()
        if not result:
            return {'message': 'database unavailable'}, 404
        return result, 200