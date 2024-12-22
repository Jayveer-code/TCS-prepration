# a=11
# if a%2==0:
#     print("even")
# else:
#     print("odd")


# name="jayveer"
# ns=""
# for char in name:
#     ns=char+ns
# print(ns)


# def prime(num):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
#     else:
#         print("Enter greter one")
# num=int(input("Enter number chek prime or not"))
# prime(num)

# def sumd(num):
#     return sum(int(digit) for digit in str(num))
# number=int(input("ENter number"))
# if number > 0:
#     print("the sum of digit is ",sumd(number))
# else:
#     print("The given number is less to zero")

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("enter number to check factorial"))
# print(fact(n))

num=10
a=0
b=1
print("fab from 1 to 10")
for i in range(2,num):
    c=a+b
    print(c,end=" ")
    a=b
    b=c