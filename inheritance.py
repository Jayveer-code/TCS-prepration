class A:
    def frist():
        print("Thisd class A")
class B:
    def secound():
        print("Thisd class B")
class c(A,B):
    def final():
        print("Thisd class C")
obj=c()
obj.final()
