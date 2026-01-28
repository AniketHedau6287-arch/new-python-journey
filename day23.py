# data1 = [1,12,11,21,19,18,13,12,121,2151,2,112,]
# data2 = []
# for i in data1 [: : -1] :
#     data2.append(i)
# print(data2)

# data = [1,21,2,21,56,25,62,62,62,52,2,626,56,26,22,62,26,22,652,62,626,26,26,5262,62,62,62,62,652,]
# start = 0 
# end = len(data)-1
# while start<end:
#     data[start],data[end] = data[end],data[start]
#     start = start+1
#     end = end-1
# print(data)

data = [4,154,51,41,4,1,54,154,21,54,1,5,5,5,4,515,21]
min = data[0]
for i in data:
    if min<i:
        min=i
print(min)

data = [4,154,51,41,4,1,54,154,21,54,1,5,5,5,4,515,21]
max = data[0]
for i in data:
    if max<i[-2]:
        print(max)
    

    