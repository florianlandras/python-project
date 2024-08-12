
#?Integer = Simple numbers
num = 3
print(type(num))


#?loat = Numbers with decimals
num_2= 3.14
print(type(num_2))


#? 3**2 = uppjöjt till = 9
print(3**2)


#?Module remainder =2 får plats 1 gång i 2%2. Ingen kvar. Slutvärde:0
print(2 % 2)
print(3 % 2)
print(4 % 2)
print(5 % 2)


#? num = num-värdet gånger 10

num = 1
num *= 10
print(num)

#? Absolute value
print(abs(-3))

#? Absolute value = round = 4
print(round(3.75))

#? Absolute value = round choosen decimal = 3.8
print(round(3.75,1))

#? Boolean = true/false
num_1 =3
num_2 = 2
print(num_1 == num_2)


#? Even if strings - I want them to be numbers. 
#!Above rule wont work
"""Answer is 100200, but should be 300"""
num_1 = "100"
num_2 = "200"
print(num_1 + num_2)

"""To solve problem above"""
num_1 = "100"
num_2 = "200"
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)