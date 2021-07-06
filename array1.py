# fill an array with 100 integers, of multiples of 3s
#declare array
exArr =[]
for i in range(100): #this should go from 0-99
    if i % 3 == 0:
        exArr.append(i)

print(exArr)


#remove all elements that end with a 5
for i in exArr:
    if i % 5 == 0:
        exArr.remove(i)
        
print(exArr)
