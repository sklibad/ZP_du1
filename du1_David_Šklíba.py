
from turtle import forward, exitonclick, left, right, penup, pendown, speed, setpos, circle
def map_projection():
    name = input('Zadej zkratku názvu zobrazení:')

    def iserror(func, *var_type, **value):
        try:
            func(*var_type, **value)
            return False
        except Exception:
            return True

    scale = input("Zadej číslo x vyjadřující měřítko mapy '1:x':")
    if iserror(int,scale) == True or int(scale) <= 0:
        exit('Měřítko musí být vyjádřeno kladným celým číslem')
    scale = int(scale)

    r = (input('Zadej poloměr Země:'))
    if iserror(float,r) == True or float(r) == 0:
        exit('Poloměr Země musí být vyjádřen nezáporným číslem')
    r = float(r)
    if r == 0:
        r = 6371.11

    par_int = input('Zadej po kolika stupních se mají vykreslit rovnoběžky:')
    if iserror(int,par_int) == True or int(par_int) < 0:
        exit('Interval rovnoběžek má být vyjádřen nezáporným celým číslem')
    par_int = int(par_int)
    if par_int == 0:
        par_int = 10
    if 360 % par_int != 0:
        exit('Interval rovnoběžel musí dělit číslo 360 beze zbytku')

    mer_int = input('Zadej po kolika stupních se mají vykreslit poledníky:')
    if iserror(int,mer_int) == True or int(mer_int) < 0:
        exit('Interval rovnoběžek má být vyjádřen nezáporným celým číslem')
    mer_int = int(mer_int)
    if mer_int == 0:
        mer_int = 10    
    if 360 % int(mer_int) != 0:
        exit('Interval poledníků musí dělit číslo 360 beze zbytku')
   
"""   
#pro ukončení zadávání souřadnic bodů je třeba zadat souřadnici X i souřadnici Y v následující podobě '000 00 00.000'
    i = 1
    while True:
        Xi_lat = 'X{}lat'.format(i)
        locals()[Xi_lat] = input("Zadej zeměpisnou šířku bodu ve formátu 'NDD MM SS.SSS':")
        if locals()[Xi_lat][0] == 'N' or locals()[Xi_lat][0] == 'S' or locals()[Xi_lat][0] == '0':
            if len(locals()[Xi_lat]) != 13 or iserror(int,locals()[Xi_lat][1:3]) == True or iserror(int,locals()[Xi_lat][4:6]) == True or iserror(float,locals()[Xi_lat][7:13]) == True:
                exit('Souřadnice zeměpisné šířky byly zadány v nesprávném formátu')
        else:
            exit("Prvním znakem zeměpisné šířky musí být písmeno 'N' nebo písmeno 'S'")
        Yi_lat = 'Y{}lat'.format(i)
        locals()[Yi_lat] = input("Zadej zeměpisnou délku bodu ve formátu 'EDD MM SS.SSS':")
        if locals()[Yi_lat][0] == 'E' or locals()[Yi_lat][0] == 'W' or locals()[Yi_lat][0] == '0':
            if len(locals()[Yi_lat]) != 13 or iserror(int,locals()[Yi_lat][1:3]) == True or iserror(int,locals()[Yi_lat][4:6]) == True or iserror(float,locals()[Yi_lat][7:13]) == True:
                exit('Souřadnice zeměpisné délky byly zadány v nesprávném formátu')
        else:
            exit("Prvním znakem zeměpisné délky musí být písmeno 'E' nebo písmeno 'W'")
        if locals()[Xi_lat] == '000 00 00.000' and locals()[Yi_lat] == '000 00 00.000':
            break

    if name = 'Or':

"""
map_projection()

