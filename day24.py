data = [1,1,2,1,2,12,1]
freq = {}

for i in data:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1

print(freq)