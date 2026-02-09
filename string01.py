"""
ns = "0123456789"
#slicing strings
print (ns[0])
print (ns[5])
print (ns[2:5])
print (ns[1:9:3])
print (ns[:-4])
print (ns[::-1])
print (ns[1:])
"""

#enter character
longmsg = """Hello everybody
This Kourosh coding againg after 5 years.
Here is a double qout char: "
end of the long string
"""
#triple qoute in a new line means add new line to the end of the string

print(longmsg)
print("And here is an enter character\nwhich adds a new line to my string!\nI\'m excited\n")

#strings are immutable
name = "kourosh"
print(name)
print(name[0])
print("miss spelled my name.\nthe \"K\" at the start should be capital!\nlets fix it")
name = "K" + name[1:]
print(name)
print("Now that\'the right way to spell my name.")