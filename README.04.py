"""
머신러닝 = 기계학습 = ML
ML : 지도, 비지도, 강화
ML Process 4 : 
    1. precprocessing 
    2. modeling
    3. learning
    4. evaluation
ML Alogrithm
0. 뉴런(neuron)
1. 회귀 
2. 분류  
3. SVM
4. dtree
5. kmean
6. PCA
7. RF (R-forest)
8. NLP
9. DL (Deep learning)
여기까지가 chap 13 입니다.
외워주세요. 
마치 지도를 외우듯이...
Tensorflow
-----------------
비지니스 로직 - service 
processing 하는 파일명
 precprocessing 
 modeling
 learning 
 evaluation
 완성되면 submit (파일로 저장)
# 외부에 있는 파이썬 파일(.py) 을 import 해야 속성, 기능을 사용할 수 있다
# 내부에서는 이것을 인스턴스화(instance) 해야 한다
# entity = Entity() 
# 이때 소문자 entity 는 인스턴스라고 하고 이를 객체로 정의한다.
# 대문자 Entity 는 클래스
# 라운드 브레이스가 있는 Entity() 는 생성자라고 한다.
# 결론..객체지향(OOP)에서는 속성과 기능을 호출하는 구조로
# 두가지 방식이 있는데
# calc = Calculator() 있다고 하면
# calc 는 인스턴스 객체가 되고
# Calculator 는 클래스 객체(스태틱)라고 한다..
# calc.sum() 하면 인스턴스 호출방식= 다이나믹
# Calculator.sum() 하면 클래스 호출방식 = 스태틱 이라 한다.
from titanic.entity import Entity
from titanic.service import Service
class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
========================================
페이로드 (컴퓨팅): 전송되는 데이터
this.fname = payload ~> setter 할당연산자( = ) 있으면 setter
this.fname 만 있으면  ~> getter 할당연산자( = ) 없으면 getter 
========================================
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked   => 메타데이터 = 스키마 = features = variables = properties
1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S => row, 행, 인스턴스, raw 데이터
2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
===========================
차원 ( dim )
variable   x = 3  스칼라, 0 차원
array      [] = {1,2,3} 벡터, 1차원이 되고, array 내부에서 varable 은 element 가 된다
matrix [[]] = {{1,2,3}, {4,5,6}} 매트릭스, 2차원 data frame, array 라 하지 않고 vector 가 된다.
=======================
지도학습에서 반드시 해야 할 일은 dataset 을 생성하는 것입니다.
그 때 dataset 은 반드시 train, test 두가지 형태로 작성합니다. p.149
"""