'''a1=int(input("User 1: "))
a2=int(input("User 2: "))
a3=int(input("User 3: "))
a4=int(input("User 4: "))
# b=(a1,a2,a3,a4)
if a1>a2:
    print("User 1 is greater:")
elif a2>a3:
    print("User 2 is greater:")
elif a3>a4:
    print("User 3 is greater:")
else:
    print("User 4 is greater:")
print("Done")'''
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")