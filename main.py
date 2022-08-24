import random
a=random.randint(1,100)
test_seed=int(input("Enter the Seed number "))
random.seed(test_seed)

names=input("Enters all name whith ', '")
name=names.split(", ")
payer=random.randint(0,len(name))
print("The payer is  ", name[payer])