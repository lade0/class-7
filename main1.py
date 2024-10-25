# activity 1 exam eligibility check
check1=input("do you have a medical cause enter y or n:")
check2=int(input("enter your attendanc e score"))

if check1== "y":
    print("you are allowed to take the test")
else:
    if check2>=75:
        print("you can take the test")
    else:
        print("you are not allowed to take the test")