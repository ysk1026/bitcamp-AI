from flask import Flask
from flask import render_template, request
from price_prediction.cabbage import Cabbage
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# method 는 총 4개가 있습니다.
# GET, POST, PUT, DELETE 그래서 이것들은 array를 이뤄요.
# 그 array 이름은 methods 입니다.
# app 에서 POST 라고 하면 인지하지 못하고 ['POST'] 해야 인지합니다.
# 그래서 아래 코드는
# methods = ['POST']로 바뀝니다.
# 이런 methods 를 RESTful 이라고 합니다.
@app.route('/cabbage', methods =["POST"])
def cabbage():
    print('UI to API Connect Success')
    avgTemp = request.form['avgTemp']
    minTemp = request.form['minTemp']
    maxTemp = request.form['maxTemp']
    rainFall = request.form['rainFall']
    print(f'avgTemp : {avgTemp}')
    print(f'minTemp : {minTemp}')
    print(f'maxTemp : {maxTemp}')
    print(f'rainFall : {rainFall}')
    cabbage = Cabbage()
    cabbage.avgTemp = avgTemp
    cabbage.minTemp = minTemp
    cabbage.maxTemp = maxTemp
    cabbage.rainFall = rainFall
    result = cabbage.service()
    print(f'Prediction : {result}')
if __name__ == '__main__':
    app.run()
