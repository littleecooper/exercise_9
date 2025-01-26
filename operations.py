# var is the name of the variable where the users input is stored
# input() is a built in python function that allows the user to type something into the terminal and then returns their input as a string
# Inside the brackets, you can add a prompt message and this will be displayed in the terminal once the program has been run
var = input("Please enter a value: ")

# printing the value of var as upper case
# the ".upper()" is called a string method in python where its purpose is to capitalise all the characters in a string.
print("Upper case:", var.upper())

# Printing the number of characters in var
# The "len" function returns the length of a string i.e the number of characters or items (lists/tuples) in the string
print("Number of characters", len(var))

# Checking if var contains characters using isdecimal()
# the isdecimal() method checks if all the characters in a string are numerical integers. If the string does ONLY contain numbers, it will return as TRUE
# If the string contains a decimal (float) or a letter or any other than an integer, then it will return as FALSE.
# the .isdecimal() function only returns and boolean value.
print('Checking for numeric characters', var.isdecimal())

