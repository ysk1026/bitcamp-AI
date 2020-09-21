class Entity:
    def __init__(self, context, fname, train, text, id, label):
        self._context = context  # _ 는 default 접근, __ 2개는 pritave 접근 의미
        self._fname = fname
        self._train = train
        self._text = text
        self._id = id
        self._label = label

    # context get, set을 만든다.

    @property
    def context(self) -> str:
        return self._context

    @context
    def context(self, context):
        self._context = context

    # fname get, set을 만든다.

    @property
    def fname(self) -> str:
        return self._fname

    @fname
    def fname(self, fname):
        self._fname = fname

    # train get, set을 만든다.

    @property
    def train(self) -> str:
        return self._train

    @train
    def train(self, train):
        self._train = train

    # text get, set을 만든다.

    @property
    def text(self) -> str:
        return self._text

    @text
    def text(self, text):
        self._text = text

    # id get, set을 만든다.

    @property
    def id(self) -> str:
        return self._id

    @id
    def id(self, id):
        self._id = id

    # label get, set을 만든다.

    @property
    def label(self) -> str:
        return self._label

    @label
    def label(self, label):
        self._label = label
