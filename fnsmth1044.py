#code for gtBank 737 is the code
print("pleas enter your USSD code")
option=input("")
if (option=="737"):
		print("1.Airtime-Self\n2.Airtime-others\n3.Data\n4Trsf-GTB\n5.Trsf-Others\n6.trsf-MFB/ewallet\n7.Cable TV\n8.Pay Bills\n Next")
option=input("")
if (option=="1"):
    amount=input("Enter Amount")
    pin=input("Enter pin")
    print("Recharge successful")
    back=input("Enter 1 To go back to menu")
    print("Enter 2 to next")
    option=input("")
    if (option=="2"):
    		amount=input("Enter Amount")
    		number=input("Enter phone number")
    		pin=input("Enter pin")
    		print("recharge successful")
    		option=input("")
    		if (option=="3"):
    			print("1.100mb=100N\n2.200=200N")
    			if (option=="1"):
    			 amount=input("Enter Amount")
    			number=input("Enter phone number")
    			print("Enter 1 to confrim")
    			confirm=input("press 1")
    			print("data recharge successful")
    			option=input("")
    			if (option=="4"):
    				account_number=input("Enter the acct number")
    			print(" the name of the account is OBEYA PATRICK")
    			amount=input("Enter Amount")
    			confirm_amount=input("Enter 1 to continue")
    			pin=input("Enter four pin")
    			print("transfer successful")
    			print("thanks for banking with GTBank")
    			option=input("")
    			if(option=="5"):
    				account_number=input("Enter Account Number")
    				print("1.firstbank\n2.Uba\n3.zenith\n4.union\n5.Access\n6.Others")
    				if(option=="1"):
    					sellect=input("the account name is OBEYA PATRICK")