import sys
sys.path.insert(0, '/Users/youngseonkim/Documents/SbaProjects')
from titanic.entity import Entity
from titanic.service import Service

"""
--- PassengerId  고객ID,
--- Survived 생존여부,  --> 머신러닝 모델이 맞춰야 할 답 
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
--- Ticket 티켓번호,
Fare 요금,
--- Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
"""


class Controller:
    def __init__(self):
        print('TEST')
        self.entity = Entity()
        self.service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocessing(train, test)
        
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        
        return this

    def preprocessing(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train)  # payload
        this.test = service.new_model(test)  # payload
        this.id = this.test['PassengerId'] # 머신에게는 이것이 question이 됩니다.
        print(f'드랍 전 변수 : {this.train.columns}')
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        print(f'드랍 후 변수 : {this.train.columns}')
        return this
    
    def learning(self):
        pass

    def submit(self): # machine이 된다.
        pass


if __name__ == '__main__':
    ctrl = Controller()
    ctrl.modeling('train.csv', 'test.csv')
