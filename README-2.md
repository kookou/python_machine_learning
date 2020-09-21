클래스 하나가 단위 unit 이 됩니다.
이제 확장을 하겠습니다.
객체지향에서는 디자인 패턴이라는 개념이 존재한다.

패턴조합을 통해 큰 개념의 패턴 -> MVC 패턴 이라고 한다.
model, view, controller 이렇게 조합한다. -> java , c 언어에서 주로 사용하는 개념

model : 데이터 처리 -> API 서버 -> python -> Tensorflow
view : 화면 UI 처리 -> UI 서버 -> Reactjs
controller : model+view 를 연결

titanic 폴더에
dataset (test.csv, train.csv)이 존재하고
entitu(속성) + service(기능) = 객체(object)

def __init__(self, ..) =>속성
def abc(): =>기능
결국 class 는 객체를 정의하는 것이다.
class 가 여러개 (entity, service) 모여서 다시 큰 개념의 객체를 이룬다. 그때 이것은 클래스라 하지 않고 model 이라고 한다.
패키지는 같은 컨셉을 공유하는 클래스의 집합 .. 모듈-(진화 속성(entity가 존재하면))->모델
모델에 AI 개념이 없으면 web에서 말하는 모델이고
AI 개념이 존재하면 인공지능 모델이 된다.

여기서 AI 개념이라고 하면 머신러닝 (기계학습) 코딩의 유무 
dataset 을 추가하면 이를 지도학습 이라고 한다.
dataset 이 없으면 비 지도 학습이라고 한다.
지금 타이타닉은 dataset을 모델에 넣었으므로 지도학습을 하겠다는 의미가 된다.
