class MagicMethod:
    area = 0
    def __add__(self, other):
        return self.area + other.area
    
    def __lt__(self, other):
        return self.area < other.area
    
    def __le__(self, other):
        return len(self.area) >= len(other.area)
    
    def __ne__(self, other):
        return len(self.area) != len(other.area)
    
    def __eq__(self, other):
        return len(self.area) == len(other.area)
    
a = MagicMethod()
a.area = "hello"
b = MagicMethod()
b.area = "helloooooo"
# print(a + b) #이거를 아래처럼 쓸 수 있음.
# print(a.__add__(b))

print(a.__lt__(b))
print(a.__le__(b))
print(a.__ne__(b))
print(a.__eq__(b))