import sys
sys.path.insert(0, '/Users/kuku/Desktop/anaconda/sba_api_04')

from flask_restful import Resource
from flask import Response, jsonify
from com_bita.food.food_dao import FoodDao

class FoodsApi(Resource):

    def __init__(self):
        self.dao = FoodDao()

    def get(self):
       foods = self.dao.select_foods()
       return jsonify(foods[0])