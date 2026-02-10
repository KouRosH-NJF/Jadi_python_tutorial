#String methods

name = "Kourosh"

print(name)
print(name.islower())

name = name.lower()

print(name)
print(name.islower())

#strings are imutable

name = "K" + name[1:]
print(name)