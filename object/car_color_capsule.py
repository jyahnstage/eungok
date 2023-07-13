class Car:

    def __init__(self, name, price, color):
        self.__name = name
        self.__price = price
        if price <= 100000000:
            raise ValueError('1억 이상의 차만 가능합니다.')
        self.__color = color

    def __str__(self):
        return (f'Car(name={self.__name}, price={self.__price}, color = {self.__color})')


    #캡슐화된 거 바꾸고 싶을때:
    @property
    def color_1(self):
        return self.__color

    @color_1.setter
    def set_color(self, color):
        if self.__color == "노랑":
            raise ValueError('노랑은 안돼요')
        self.__color = color

car = Car("쏘렌토", 1100000, "검정")
print(car)

# cat.__age = 10
car.set_color = "파랑"
print(car)
print(car.color_1)