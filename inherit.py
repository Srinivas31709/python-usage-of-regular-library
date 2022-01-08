class Area():
    def f1(self):
        print("This prints Area")

class Square(Area):
    def f2(self,a):
        s=a*a
        print(s)

class Circle(Area):
    def f3(self,r):
        s=3.14*r*r
        print(s)

s=Square()
r=Circle()
s.f2(4)
r.f3(2)