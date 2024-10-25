# activity3 customise your ride
mystery1=int(input("enter your choice of ride, 1.bike or 2.car"))
if mystery1==1:
    bike=int(input("enter your bike choice,1.scootie or 2.bulletbike"))
    if bike==1:
        print("you have selected scootie")
    else:
        print ("you have selected bulletbike")
elif mystery1==2:
    car=int(input("enter your car choice,1.toyota or 2.ferrari"))
    if car==1:
        print("you have selected toyota")
    else:
        print("you have selected ferrari")
else:
    print("you have entered wrong choice")