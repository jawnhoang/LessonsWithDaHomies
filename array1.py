# # fill an array with 100 integers, of multiples of 3s
# #declare array
# exArr =[]
# for i in range(100): #this should go from 0-99
#     if i % 3 == 0:
#         exArr.append(i)
#
# print(exArr)
#
# #remove all elements that end with a 5
# for i in exArr:
#     if i % 5 == 0:
#         exArr.remove(i)
#
# print(exArr)

# remove elements
x = []

#fill an array
for i in range(10):
    x.append(i)

print(x)

#remove first element inside list
x.remove(0)
print(x)

#remove element using it's index
del x[0]
print(x)


#remove last element
del x[-1]
print(x)

#remove element in the middle with known index
del x[3] #or del x[-4] <- starts from right to left
print(x)

for i in x:
    if i == 6:
        x.remove(i)
print(x)
