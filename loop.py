#Program to demonstrate the use of while loop by adding natural numbers
n=int(input("Enter how many natural numbers you want to add: "))
sum=0 #initialize sum to 0
i=1 #initialize i as index to one


#While loop to add natural numbers 
while (i<=n): 
    sum +=i #sum=sum +i 
    print ( "The sum of the ", i, "natural numbers is: ", sum)
    i+=1 #i=i+1

''''''

#A simple program to demonstrate a break statement
for char in "string" :
    print(' in for loop', char)
    if char=="i":
        break

print('out of loop')

#A simple program to demonstrate the use of continue statement
for char in "string":
    print('in for loop ', char)
    if char=="i" :
        print('I found ', char)
        continue

print (" The end")
     