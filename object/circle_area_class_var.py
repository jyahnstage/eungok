class Circle:
    PI = 3.14
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return self.__radius * self.__radius * Circle.PI
    
    @property
    def radius(self):
        return self.__radius

circle = Circle(5)
print(circle.radius)
area = circle.area()
print(f'반지름이 {circle.radius}인 원의 넓이는 {area}이다.')