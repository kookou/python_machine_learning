class Entity :
    def __init__(self, context, fname, train, test, id, label):
        self._context = context # _ 1개 는 default 접근 의미 , __2개는 preivate 접근의미
        self._fname = fname
        self._train = train
        self._id = id
        self._label = label
        # 나머지는 완성

    #context get,set 를 만든다.
    @property
    def context(self) -> str: # -> : return 하는 결과값이 str(스트링)이다.
        return self._context

    @context
    def context(self, context):
        self._context = context

    #fname get,set 를 만든다.
    @property
    def fname(self) -> str: # -> : return 하는 결과값이 str(스트링)이다.
        return self._fname

    @context
    def fname(self, fname):
        self._fname = fname

    #train get,set 를 만든다.
    @property
    def train(self) -> str: # -> : return 하는 결과값이 str(스트링)이다.
        return self._train

    @context
    def train(self, train):
        self._trian = train

    #test get,set 를 만든다.
    @property
    def test(self) -> str: # -> : return 하는 결과값이 str(스트링)이다.
        return self._test

    @context
    def test(self, test):
        self._test = test

    #id get,set 를 만든다.
    @property
    def id(self) -> str: # -> : return 하는 결과값이 str(스트링)이다.
        return self._id

    @context
    def id(self, id):
        self._id = id

    #label get,set 를 만든다.
    @property
    def label(self) -> str: # -> : return 하는 결과값이 str(스트링)이다.
        return self._label

    @context
    def id(self, label):
        self._label = label
    