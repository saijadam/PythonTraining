#List - Mutable
list1 = [1,2,3,1,5]

#so that I can add, remove, etc
list1.append(6)
sum=0
for item in list1:
    sum=sum+item

#comment
#TO COMMENT MULTIPLE LINES - CTRL+/
print("Sum of list: ",sum)

#list duplicate of occurances here 2, only ONE occueanc of 1
print(list1.count(1))

#Data type conversion
print("converted to tuple :", tuple(list1))

