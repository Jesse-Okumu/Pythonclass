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



#create a list by declaration
list=[]
print("Initial blank list: ", 'List')
print("Type ")



Tuple1=()
print("The type of tuple1" ,type(Tuple1))
Tuple1=(1,"Geek", 'a')
print("Tuple1: ", Tuple1[1])
Tuple2=tuple("First,")

#Basic if statment to check if a number is positive, negative or zero
num=int('about'("Enter a number: "))
if num>0:
    print(num,"is a positive number.")
elif num== 0:
    print(num,"is neither positive or negative, it is Zero")
else:num<0
print(num, "is a ngative number.")


#Demonstation of nested if statment to check if a number is positive , negative or zero
num=int(input("Enter a number:"))
if num>=0:
    if num== 0:
        print(num,"is neither postive or negative, it Zero")
    
    else:
        print(num,"is a negative number.")
    
        print("Outside body if statement")

#Program for calculating the sum in a list 
sum=0
i=2
list=[2,3,4,5,6,7,8,9,10]
for val in list:
    sum+=i #instead of sum= sum+1
print ("The sum of the list is: ")


#Demonstation of the raneg function
#Ranges starts from zero
print(range(10))
alist=list(range(10))
print(alist)

#Range with 2 parameters
print(range(2,8))
listb=list(range(2,8))
print("Print the whole listb: ", )