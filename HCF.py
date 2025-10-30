a=int(input("Enter first number"))
b=int(input("Enter sec number"))
while b != 0:
    a,b = b, a % b
print("HCF is...",a)