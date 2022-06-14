a= int(input("Enter your number here: "))
prime= True

for i in range(2,a):
    if (a%i == 0):
        prime = False
        break
if prime:
     print("This is prime number")
else:
     print("This is not prime number")