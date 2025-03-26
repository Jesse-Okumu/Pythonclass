"""""
a=10
print ("Type of a: " , type(a))

b=10.5
print ("Type of b: "  ,type (b))

c=2+3
print ("Type of d: "  ,type (c))

b=10.5
print ("Type of c: "  ,type (c))


string1= "Hello"
string2= "World"
string3= ''

print(string1+string2+string3)
print("Type of string1: ", type(string1))
print("Type of string2: ", type(string2))
print("Type of string3: ", type(string3))
print("First character of string1: ",string1)
print("Last character of strings: ", string2)

"""

# Create a list by declaration
my_list = []
print("Initial blank list:", my_list)

# Tuple demonstration
Tuple1 = ()
print("The type of Tuple1:", type(Tuple1))
Tuple1 = (1, "Geek", 'a')
print("Tuple1:", Tuple1[1])

Tuple2 = ("First",)
print("Tuple2:", Tuple2)

# Basic if statement to check if a number is positive, negative, or zero
try:
    num = int(input("Enter a number: "))
    if num > 0:
        print(num, "is a positive number.")
    elif num == 0:
        print(num, "is neither positive nor negative, it is Zero.")
    else:
        print(num, "is a negative number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# Demonstration of nested if statement
try:
    num = int(input("Enter a number: "))
    if num >= 0:
        if num == 0:
            print(num, "is neither positive nor negative, it is Zero.")
        else:
            print(num, "is a positive number.")
    else:
        print(num, "is a negative number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

print("Outside body of if statement")

# Program for calculating the sum in a list
total_sum = 0
my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for val in my_list:
    total_sum += val  # Summing correctly
print("The sum of the list is:", total_sum)

# Demonstration of the range function
print("Range from 0 to 9:", list(range(10)))

# Range with two parameters
listb = list(range(2, 8))
print("Print the whole listb:", listb)