# import random 

# sn=random.randint(1,100)
# attempt=0

# while attempt<10:
#     guess=int(input("Enter the Guess number from 1 to 100..."))
#     attempt = attempt+1
#     if guess<sn:
#         print("Too Low Number Enter Higher Number...")
#     elif guess>sn:
#         print("Too Higher Number Enter low Number...")
#     else:
#         print(f"Congratulation You Choose Perfect Number {guess} in {attempt} attempt")
#         break
# else:
#     print("......................................")
#     print("  Game Over Maximum  Attempts  Over   ")
#     print("......................................")
    
    
# def machine():
#         n1=float(input("Enter First Number..."))
#         op=input("Choose Operation To Perfome ('+','-','*','/')")
#         n2=float(input("Enter Secound Number..."))
        
#         if op=='+':
#             print(f"result is {n1+n2}")
#         elif op=='-':
#             print(f"result is {n1-n2}")
#         elif op=='*':
#             print(f"result is {n1*n2}")
#         elif op=='/':
#             if n2!=0:
#                 print(f"result is {n1/n2}")
#             else:
#                 print(f"Not Divide By Zero...")
#         else:
#             print(f"Invalid Operation...")
# machine()


# tasks=[]
# def todo_list():
#     while True:
#             print("\n1. Add Task\n2. Remove Task\n3. Show Tasks\n4.Exit")
#             ch=input("Enter Task To Perfome...")
#             if ch=='1':
#                 new_task=input("Enter Task To Add...")
#                 tasks.append(new_task)
#                 print("Task Added SucessFully...")
#             elif ch=='2':
#                 new_task=input("Enter Task To Remove...")
#                 if new_task in tasks:
#                     tasks.remove(new_task)
#                     print("Task Remove SucessFully...")
#                 else:
#                     print("Task Not Found...")
#             elif ch=='3':
#                 if tasks:
#                     print("Your all Tasks is\n",tasks)
#                 else:
#                     print("Not task in Database") 
#             elif ch=='4':
#                 print("GoodBye...")
#                 break
#             else:
#                 print("Inavalid Choose Operation...")
# todo_list()               


def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    for word, count in frequency.items():
        print(f"{word}: {count}")

text = input("Enter a paragraph: ")
word_frequency(text)