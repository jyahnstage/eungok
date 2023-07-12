#캡슐화
class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Cat(name={self.__name}, age={self.__age}살)'
    
nabi = Cat("나비","10")


print(nabi)
print("===============================")
nabi.__age = "20"
print(nabi)  