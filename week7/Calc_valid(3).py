class Calc_valid:
    def __init__(self, num1, num2, flag):
        self.num1 = num1
        self.num2 = num2
        self.flag = flag

    def is_valid_clac(self, ):

        self.flag = False
        try:
            self.num1/self.num2
        except ZeroDivisionError:
            print(f"{self.num1}/{self.num2}의 경우")
            print(f"{self.num2}가 분모에 0 이므로")
            print("계산 불가능한 값입니다.\n")
        else:
            self.flag = True
            print(f"{self.num1}/{self.num2}의 경우")
            print("계산 가능한 값입니다.\n")

        try:
            self.num2/self.num1
        except ZeroDivisionError:
            print(f"{self.num2}/{self.num1}의 경우")
            print(f"{self.num1}가 분모에 0 이므로")
            print("계산 불가능한 값입니다.")
        else:
            self.flag = True
            print(f"{self.num2}/{self.num1}의 경우")
            print("계산 가능한 값입니다.")
