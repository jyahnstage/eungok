#클래스 상속

class Family:
    def __init__(self):
        self.lastname = '김'
    
    def lname(self):
        print(f'성은 {self.lastname}')


class Person(Family):
    def __init__(self):
        self.firstname = "태경"
    
    def fname(self):
        print(f'이름은 {self.firstname}')

family = Family()
person = Person()

family.lname()
person.fname()

#아래는 오류나는 거
person.lname()
print(person.lastname)