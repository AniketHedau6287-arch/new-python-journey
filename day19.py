#sum of a number from 1 to 10 ?
# sum = 0
# for i in range(1,11):
#     sum = sum + i 
# print(sum)

#sum of a number from 1 to n ?
# num = int(input("enter"))
# sum = 0
# for i in range (1,num+1):
#     sum = sum + i
# print(sum)

#sum of even number from 1 to 10?
# sum = 0
# for i in range(1,11):
#     if i%2==0:
#         sum = sum + i
# print(sum)

# #sum num of odd number from 1 to 10 ?
num = int(input("enter"))
sum = 0
for i in range(1,num):
    if num%i==0:
        sum = sum +i
if num==sum:
     print("perfect")
else:
    print("not perfect")

#factorial of 5 
# num = int(input("enter"))
# sum = 1
# for i in range(1,num+1):
#         sum = sum * i
# print(sum)

# num = 5
# sum = 1
# while num>0:
#         sum=sum*