#클래스 상속

class Family:
    def __init__(self):
        self.lastname = '김'
    
    def lname(self):
        print(f'성은 {self.lastname}')


class Person(Family):
    firstname = "태경"  #자식클래스에 init이 없으면 부모 클래스의 init을 받아옴.
    
    def fname(self):
        print(f'이름은 {self.firstname}')

family = Family()
person = Person()

family.lname()
person.fname()

print(person.lastname)
person.lname()
