import ctypes

# mydict={
#     "Company":"Champion Software",
#     "Employe":"Dharmesh",
#     "Group":"o+",

# print(mydict.items())
# print(list(mydict),list(mydict.values()))
# print(mydict)
# a=mydict
# print(type(mydict))
# print(mydict.keys(),mydict.values())
# print(mydict.values())
# ************************************************

mydict={"Adharcard No":"1234 1234 1234 1234","Driving Licence":"DEMO123","Pan No":"ABCDE1234F"}
# print(type(mydict))
# print(mydict)
# print(mydict["Adharcard No"],mydict["Driving Licence"],mydict["Pan No"])
# print(mydict.items())
salary={"Dharmesh":"99999"}
# print(type(salary))
mydict.update(salary)
print(mydict)
# print("Enter your choice:-\n",mydict.keys())
choice=input("Your Choice is:-\n")
print("your choice is:-",mydict.get(choice))
# print(mydict.values())
