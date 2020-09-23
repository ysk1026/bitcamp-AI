"""
클래스 하나가 단위 unit 이 됩니다.
이제 확장을 하겠습니다.
객체지향에서는 디자인패턴이라는 개념이 존재합니다.
1994년 GoF 4인방 개발자 에릭 감마 ... 패턴 23개로 정의... 
이 분이  vscode 개발자입니다.
패턴조합을 통해 큰 개념의 패턴 -> MVC 패턴 이라고 합니다.
model , view, controller 이렇게 조합합니다. -> Java,  C 언어에서 주로 사용하는 개념.
model : 데이터처리 -> API 서버 -> Python -> Tensorflow 
view : 화면UI 처리 -> UI 서버 -> Reactjs
controller : model + view 를 연결 ---> 네트워크 처리 -> Flask (app.py) -> RESTful 방식
이 지점에서 팀내에서 나의 역할을 고민하시면 됩니다.
곧 취업시 자신을 어필할 수 있는 혹은 자신있는 혹은 흥미있는 카테고리를 결정하시는 것이 좋습니다.
Backend Tier (API 서버 구축담당 : Java, C, Python, SQL)
Frontend Tier (UI 서버 구축담당 : Javascript, HTML, Reactjs)
모델을 제작하고 뷰를 만들어서 컨트롤러로 연결한다. 이 컨셉을 이해하세요....
프로토타입 입니다.
독자적으로 움직이는 --> 모듈.
5개의 모듈(개인이 작성)을 합쳤을 때, 조립이 잘 되서 작동이 잘 되면 1단계를 패스한다.
캐글... 회원가입을 하세요.
dataset (test.csv, train.csv) 를 모델에 추가했습니다.
titanic 폴더에
dataset (test.csv, train.csv) 이게 존재하고
entity (속성) + service(기능)  = 객체(object)
def __init__(self, .....) => 속성
def abc(): => 기능
결국 class 는 객체를 정의하는 것이다.
class 가 여러개 (entity, service) 모여서 다시 큰 개념의 객체를 이뤄요.. 그때 이것은 클래스라 하지 않고
model 이라고 한다.
패키지는 같은 컨셉을 공유하는 클래스의 집합... 모듈 -(진화)-> 모델
모델에 AI 개념이 없으면 web 에서 말하는 모델이고
AI 개념이 존재하면 인공지능 모델이 됩니다.
여기서 AI 개념이라고 하면 머신러닝(기계학습) 코딩의 유무...
dataset 을 추가하면 이를 지도학습이라고 합니다. 
dataset 이 없으면 이를 비지도학습이라고 합니다.
지금 타이타닉은 dataset 을 모델에 넣었으므로 이는 지도학습을 하겠다는 의미가 됩니다.
"""