import sys
sys.path.insert(0,'/Users/kuku/Desktop/anaconda')
from titanic.entity import Entity
from titanic.service import Service

class Controller:
    def __init__(self):
        pass

if __name__ == '__main__':
    api = Controller()
    service = Service()
    service.naver_cartoon('https://comic.naver.com/webtoon/weekday.nhn')