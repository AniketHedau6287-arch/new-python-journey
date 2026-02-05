# function-- reusability of code , redability of code.
# def functio_name(parameter):
#       code
#       return / print()

# non return type without argument
# def welcome():   # parameter
#     print("Welcome")

# welcome()        # argument

# # non return type with argument
# def addition(num1,num2):
#     print(num1+num2)

# a=10
# b=20
# addition(a,b)



# return type with argument

# def plusone(num):
#     return num+1

# a=20
# ans = plusone(a)
# print(ans)


# factorial

# def factorial(num):
#     ans=1
#     for i in range(1,num+1):
#         ans*=i
#     return ans


# a = int(input("Enter a Number "))
# ans = factorial(a)
# print(ans)


# fibonacci series
# 0 1 1 2 3 5 

# def fibonacci_series(num):
#     fi = 0
#     se = 1
#     for i in range(num):
#         print(fi,end=" ")
#         fi,se = se,fi+se
    
# fibonacci_series(5)


# pallindrom
# amstrong
# second largest in a list
# reverse a list
# count the digit in a number


#find the frequency of element in a list 

def frequency (li):
    freq = {}
    for i in li:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    return freq
liis=[1,52,5,11,2,15,21,1,1,11,1,1]
print(frequency(liis))    
        