class Cat:

    def __init__(self, name, age):
        self.__name = name
        if age <= 3:
            raise ValueError('3살 이상의 야옹이만 입장 가능합니다')
        self.__age = age

    def __str__(self):
        return (f'Cat(name={self.__name}, age = {self.age})')


    #캡슐화된 거 바꾸고 싶을때:
    @property
    def age_1(self):
        return self.__age

    @age_1.setter
    def age(self, age):
        if age <= 3:
            raise ValueError('3살보다 많아야 나이를 바꿀 수 있습니다.')
        self.__age = age

cat = Cat("nabi", 5)
print(cat)

# cat.__age = 10
cat.age = 4
print(cat)
print(cat.age_1)