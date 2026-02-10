#string interpolation
name = "Kourosh"
lname = "Najafian"
print("Hello " + name + " " + lname)

#now lets use interpolation
#the first method os used by C programmers
#I shouldnt use this
print("Hello %s %s" %(name, lname))
age = 24
print("Hello %s %s. You are %i" %(name, lname, age))

#format method
print("Hello {} {}. You are {}".format(name, lname, age))
print("Hello {1}, {0}. You are {2}".format(name, lname, age))
print("Hello {1}, {0}. You are {0}".format(name, lname, age))
print("Hello {family}, {name}. You are {sen}".format(name=name, family=lname, sen=age))

#lets add precision
age = 24.4879348252
print("Hello {family}, {name}. You are {sen:1.1f}".format(name=name, family=lname, sen=age))
print("Hello {family}, {name}. You are {sen:1.0f}".format(name=name, family=lname, sen=age))
print("Hello {family}, {name}. You are {sen:5.0f}".format(name=name, family=lname, sen=age))
#the 5 helps to organize the output by adding a little space before the nembers so that eveything lines up perfectly in different lines


#lets do it differently
print(f"Hello {lname}, {name}. You are {age:1.0f}")
#i can write any python code in {}