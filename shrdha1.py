#practice no 1 
class student:
    def __init__(self,name,marks):
        self.name=name  
        self.marks=marks
    def avg(self):
        sum=0
        for val in self.marks:
            sum +=val
        print(self.name,"Your avg score is ",sum/3)
s1=student("jay",[12,11,15])
s1.avg()




# class stufent:
#     name="jayveer"
# s1=stufent()
# print(s1.name)


# class car:
#     color="blue"
#     brand="tata"
# c1=car()
# print(c1.color)
# print(c1.brand)


#object attribute ni priority alwaays  high then class attribute
# class stufent:
#     name="jayveer"
#     def __init__(self,name,amarks):
#         self.name=name  
#         self.marks=amarks
#     def wel(self):
#         print("Welcome::",self.name)
    
#     def get_mar(self):
#         return self.marks
# s1=stufent("Jayveer",99)
# print(s1.wel(),s1.get_mar())
# s2=stufent("Harsh",98)
# print(s2.wel(),s2.get_mar())