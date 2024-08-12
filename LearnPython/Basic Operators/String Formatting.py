###String Formatting

Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".
%s: This is a placeholder for a string. When the string is formatted, any value provided in its place will be converted to a string if it is not already one.
%d: This is a placeholder for an integer. When the string is formatted, the value provided in its place should be an integer, and it will be displayed as a decimal number.

Let's say you have a variable called "name" with your user name in it, and you would then like to print(out a greeting to that user.)###

name = "John"
print("Hello, %s!" % name)



#!Example 1
#To use two or more argument specifiers, use a tuple (parentheses):
name = "John"
age = 23
print("%s is %d years old."%(name, age))


#!Example 2 
#With F-strings
name = "John"
age= 23
print(f"{name} is {age} years old.")


name1= "Bala"
name2="Miskin"
ageBala = 34
ageMiskin= 22

print(f"Hello your fucking idiots, {name2} is {ageMiskin} years old and {name1} is {ageBala} years old")



#Any object which is not a string can be formatted using the %s operator as well. 
# The string which returns from the "repr" method of that object is formatted as the string. For example:

#? This prints out: A list: [1, 2, 3]
#! Example 1
mylist = [1,2,3]
print("A list: %s " % mylist)

#! Example 2
mylist = [1,2,3]
print(f"A list: {mylist}")





