class Claculator:
    def__init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 = self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2



if __name__ == '__main__':
    calc = Claculator(4,6) # num1 = 4 , num2 = 6
    sumResult = cala.sum()
    re2 = cala.sub()
    re3 = cala.mul()
    re4 = cala.div()
    print('덧셈 결과' +format(sumResult))
    print('뺄셈 결과' + format(re2))
    print('곱셈 결과' + format(re3))
    print('나눗셈 결과' + format(re4))