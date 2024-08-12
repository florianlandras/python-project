´

#Arithmetic Operators
#Remaineder - The value 3 fits 3 times in 11. It will then be 2 left. Which is the remainder. 
Remaineder=11%3
print(Remaineder)


#Using two multiplication symbols makes a power relationship.

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)


#Using Operators with Strings
#Python supports concatenating strings using the addition operator:

helloworld = "hello" + " " + "world"
print(helloworld)

#Python also supports multiplying strings to form a string with a repeating sequence:

lotsofhellos = "Hello" * 10
print(lotsofhellos)

#Using Operators with Lists

#Lists can be joined with the addition operators:

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)


collabage = [33,35,36]
miskins= [12,13,14]
total = collabage+miskins
print(total)

#Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:
print([1,2,3]* 3)

#Exercise

###        The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. 
            You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.
###



#! Example : 1 = Using old school method with %d - Crap method

x = object()
y = object()

x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")


#! Example : 2 = Using f-strings. Remove the piece of shit %d and replace it with f. Much better.

x= object()
y= object()

x_list = [10]*10
y_list = [10]*10
big_list = x_list + y_list
print(f"x_list contains {len(x_list)} objects")
print(f"y_list contains {len(y_list)} objects")
print(f"big_list contains {len(big_list)} objects")

# testing code  
if x_list.count(x) == 10 and y_list.count(y) == 10:  
    print("Almost there...")  
if big_list.count(x) == 10 and big_list.count(y) == 10:  
    print("Great!")  

