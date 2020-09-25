import sys
sys.path.insert(0, '/Users/kuku/Desktop/anaconda')

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from util.file_handler import FileReader
import pandas as pd
import numpy as np
import tensorflow as tf
from dataclasses import dataclass

@dataclass
class Cabbage :
    '''
    year,avgTemp,minTemp,maxTemp,rainFall,avgPrice
    20100101,-4.9,-11,0.9,0,2123
    '''
    year: int = 0
    avgTemp: float = 0.0
    minTemp: float = 0.0
    maxTemp: float = 0.0
    rainFall: int = 0
    avgPrice: int = 0

    def __init__(self):
        self.fileReader = FileReader()  # Autowired Entity entity
        self.context = '/Users/kuku/Desktop/anaconda/price_prediction/data/'

    def new_model(self, payload) -> object:
        this = self.fileReader
        this.context = self.context
        this.fname = payload
        return pd.read_csv(this.context + this.fname, sep=',')

    def create_tf(self, payload):
        xy = np.array(payload, dtype=np.float32)
        x_data = xy[:,1:-1] # feature
        y_data = xy[:,[-1]] # price
        X = tf.compat.v1.placeholder(tf.float32, shape=[None, 4])
        Y = tf.compat.v1.placeholder(tf.float32, shape=[None, 1])
        W = tf.Variable(tf.random.normal([4, 1]), name='weight')
        b = tf.Variable(tf.random.normal([1]), name='bias')
        hyposthesis = tf.matmul(X, W) + b
        cost = tf.reduce_mean(tf.square(hyposthesis - Y))
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.000005)
        train = optimizer.minimize(cost)
        sess = tf.compat.v1.Session()
        sess.run(tf.compat.v1.global_variables_initializer())
        for step in range(100000):
            cost_, hypo_, _ = sess.run([cost, hyposthesis, train],
                                        feed_dict={X: x_data, Y: y_data})
            if step % 500 == 0:
                print(f'# {step} 손실비용: {cost_} ')
                print(f'- 배추가격 : {hypo_[0]}')

        saver = tf.compat.v1.train.Saver()
        saver.save(sess, self.context+'saved_model.ckpt')
        print('저장완료')

    def test(self):
        self.avgPrice = 100
        return self.avgPrice

    def service(self):
        X = tf.compat.v1.placeholder(tf.float32, shape=[None,4])
        # year,avgTemp,minTemp,maxTemp,rainFall,avgPrice
        # 에서 avgTemp,minTemp,maxTemp,rainFall 입력받겠다.
        # year 는 모델에서 필요없는 값이다 -> 상관관계없음
        # avgPrice 는 얻고자 하는 답. 종속변수
        # avgTemp,minTemp,maxTemp,rainFall 는 종속변수를 결정하는 독립변수
        # 그리고 avgPrice 를 결정하는 요소로 사용되는 파라미터(이것이 중요)
        # 이제 우리는 통계와 확률로 들어가야 합니다. 용어를 먼저 잘 정의 합시다.
        # y = ax + b 선형관계 linear 
        # X 는 대문자를 사용 확률변수라고 한다.

        w = tf.Variable(tf.random.normal([4,1]), name= 'weight')
        b = tf.Variable(tf.random.normal([1]), name= 'bias')
        # 텐서에서 변수는 웹에서 변수와 다르다.
        # 이 변수를 결정하는 것은 외부 값이 아니라 텐서가 내부에서 사용하는 변수이다.
        # 기존 웹에서 사용하는 변수는 placeholder 이다 

        saver = tf.train.Saver()
        with tf.Session() as sess :
            sess.run(tf.compat.v1.global_variables_initializer())
            saver.restore(sess, self.context +'saved_model.ckpt')
            data = [[self.avgTemp,self.minTemp,self.maxTemp,self.rainFall],]
            arr = np.array(data, dtype = np.float32)
            dict = sess.run(tf.matmul(X,w) + b, {X: arr[0:4]})
            # Y = wx + b 를 코드로 표현하면 위 처럼 
            # matmul matrix 구조
            
            print(dict[0])
        return int(dict[0])

if __name__ == '__main__':
    m = Cabbage()
    '''
    dframe = m.new_model('price_data.csv')
    print(dframe.head())
    m.create_tf(dframe)
    m.avgPrice = 1
    '''
   
    print(m.test())