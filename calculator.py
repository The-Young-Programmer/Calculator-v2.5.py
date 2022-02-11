import random
import time
#The Young Programmer 👨‍💻
#Do not copy my code without giving credit 


print("-"*20)
print("Welcome to Calculator v2.5")
print("created by TYP 👨‍💻")
print("-"*25)
time.sleep(1)

while True:
  print("[1]- Addition\n[2]- Subtraction\n[3]- Division\n[4]- Times Table\n[5]- Multiplication\n[6]- Exit")
  print("-"*25)
  per = int(input("-"))
  if per == 6:
    print("...")
    break
  elif per == 5:
    a = int(input("Input First number:"))
    b = int(input("Input Second number:"))
    c = a*b
    print("Multiplying {} with {} gives this result {}.".format(a,b,c))
    time.sleep(2)
    print("-"*25)
  elif per == 4:
    a = int(input("Input a number:"))
    for q in range(1,11):
      b = a*q
      print("{} × {} = {}".format(a,q,b))
    print("-"*25)
    time.sleep(2)
  elif per == 3:
      a = int(input("Input First number:"))
      b = int(input("Input Second number:"))
      c = a/b
      print("The division between {} with {} results in {}.".format(a,b,c))
      print("-"*25)
  elif per == 2:
    a = int(input("Input First number:"))
    b = int(input("Input Second number:"))
    c = a-b
    print("The subtraction between {} with {} results in {}.".format(a,b,c))
    print("-"*25)
  elif per == 1:
    a = int(input("Input First number:"))
    b = int(input("Input Second number:"))
    c = a+b
    print("The addition of {} with {} results in {}.".format(a,b,c))
    print("-"*25)
    time.sleep(1)
