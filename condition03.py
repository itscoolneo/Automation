print("This is a beautiful program ")
cmnt=input("Enter Your Comment hear:-")
# restrictedcomments=['Make a lot of money','buy now','subscribe this','click here']
# print(type(restrictedcomments))

if ("Make a lot of money" in cmnt):
    print("This is restricted comment..!")
elif("buy now" in cmnt):
    print("This is restricted comment..!")
elif("subscribe this" in cmnt):
    print("This is restricted comment..!")
elif("click here" in cmnt):
    print("This is restricted comment..!")
else:
    print(cmnt)