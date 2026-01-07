data = [1,4,6,43,6,43,6,30,90]

ans = data.count(43)
print(ans)

ans = data.index(43)
print(ans)

data1 = data.copy()
data.pop()

print(data)
print(data1)

data.reverse()
print(data)

data.sort()   # assending
data.sort(reverse=True)   # dessending
print(data)

# to delete data from list
data.pop()   # remove data from last
data.pop(0)  # remove data according to index
print(data)
data.remove(43)
print(data)
data.clear()
print(data)
del data



# to add data in list
data.append(6)
print(data)
data.insert(0,20)
print(data)
data.extend([1,3,5,6,4])   # iterable object
print(data)

#Common functions of list tuple set dictionary
print(len(data))
print(min(data))
print(max(data))
print(sum(data))