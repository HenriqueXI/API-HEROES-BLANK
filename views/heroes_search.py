from flask_restful import Resource
from flask import request
from models.hero import Hero


class HeroesSearchHandler(Resource):
    """Heroes Serach Handler"""
    def get(self):
        """Get heroes"""
        try:
            heroes = Hero.search(request.args.get('name'))
            response = {
                'heroes': []
            }

            for hero in heroes:
                response['heroes'].append(hero.to_dict())

            if response['heroes']:
                return response['heroes']
            return {'message': 'Bad request, param name is required'}, 400

        except Exception as error:
            return {
                       'message': 'Bad request, param name is required'
                   }, 500

