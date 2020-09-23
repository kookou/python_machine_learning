import sys
sys.path.insert(0,'/Users/kuku/Desktop/anaconda')

from titanic.entity import Entity
import numpy as np
import pandas as pd

'''
PassengerId  고객ID,
Survived 생존여부, -> 머신러닝 모델이 맞춰야 할 답 
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼

'''

class Service:
    def __init__(self):
        self.entity = Entity()  # Autowired Entity entity

    def new_model(self, payload)-> object: #페이로드 / payload (컴퓨팅) : 전송되는 데이터 
        this = self.entity
        this.context = './data'
        this.fname = payload
        return pd.read_csv(this.context + this.fname) # p.139 df = tensor
        # this.fname = payload ~> setter 할당연산자 (=) 있으면 setter
        # this.fname 만 있으면  ~> getter 할당연산자 (=) 없으면 getter

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1) # train 은 답이 제거된 데이터 셋이다. * 서바이벌을 축으로 빼라.
    
    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived'] # label 은 곧 답이된다.

    @staticmethod
    def drop_feature(this,feature)-> object:
        this.train = this.trian.drop([feature], axis =1) 
        this.test = this.test.drop([feature], axis =1) # p.149에 보면 훈련셋 테스트셋 이 나누어져 있다.
