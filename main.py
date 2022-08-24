import random
a=random.randint(1,100)
test_seed=int(input("Enter the Seed number "))
random.seed(test_seed)
paier=random.randint(0,5)
names=input("Enters all name whith ', '")
name=names.split(", ")
print("The paier is  ", name[paier])