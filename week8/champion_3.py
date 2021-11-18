class Champion:
    def __init__(self, name):
        self.name = name
        self.hp = 1000
        self.cure = 15
        self.speed = 300
        self.attack_power = 10
        self.defend = 10
    def cham_detail_info(self):
        print(f"----------현재{self.name}의 자세한 정보----------")
        print(f"체력 : {self.hp}\n회복 : {self.cure}\n속도 : {self.speed}\n공격력 : {self.attack_power}\n"
              f"방어력 : {self.defend}")
        print(f"\n#########################{self.item_name} 사용!#########################")
        Item.change_cham_detail_info(self)

class Item(Champion):
    def __init__(self, name, item_name):
        super().__init__(name)
        self.item_name = item_name
    def which_item(self, item_name):
        if item_name == "shoe":
            self.speed += 100
        elif item_name == "shield":
            self.defend += 80
        elif item_name == "water pill":
            self.cure += 60
        elif item_name == "sword":
            self.attack_power += 120
    def change_cham_detail_info(self):
        Item.which_item(self, self.item_name)
        print(f"----------현재{self.name}의 자세한 정보----------")
        print(f"체력 : {self.hp}\n회복 : {self.cure}\n속도 : {self.speed}\n공격력 : {self.attack_power}\n"
              f"방어력 : {self.defend}")
