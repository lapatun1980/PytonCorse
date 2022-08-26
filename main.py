import random
rock0 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper1 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors2 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
you=int(input("Enter rock - 0  or paper - 1 or scissors - 2  "))
if you==0: print(">>>Your choice - ROCK",rock0)
elif you==1: print(">>>Your choice - PAPER",paper1)
elif you==2: print (">>>Your choice - SCISSOR",scissors2)
  # PC choice
pc_choice=random.randint(0,2)
if pc_choice==0: print(">>>pc_choice choice - ROCK",rock0)
elif pc_choice==1: print(">>>pc_choice choice - PAPER",paper1)
elif pc_choice==2: print (">>>pc_choice choice - SCISSOR",scissors2)
  # Who are win
if you==pc_choice: print ("Drow")
elif you==0 and pc_choice==1: print ("You losse")
elif you==0 and pc_choice==2: print ("You WIN!!!")
elif you==1 and pc_choice==0: print ("You WIN!!!")
elif you==1 and pc_choice==2: print ("You losse")
elif you==2 and pc_choice==0: print ("You WIN!!!")
elif you==2 and pc_choice==1: print ("You losse")