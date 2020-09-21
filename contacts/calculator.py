class Caculator:
    # 생성자 함수 -> 인스턴스 (객체) 만드는 함수
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # 함수
    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


if __name__ == '__main__':
    calc = Caculator(6, 2)
    sumResult = calc.sum()
    print(f'덧셈 결과 {sumResult}')
    subResult = calc.sub()
    print(f'뺄셈 결과 {subResult}')
    mulResult = calc.mul()
    print(f'곱셈 결과 {mulResult}')
    divResult = calc.div()
    print(f'나누기 결과 {divResult}')
