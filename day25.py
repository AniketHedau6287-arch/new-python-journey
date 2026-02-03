#1
#12
#123
#1234
#12345

# n = 5
# st = ""
# for i in range (1,n+1):
#     st+= str(i)
#     print(st + " "*(n-i) )
    
# #1
# #22
# #333
# #4444
# #55555
# n = 5
# for i in range (1,n+1):
#    print(str(i)*i + ""*(n-i) )
   
#A
#AB
#ABC
#ABCD
#ABCDE
n = 5
st = ""
for i in range (1,n+1):
    st+= chr(64+i)
    print(st + " "*(n-i) )
    
#A
#BB
#CCC
#DDDD
#EEEEE
n = 26
for i in range (1,n+1):
   print(chr(64+i)*i + ""*(n-i) )



    
    
    
    
    
    
