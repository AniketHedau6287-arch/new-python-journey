#SET QUESTIONS
#Create a set with numbers 1–10
# set = {1,2,3,4,5,6,7,8,9,10}
# print (set)

#Check if an element exists
# "apple" in {"apple","banana","cherry"} → True
# set={"apple","banana","cherry"}
# print ("apple" in set)

# # Convert list with duplicates into a set
# # [1,2,2,3,4,4] → {1,2,3,4}
# numbers = [1, 2, 2, 3, 4, 4]
# unique_numbers = set(numbers)
# print(unique_numbers)

# Find length of a set
# {10,20,30} → length = 3
# set = {10,20,30,40}
# print(len(set))

# Remove duplicate words from a sentence
# "this is is a test" → {'this','is','a','test'}
# sentence = "this is is a test"
# words = set(sentence.split())
# print(words)

#Unique values from list of tuples
# [(1,2),(2,3),(3,4)] → {1,2,3,4}

# Uncommon elements between lists
# L1=[1,2,3], L2=[2,3,4] → {1,4}
# x = [1,2,3]
# y = [2,3,4]
# uncomman = set(x) ^ set(y)
# print(uncomman)

# Elements in all three lists
# [1,2,3], [2,3,4], [3,4,5] → {3}
# L1 = [1,2,3,]
# L2 = [2,3,4,]
# L3 = [3,4,5,]
# comman = set(L1) & set(L2) & set(L3)
# print (comman)

# DICTIONARY QUESTIONS 

# Create dictionary of students
# {"Aman":85, "Ravi":92, "Neha":78}
# student ={}
# student["Aman"]=85
# student["Ravi"]=92
# student["Neha"]=78
# print(student)

#Access value by key
# marks["Ravi"] → 92
# student = {"Aman":85, "Ravi":92, "Neha":78}
# print(student.get("Ravi"))

# Add/Update value
# marks["Neha"]=80
# student = {"Aman":85, "Ravi":92, "Neha":78}
# student["Neha"]=80
# print(student)

#Delete a key
# del marks["Aman"]
# student = {"Aman":85, "Ravi":92, "Neha":78}
# student.pop("Aman")
# print(student)

# Check if key exists
# "Ravi" in marks → True
# student = {"Aman":85, "Ravi":92, "Neha":78}
# print ("True" if "Ravi" in student else "False")

# Lists to dictionary
# keys=["a","b"], vals=[1,2] → {"a":1,"b":2}





