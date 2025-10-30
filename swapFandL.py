n = int(input("Enter number: "))
s = str(n)
if len(s)>1:
    swapp=s[-1]+s[1:-1]+s[0]
else:
    swapp=s
print("After Swapping...",swapp)

# str(n) → number ko string me convert kiya (taaki digits handle kar sakein).

# s[-1] → last digit

# s[0] → first digit

# s[1:-1] → beech ke digits

# Sabko swap karke join kar diya.