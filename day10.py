#dictionary
#key = unique
#value = can be duplicate 

data={
    "name":"aniket",
    "rollno":"0198CD221004",
    "course":["python","pandas","numpy"],
    101:2200
}

print(data["name"])
print(data[101])
print(data["course"])
print(type(data))

data["duration"]="5+1"
data["duration"]="6+2"
data[102]=9000
data.setdefault(102,2345)
print(data)
print(len(data))
print(data.get(101))
data.pop("rollno")
data.popitem()
print(data.keys())
print(data.values())
print(data.items())
