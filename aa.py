import array

#create an array of integers

intarr= array.array('i' , [1,2,3,4,5])

#access elemnts using their index
print(intarr[1])

#add items using append () which adds elements to the end of the array 
intarr.append(6)
print(intarr)

#remove items using remove() by specifying the item to be removed
intarr.remove(3) #specify the item to remove
print(intarr)