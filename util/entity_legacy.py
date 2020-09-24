class Entity:
    def __init__(self, context, fname, train, text, id, label):
        self._context = context  # _ 는 default 접근, __ 2개는 pritave 접근 의미
        self._fname = fname
        self._train = train
        self._text = text
        self._id = id
        self._label = label

    @property
    def context(self) -> str:
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @property
    def fname(self) -> str:
        return self._fname

    @fname.setter
    def fname(self, fname):
        self._fname = fname

    @property
    def train(self) -> str:
        return self._train

    @train.setter
    def train(self, train):
        self._train = train

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, label):
        self._label = label
