import sys
sys.path.insert(0,'/Users/kuku/Desktop/anaconda')
from titanic.entity import Entity
from titanic.service import Service

class Controller:
    def __init__(self):
        print('test')
        self.service = Service()
        self.entity = Entity()

    def preprocessing(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train) # payload
        this.test = service.new_model(test)
        return this

    def modeling(self,train,test):
        service = self.service
        this = self.preprocessing(train, test)
        print('훈련 컬럼 : {this.train.columns')
        this.label = service.create_label(this)
        this.train = service.create_train(this)

    def learning(self):
        pass 

    def submit(self):
        pass

if __name__ == "__main__":
    ctrl = Controller()
    ctrl.modeling('train.csv', 'test.csv')
