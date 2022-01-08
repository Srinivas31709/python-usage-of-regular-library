class Parent:
    def function1(self):
        print("this is function one")

class Child(Parent):
    def function2(self,a):
        print("this is function two")
        print(a)
        b=5
        print(b)

p=Child()
p.function1()
p.function2(10)