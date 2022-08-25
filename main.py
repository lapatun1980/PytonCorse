a1=['⬜️', '⬜️', '⬜️']
a2=['⬜️', '⬜️', '⬜️']
a3=['⬜️', '⬜️', '⬜️']
b=[a1,a2,a3]
print(f"{a1}\n{a2}\n{a3}\n")
place=input("Enter column & rou")
x=int(place[0])
y=int(place[1])
change=b[x-1]
change[y-1]="X"
print(f"{a1}\n{a2}\n{a3}\n")
