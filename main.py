'''import time
szam = 0
while szam < 9 :
    print ("a szám ", szam)
    szam = szam + 1
    time.sleep(1)

print ("Good bye!")'''

'''line1 = open ("szoveg.txt")
szöveg = line1.readline(4)
print (szöveg)'''




'''import time
szoveg = open("szoveg.txt")
szoveg1 = szoveg.readline (4)
print (szoveg1)
time.sleep(1)
szoveg1= szoveg.readline(11.)
print(szoveg1)'''

kor= []
kor = input ("Hány éves vagy? ")
 if kor < 5 :
    print("Kisbaba vagy!")
 elif kor >5 but : kor < 10 :
    print("Kisgyerek vagy!")
 elif kor >10 but :kor < 22 :
    print("Kamasz vagy!")
 elif kor > 22 but :kor < 65 :
    print ("Felnőtt vagy! ")
 elif kor >65 but :kor < 85 :
    print ("Idős vagy!")
 else kor > 85 :
 print ("Szépkorú vagy!")
 time.sleep(2)