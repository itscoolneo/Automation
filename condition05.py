marks=int(input("Enter Youe Marks Here: "))

if marks>=90:
    percantage = "Distiction"
elif marks>=80:
    percantage = "First Class"
elif marks >= 70:
    percantage = "Second Class"
elif marks >=60:
    percantage = "Third Class"
elif marks >=50:
    percantage = "Fourth Class"
else:
    percantage ="Failed"

print("You marks is:" + percantage)
   # print("Your marks is" + grp)