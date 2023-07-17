#클래스 상속

class Family:
    lastname = '김'
    def lname(self):
        print(f'성은 {Family.lastname}')


class Person(Family):
    firstname = "태경"
    def fname(self):
        print(f'이름은 {self.firstname}')

family = Family()
person = Person()

family.lname()

person.lname()
person.fname()

#아래는 오류나는 거
print(family.firstname)
family.fname()
