class 붕어빵:
    def __init__(self, contents, price):
      self.contents = contents
      self.price = price
      self.total_sales = 0

    def sell(self):
        print(f"{self.contents} 붕어빵이 {self.price}원에 판매되었습니다.")
        self.total_sales += self.price

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

    def display_total_sales(self):
        print(f"총 판매금:{self.total_sales}원")

슈크림붕어빵 = 붕어빵("슈크림", 1500)
팥붕어빵 = 붕어빵("팥", 1000)
고구마붕어빵 = 붕어빵("고구마", 2000)

슈크림붕어빵.sell()
슈크림붕어빵.sell()
슈크림붕어빵.sell()
슈크림붕어빵.eat()

팥붕어빵.sell()
팥붕어빵.sell()
팥붕어빵.sell()
팥붕어빵.eat()

고구마붕어빵.sell()
고구마붕어빵.sell()
고구마붕어빵.sell()
고구마붕어빵.eat()

print(f"총 판매금은 {슈크림붕어빵.total_sales + 팥붕어빵.total_sales + 고구마붕어빵.total_sales}원 입니다.")

