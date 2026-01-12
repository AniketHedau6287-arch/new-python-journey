#ATM 
#withdrawal 
# deposite 
# balance cheque 
pin = int(input("enter your pin"))
if pin==1234 :
    balance = 10000
    atm = input("choose your operation withdrawal deposite balance cheque")
    if atm=="withdrawal":
            amount=int(input("enter your amount"))
            if amount>0 and amount<=balance:
                print(balance-amount)
            else :
                    print("invalid")
    elif atm=="deposite":
            amount=int(input("enter your amount"))
            if amount>0 :
                print(balance+amount)
    elif atm=="balance cheque":
        amount=int(input("enter your amount"))
        print("your balance is ", balance)
    else :
                print("invalid")
else :
        print ("incorrect pin")
