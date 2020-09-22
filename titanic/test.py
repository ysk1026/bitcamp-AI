from dataclasses import dataclass
import pandas as pd
import numpy as np


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


class Service:
    def __init__(self):
        self.entity = Entity()

    def new_model(self, payload) -> object:
        this = self.entity
        this.context = './data'
        this.fname = payload
        return pd.read.csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, feature) -> object:

        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)
        return this


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def preprocessing(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train)  # payload
        this.test = service.model(test)  # payload
        return this

    def modeling(self, train, test):
        service = self.service
        this = self.preprocessing(train, test)
        print(f'훈련 컬럼 : {this.train.columns}, ')
        this.label = service.create_lable(this)
        this.train = service.create_train(this)
        return this

    def learning(self):
        pass

    def submit(self):
        pass


if __name__ == '__main__':
    ctrl = Controller()
    ctrl.modeling('train.csv', 'test.csv')
