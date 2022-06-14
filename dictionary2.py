company={}
a=input("Enter your fav company Keyur:-")
b=input("Enter your fav company Dharmesh:-")
c=input("Enter your fav company jaydip:-")
d=input("Enter your fav company Rasul:-")
company['Keyur']=a
company['Dharmesh']=b
company['Jaydip']=c
company['Rasul']=d
print(company.items())
print([value for key, value in company.items() if 'sul' in key])
