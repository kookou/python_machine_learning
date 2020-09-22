머신러닝 = 기계학습 = ML( == Deep Learning)
ML 종류 : 지도, 비지도, 강화
ML Process : (데이터)정형화(preprocessing/전처리) > 모델링 > 러닝 > 평가 

ML Algorithm
1. 퍼셉트론(perceptron) -> 뉴런 (neuron)
2. 회귀 rgs
3. 분류 cls
4. SVM
5. Dtree
6. kmean
7. PCA
8. R-forest -> RF
9. NLP
10. Deep learning -> DL

여기까지가 chap 13 
지도를 외우듯이 외워라 

Tensorflow

---------------------------------------

비지니스 로직
processing 하는 파일명 
processing
modeling
learning
evaluation
완성 되면 submit(파일로 저장)

# 외부에 있는 파이선 파일(.py)를 import 해야 속성, 기능을 사용할 수 있다.
# 내부에서는 이것을 인스턴스화(instance) 해야한다
# entity = Entity()
# 이떄 소문자 entity 는 인스턴스라고 하고 이를 객채로 정의한다.
# 대문자 Entitiy는 클래스
# 라운드 브레이스가 있는 Entity()는 생성자 라고 한다.
# 객체지향(OOP) 에서는 속성과 기능을 호출하는 구조로 두가지 방식이 있는데
# calc = Calculator() 에서
# calc 는 인스턴스 객체가 되고
# Calculator 는 클래스 객체(스테틱)라고 한다.
# calc.sum() 하면 인스턴스 호출방식 = 다이나믹
# Calculator.sum() 하면 클래스 호출방식 = 스태틱 이라고 한다.


----------------------------------------------------
페이로드 / payload (컴퓨팅) : 전송되는 데이터 

# this.fname = payload ~> setter 할당연산자 (=) 있으면 setter
# this.fname 만 있으면  ~> getter 할당연산자 (=) 없으면 getter


PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked  => 메타데이터 = 스키마 = features = variables = property
1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S => row, 행, 인스턴스, raw 데이터
2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C

차원 (dim)
variable x = 3 스칼라 값, 0차원
array    [] = {1,2,3} 백터개념, 1차원이 되고 variable 은 element 가 된다.
matrix  [[]] = {{1,2,3}, {4,5,6}} 매트릭스 2차원 data frame, array 라 하지않고 vector 라고 한다.

------------------------------------------------------
지도학습에서 반드시 해야할 일은 dataset을 생성하는 것이다.
그때 dataset은 반드시 train, test 두가지 형태로 작성한다. 
