
'''kuki= bool(2==2)
print (kuki)'''

'''import random
szam =1
while szam ==1 :
    random.seed(10)
    print (random.seed())'''

'''from random import randrange
szam1= ()
szam = 1
while szam == 1 :
    szam1= [randrange(10) for szam1 in range(5) ]
    print(szam1)'''

'''honap = ["januar", "februar", "marcius" ]
szam = [10, 7 , 5]
minszam = min(szam)
sorszam = szam.index(minszam)
kishonap= honap[sorszam]
print(kishonap)'''


'''honap = ["januar", "februar", "marcius"]
szam = [6 , 1, 2]
kishonap= honap[szam.index(min(szam))]
print(kishonap)'''


'''szam = [ 3 ,1, 5, 10, 7, 4]
szam1 = sorted(szam, reverse=True)
print (szam1)'''


'''szavak = ["benned", "az", "abban", "ezt"]
print(sorted(szavak,key=len, reverse=True))'''

'''print((3, 4) > (2, 2) )'''


'''participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]''' #ezt folyt


'''def greet(name) :
  print(" Szia! " + name + ". Szép napunk van!")
greet('Gergő')'''



'''jatekosok= ["Bulcsú", "Gábor", "Irén", "Emese", "Karolina", "Béla"]
def uzenet() :
    felado= input("Ki vagy? ")
    cimzett= input("Kinek? " )
    hasonlitas1 = jatekosok.count(cimzett)
    if hasonlitas1 == 1 :
        uzeneted = input("Üzenet: ")
        print("Kedves " + cimzett + "! " + felado + " üzenetet küldött! " + uzeneted)
    else :
        print("Nincs ilyen játékos!")

uzenet()'''


'''
import sys
import time
import random

print("Loading:")
animation = ["[■■□□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■■]"]
for i in range(len(animation)):
    time.sleep(0.5)                                           #ezt nem én csináltan :(
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
pontok =0
while pontok <=100 :
 szam = random.randint(1,50)
 szam1= random.randint(1,50)
 osszeg = szam1 + szam
 time.sleep(0.8)
 print()
 print(szam, "+" , szam1)
 valasz = int(input("Mennyi ez? "))
 if valasz == osszeg :
     print("Helyes!")
     pontok = int(pontok + 1)
 else:
     pontok = int(pontok -1)
     print("Rossz! A helyes válasz: ",osszeg, " !")
 print("Pontjaid: ", pontok)
 time.sleep(1)
 if pontok == 10 :
     print("Nyertél!")
     break'''














