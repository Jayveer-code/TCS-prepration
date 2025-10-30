n = int(input("Enter a number: "))
sum = 0
temp = n

while temp > 0:# temp >=0  for confustion error
    digit=temp%10
    sum=sum+digit ** 3
    temp //=10
if n==sum:
        print("Armstrong number")
else:
    print("Not Armstrong number")


# Ek-ek digit nikalte hain (digit = temp % 10)

# Har digit ka cube karte hain (digit ** 3)

# Sab cubes ka sum nikalte hain

# Agar ye sum original number ke equal ho →
# 👉 Armstrong number