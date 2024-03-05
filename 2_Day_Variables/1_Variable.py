##___Variables___##

#Variables are containers for storing data values.




##___Creating Variables___##

#Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it.

#Example:
a="Python"
b=40
print(a)
print(b)


#Variables do not need to be declared with any particular type, and can even change type after they have been set.
 
#Example:
y = "Rocky"       # y is of type int
y = 23            # y is now of type str
print(y)



##___Casting___##

# If you want to specify the data type of a variable, this can be done with casting.

#Example:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0



##____Get the Type____##

# You can get the data type of a variable with the type() function.

#Example:
x = 5
y = "John"
print(type(x))
print(type(y))




##___Single or Double Quotes?___##

# String variables can be declared either by using single or double quotes:

# #Example:
x = "John"
# is the same as
x = 'John'




##____Case-Sensitive____##

# Variable names are case-sensitive.

#Example:
a = 4
A = "Sally"
#A will not overwrite a

