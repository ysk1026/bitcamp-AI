from entity import Entity
import pandas as pd
import numpy as np

'''
PassengerId  고객ID,
Survived 생존여부, -> 머신 러닝 모델이 맞춰야 할 답
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
        self.entity = Entity()

    def new_model(self, payload) -> object:
        this = self.entity
        this.context = './data'
        this.fname = payload
        return pd.read.csv(this.context + this.fname)

    @staticmethod
    def create_train(this):
        return this.train.drop('Survived', axis=1)  # train 은 답이 제거된 데이터 셋이다.

    @staticmethod
    def create_label(this):
        return this.train['Survived']  # lable 은 곧 답이 된다.

    @staticmethod
    def drop_feature(this):
        pass
