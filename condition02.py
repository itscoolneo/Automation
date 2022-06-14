m1=int(input("Enter your marks English:-"))
m2=int(input("Enter your marks Hindi:-"))
m3=int(input("Enter your marks Marathi:-"))

percentage=((m1+m2+m3)/3)
print("Your percentage is",percentage)
a=70
b=40
c=33
if (m1 or m2 or m3) <33:
    print("You are failed due to less than mandatory marks:",)
elif   percentage >= a:
    print("Congratulation You Are Pass with First class...!")
elif percentage >= b:
    print("Congratulation You Are Pass")
elif percentage >= c:
    print("Dear Man You are just pass anyways")
else:
    ("You are failed due to less than mandatory marks:")