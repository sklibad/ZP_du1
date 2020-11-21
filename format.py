"""
option = input("Pokud zadáváš stupně: zadej 'D', pokud zadáváš stupně, minuty, vteřiny: zadej 'DMS'") 
if option == "D":
    deg = float(input("Zadej stupně:"))
    min = (deg % 1) * 60
    print("Převod hodnoty {} stupňů na formát DMS je následovný: {:.0f} stupňů {:.0f} minut {:.2f} vteřin".format(deg, deg // 1, min, (min % 1) * 60))
elif option == "DMS":
    DMS = input("Zadej souřadnici ve formátu N DD MM' SS.SSS'':")
    print("Převod hodnoty souřadnice {} na stupně vypadá následovně: {}".format(DMS,int(DMS[2:4]) + int(DMS[5:7])/60 + float(DMS[9:15])/3600))    
else:
    print("Zadali jste neplatnou zkratku")
"""

def nakresli_ctverec(a,s):
    from turtle import forward, exitonclick, left, right, speed
    speed(s)
    for k in range(5):
        forward(a)
        right(90)
    exitonclick()

def nakresli_radek(x,a,s):
    from turtle import forward, exitonclick, left, right, speed
    speed(s)
    for j in range(x):
        nakresli_ctverec(a,s)
        left(90)
    left(180)
    forward(x*a)
    left(90)
    forward(a)
    left(90)   
    exitonclick()

def nakresli_tabulku(x,y,a,s):    
    from turtle import forward, exitonclick, left, right, speed
    for i in range(y):
        nakresli_radek(x,a,s)
    exitonclick()

nakresli_tabulku(2,3,50,7)