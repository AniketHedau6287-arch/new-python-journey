#print 1 to 10 numbers 
# for i in range (1,11,1):
#     print(i,end=" ")

#print 1 to 10 even number 
# for i in range(1,10):
#     if i%2==0:
#         print(i,end=" ")

#print all number present in list
# nums = [10, 20, 30, 40, 50]
# for i in nums:
#     print(i,end=" ")

# add all numbers 1 to 100
# sum = 0

# for i in range(1, 101):
#     sum = sum + i

# print(sum)

#print table of 5 
# for i in range (1,11):
#     print(i*5)

#counr the even numbers in the list
# nums = [2, 5, 8, 9, 10, 13, 20]
# even = 0
# for i in nums:
#     if i%2==0:
#         even = even+1
# # print(even)

#reverce the number 
# num = 9009272561
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print(reverse)

#check the number is palindrome or not 
# num = input("enter any number")
# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#check the palindrome in string and sentence 
# import string

# sentence = "A man a plan a canal Panama"

# # 1. Lowercase
# s = sentence.lower()

# # 2. Remove spaces and punctuation
# s = "".join(c for c in s if c.isalnum())  # alphanumeric characters only

# # 3. Reverse and compare
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# #print 1 to 20 numbers 
# for i in range (1,21):
#     if i%2!=0:
#         print(i,end=" ")

#print the square of numbers present in the list 
# nums = [2, 4, 6, 8]
# square = 0
# for i  in nums :
#     square = i*i
#     print(square,end=" ")

# print the all character in different line 
# word = "python"
# for i in word :
#     print(i)

# count the number greater than 10 present in list 
# nums = [5, 12, 30, 7, 18, 3, 25,100]
# count = 0
# for i in nums :
#     if i>10:
#         count = count+1 
# print(count)

#sum of this numbers 
# nums = 9999999999
# sum = 0
# while nums>0 :
#     digit = nums % 10
#     sum = sum + digit 
#     nums = nums // 10
# print (sum)

# print the numbers which are divisible by 3 ans 5 for 1 to 50
# for i in range (1,51):
#     if i%3==0 and i%5==0 :
#         print(i,end=" ")

# find the max number in the list 
# nums = [12, 45, 2, 89, 34, 67]
# bada_num = nums[0]
# for i in nums:
#     if i>bada_num:
#         bada_num = i
# print(bada_num)

# count the digit present in num
# nums=987654
# count=0
# while nums>0:
#     digit = nums %10
#     count=count+1
#     nums = nums // 10
# print(count)

#find the factorial of the number 
num = 50
fact=1
while num>0:
    fact = fact*num
    num=num-1
print(fact) 
    

    





