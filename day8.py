# 1 - sum of all element of a list
# 2 - find largest value in a list
# 3 - find second largest value in a list
# 4 - find smallest value in a list
# 5 - find second smallest value in a list

#1
# data =[1,6,15,15,11,515,6,5651,54,1,]
# print(sum(data))

# #2
# data =[1,6,15,15,11,515,6,5651,54,1,]
# print(max(data))

#3
data =[1,6,15,15,11,515,6,5651,54,1,]
data.sort()
print(data[-2])

#4
# data =[1,6,15,15,11,515,6,5651,54,1,]
# print(min(data))

#5
data =[1,6,15,15,11,515,6,5651,54,1,]
data.sort()
print(data[1])




# Tuple  ()   immutable(unchangable)
# read only

# data = ()
# data = tuple()

# data = (10,7)
# print(type(data))

# data = (1,3,6,78,76)
# data[0] = data[0]+10
# print(data)
# print(data[0])

# data = (1,3,6,78,76)
# data = sorted(data)
# data = tuple(data)
# print(data)

# print(len(data))
# print(max(data))
# print(min(data))
# print(sum(data))
# print(data.count(1))
# print(data.index(1))

# a=10
# b=30
# c=59

# data = a,b,c   # packing of data
# print(data)

# a,b,c = data   # unpacking
# print(a)
# print(b)
# print(c)