import random
a=random.randint(1,100)
test_seed=int(input("Enter the Seed number "))
random.seed(test_seed)
rais=random.randint(0,1)
if rais==0:
  print ("Heds")
else: 
  print ("Tails")