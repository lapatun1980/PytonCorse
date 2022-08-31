import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words=['ball', 'apple', 'botle', 'woman', 'brad' ]
word=random.choice(words)
finde_word=[]
for i in range(0,len(word)):
    finde_word+="_"
# print(finde_word)
    people=0
    last_latter=len(word)
while (people<7 and last_latter!=0):
    counter=0
    latter=input("Enter letter")
    for i in range(0, len(word)):
        if latter==word[i]:
            finde_word[i]=word[i]
            counter+=1
            last_latter-=1
    if counter!=0:
        print (finde_word)
    else:
        print("wronge")
        people+=1
        print(stages[7-people])
win_word=""
for i in range(0,len(word)):
    win_word+=finde_word[i]

if people==7:
    print("YOU LOSSE")
else:
    print ("YUO WIN!", win_word)
  

     
    