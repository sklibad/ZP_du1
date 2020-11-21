
import math
a_str = input("Zadej koeficient a^2: ")
a = int(a_str)
b_str = input("Zadej koeficient b: ")
b = int(b_str)
c_str = input("Zadej koeficient c: ")
c = int(c_str)
D = b**2-4*a*c
if D < 0:
    break
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b-math.sqrt(D))/(2*a)
if D > 0:
    print("Rovnice má 2 kořeny: ",x1," a ",x2)
elif D == 0:
    print("Rovnice má jeden dvojnásobný kořen: ",x1)
else:
    print("Rovnice nemá žádný reálný kořen")


vstup_str = input("Zadej číslo:")
vstup_int = int(vstup_str)
print(type(vstup_int))
print(type("12"))
print(type(12))

deg = int(input("Zadej stupně: "))
min = int(input("Zadej minuty: "))
sec = float(input("Zadej vteřiny: ")
vysledek1 = deg + min/60 + sec/3600
print(vysledek1)

vstup = input("Zadej stupně: "))
vstup = float(vstup)
stupne = vstup // 1
minuty = (vstup % 1) * 60
vteriny = (minuty % 1) * 60
print(stupne,"°",minuty,"'",vteriny,"''")

