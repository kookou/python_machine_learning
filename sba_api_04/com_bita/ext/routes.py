import sys
sys.path.insert(0, '/Users/kuku/Desktop/anaconda/sba_api_04')

from com_bita.food.food_api import FoodsApi

def initialize_routes(api):
    api.add_resource(FoodsApi, '/api/foods')