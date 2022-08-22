height=float(input("Enter you height m "))
weight=float(input("Enter you weight kg "))
bmi=round(weight/height**2)
if bmi <18.5: 
  print (f" {bmi} UNDERWEIGHT")
if bmi>=18.5 and bmi <25:
  print (f" {bmi} normal weight")
if bmi>=25 and bmi<30:
  print (f" {bmi} over weight")
if bmi>=30 and bmi<35:
  print (f" {bmi} obese")

if bmi>=35:
  print (f" {bmi} clinicall obese")
