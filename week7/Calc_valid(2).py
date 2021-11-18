class Calc_valid:
    def __init__(self, num1, num2, flag):
        self.num1 = num1
        self.num2 = num2
        self.flag = flag


    def is_valid_clac(self, ):

        self.flag = False
        if self.num2 == 0:
            print("계산 불가능한 값입니다.")
        else:
            self.flag = True
            print("계산 가능한 값입니다.")
