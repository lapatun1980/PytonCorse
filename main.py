height=float(input("Enter you height m "))
weight=float(input("Enter you weight kg "))
rezult=weight/height**2
if rezult <=18.5: 
  print ("UNDERWEIGHT")
if rezult>18.5 and rezult <=25:
  print ("normal weight")
if rezult>25 and rezult<=30:
  print ("over weight")
if rezult>30 and rezult<=35:
  print ("obese")

if rezult>35:
  print ("clinicall obese")
