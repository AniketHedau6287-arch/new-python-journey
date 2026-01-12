# range(start,end-1,steps)

# print(list(range(1,11,1)))
# print(list(range(1,11)))
# print(list(range(11)))
# print(list(range(2,11,2)))
# print(list(range(1,11,2)))
# print(list(range(1,20,2)))
# print(list(range(1,11,-1)))
# print(list(range(-1,-11,1)))
# print(list(range(-11,-1,1)))
# print(list(range(-1,-11,-1)))
# print(list(range(1,11,1)))
# print(list(range(11,1,-1)))
# print(list(range(-11,-1,1)))



# slicing []
# indexing slicing -> list tuple string
# variable_name[start:end-1:steps] 

# name = "python"
# print(name[1:5:1])
# print(name[1:5:])
# print(name[:5:])
# print(name[1::])
# print(name[1:5:-1])
# print(name[-1:-5:1])
# print(name[-1:-5:-1])
# print(name[5:1:-1])

# name = "python"
# print(name[1:-4:1])
# print(name[-1:1:-1])
# print(name[-1::-1])
# print(name[::-1])


# swap a first and last letter of a string
# ex:- "python"  output:- "nythop"
# ex:- "welcome"  output:- "eelcomw"
name = "welcome"
print(name[-1] + name[1:-1:] + name[0])
