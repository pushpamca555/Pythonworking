class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def detail(self):
         print(self.a)
         print(self.b)

class B(A):
    def __init__(self,a,b,c):
        self.c=c
        A.__init__(self,a,b)
    def det(self):
        print(self.detail)
class C(A):
    def __init__(self,a,b,c):
        self.c=c
        A.__init__(self,a,b)
    def deta(self):
        print(self.c)




obj1=B("Tamil","Pushpa","QA")
obj1.detail()
obj1.det()

obj2=C("English","Agarna","Dev")
obj2.detail()
obj2.deta()