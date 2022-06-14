a=input("Enter Your Name::")
b=input("Enter Date::")

letter='''Dear,<|NAME|>,
I am glad to inform you that,we would like to move   forword with you,and very happy to inform you that,You are selected,
for our firm from

<|DATE|>'''
# print(letter)
letter=(letter.replace("<|NAME|>",a))
letter=(letter.replace("<|DATE|>",b))
letter=(letter.replace("   "," " ))
print(letter)
# print(len(letter))