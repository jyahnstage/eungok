class Cat:
    def __init__(self, name="nabi", age=3):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Cat Class : name = {self.__name}, age = {self.__age}'

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

cat = Cat("네로", 5)
print(cat)
# print(cat.__name) # 이렇게 하면 오류 발생 하므로 name 함수 만들었으니까 아래처럼
print(cat.name)
cat.name = "미미"
print(cat.name)
print(cat.get_age())
cat.set_age(10)
print(cat.get_age())