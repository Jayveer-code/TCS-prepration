def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print("not prime")
                break
        else:
            print("Prime")
    else:
        print("NEter Nmuber plese grater then Xeo")
num=int(input("Enter any number"))
prime(num)
    
    
                
        