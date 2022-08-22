year=int(input("Enter the year "))
if year%4!=0:
  print ("is NOT leap year ")
elif year%100!=0:
  print("is  leap year ")
elif year%400==0:
    print("is  leap year ")
else: print("is  NOT leap year ")