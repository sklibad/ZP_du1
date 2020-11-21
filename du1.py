from turtle import forward, exitonclick, left, right, penup, pendown, speed, setpos, circle, pensize, pos
import math

#funkce, vytvářející zeměpisnou síť ortografické projekce (azimutální zobrazení) 
#s povinnými parametry 'r' = poloměr Země, 'par_int' = interval rovnoběžek, 'mer_int' = interval poledníků, 'km_per_pixel' = počet kilometrů na pixel
def ortographic_projection(r, par_int, mer_int, km_per_pixel): 
    speed(9)
    for par in range(0+par_int,100,par_int):
        r_par = r*math.sin(math.radians(par))
        r_par_scaled = r_par/km_per_pixel
        penup()
        setpos(0,-r_par_scaled)
        pendown()
        circle(r_par_scaled)
    penup()
    setpos(0,0)
    pendown()
    right(90)
    for mer in range(int(360/mer_int)):
        forward(r_par_scaled)
        setpos(0,0)
        left(mer_int) 

#funkce, vytvářející bod o souřadnicích Xi_lat a Yi_long v zeměpisné síti ortografické projekce
#s povinnými parametry 'r' = poloměr Země, 'Xi_lat' = souřadnice zeměpisné šířky zadaná uživatelem, 'Xi_long' = souřadnice zeměpisné délky zadaná uživatelem, 
#'Lat_deg' = souřadnice zeměpisné šířky ve stupních, 'Long_deg' = souřadnice zeměpisné délky ve stupních, 'km_per_pixel' = počet kilometrů na pixel
#toto zobrazení je vytvořeno pouze pro severní zeměpisnou šířku, není tedy povoleno zadávat body ležící na jižní zeměpisné šířce  
def ortographic_projection_point(r, Xi_lat, Yi_long, Lat_deg, Long_deg, km_per_pixel):
    if Xi_lat[0] == 'S':
        exit('Zadávat lze pouze body ležící na severní zeměpisné šířce')
    
    #v proměnné 'point_r' je uložen poloměr kružnice bodu vztažený k měřítku
    point_r = (r*math.sin(math.radians(90)) - r*math.sin(math.radians(80)))/km_per_pixel
    pensize(2)             
    dist = r*math.sin(math.radians(90-Lat_deg))/km_per_pixel
    if Yi_long[0] == 'E':
        left(Long_deg)
        if Long_deg < 90:
            angle = 270 + Long_deg
        elif Long_deg >= 90 and Long_deg <= 180:
            angle = Long_deg - 90      
    elif Yi_long[0] == 'W':
        right(Long_deg)
        angle = 270 - Long_deg   
    penup()
    forward(dist + point_r)
    pendown()
    left(90)
    circle(point_r)
    penup()
    setpos(0,0)
    pendown()
    if Yi_long[0] == 'E':  
        right(90 + Long_deg)
    elif Yi_long[0] == 'W':   
        right(90 - Long_deg)
    if Long_deg == 0 or Long_deg == 180:
        x = 0.0
    else:
        x = dist*math.cos(math.radians(angle))*0.3
    y = dist*math.sin(math.radians(angle))*0.3
    print('Souřadnice Vámi zadaného bodu v kartézském souřadnicovém systému jsou: (x,y) = ({},{})mm'.format(x,y))

#funkce, vytvářející zeměpisnou síť Lambertova zobrazení (válcové zobrazení)
#s povinnými parametry 'r' = poloměr Země, 'par_int' = interval rovnoběžek, 'mer_int' = interval poledníků, 'km_per_pixel' = počet kilometrů na pixel
def lambert_projection(r, par_int, mer_int, km_per_pixel):
    speed(9)
    for par in range(0,90+par_int,par_int):
        penup()
        setpos(-math.pi*r/km_per_pixel,r*math.sin(math.radians(par))/km_per_pixel)
        pendown()
        forward(2*math.pi*r/km_per_pixel)
    for par in range(par_int,90+par_int,par_int):
        penup()
        setpos(-math.pi*r/km_per_pixel,-r*math.sin(math.radians(par))/km_per_pixel)
        pendown()
        forward(2*math.pi*r/km_per_pixel) 
    n = 360/mer_int 
    right(90) 
    for mer in range(0,int(n)+1):
        penup()
        setpos(-math.pi*r/km_per_pixel+mer*2*math.pi*r/(n*km_per_pixel),r*math.sin(math.radians(90))/km_per_pixel)
        pendown()
        forward(2*r*math.sin(math.radians(90))/km_per_pixel)
    left(90)

#funkce, vytvářející bod o souřadnicích Xi_lat a Yi_long v zeměpisné síti Lambertova zobrazení
#s povinnými parametry 'r' = poloměr Země, 'Xi_lat' = souřadnice zeměpisné šířky zadaná uživatelem, 'Xi_long' = souřadnice zeměpisné délky zadaná uživatelem, 
#'Lat_deg' = souřadnice zeměpisné šířky ve stupních, 'Long_deg' = souřadnice zeměpisné délky ve stupních, 'km_per_pixel' = počet kilometrů na pixel
def lambert_projection_point(r, Xi_lat, Yi_long, Lat_deg, Long_deg, km_per_pixel):
    point_r = (r*math.sin(math.radians(90)) - r*math.sin(math.radians(80)))/km_per_pixel
    pensize(2)
    if Yi_long[0] == 'E':
        X_pos = math.pi*r*Long_deg/(180*km_per_pixel)
    elif Yi_long[0] == 'W':
        X_pos = -math.pi*r*Long_deg/(180*km_per_pixel)
    if Xi_lat[0] == 'N':
        Y_pos = r*math.sin(math.radians(Lat_deg))/km_per_pixel
    elif Xi_lat[0] == 'S':
        Y_pos = -r*math.sin(math.radians(Lat_deg))/km_per_pixel
    penup()
    setpos(X_pos,Y_pos-point_r)
    pendown()
    circle(point_r)
    print('Souřadnice Vámi zadaného bodu v kartézském souřadnicovém systému jsou: (x,y) = ({},{})mm'.format(X_pos*0.3, Y_pos*0.3))
        
#funkce, vytvářející zeměpisnou síť Ptolemaiova zobrazení (kuželové zobrazení)
#s povinnými parametry 'r' = poloměr Země, 'par_int' = interval rovnoběžek, 'mer_int' = interval poledníků, 'km_per_pixel' = počet kilometrů na pixel
def ptolemys_projection(r, par_int, mer_int, km_per_pixel):
    speed(9)
    konst = r*math.tan(math.radians(60))
    right(90)
    move_up = (konst + r*math.pi*20/180)/km_per_pixel
    for par in range(0,180+par_int,par_int):
        X_pos = -(konst + r*math.pi*(par-60)/180)/km_per_pixel
        penup()
        setpos(X_pos,move_up)
        pendown()
        circle(-X_pos,180)
        left(180)
    right(90)   
    for mer in range(0,int(360/mer_int)+1):
        penup()
        setpos(0,move_up)
        forward((konst - r*math.pi*60/180)/km_per_pixel)
        pendown()
        forward(((konst + r*math.pi*120/180)/km_per_pixel)-((konst - r*math.pi*60/180)/km_per_pixel))
        left(mer_int/2)         
    right(mer_int/2+90)

#funkce, vytvářející bod o souřadnicích Xi_lat a Yi_long v zeměpisné síti Ptolemaiova zobrazení
#s povinnými parametry 'r' = poloměr Země, 'Xi_lat' = souřadnice zeměpisné šířky zadaná uživatelem, 'Xi_long' = souřadnice zeměpisné délky zadaná uživatelem, 
#'Lat_deg' = souřadnice zeměpisné šířky ve stupních, 'Long_deg' = souřadnice zeměpisné délky ve stupních, 'km_per_pixel' = počet kilometrů na pixel,
#'konst' = r*math.tan(math.radians(60)), 'move_up' = (konst + r*math.pi*20/180)/km_per_pixel
def ptolemys_projection_point(r, Xi_lat, Yi_long, Lat_deg, Long_deg, km_per_pixel, konst, move_up):
    point_r = 0.2*(((konst + r*math.pi*20/180)/km_per_pixel)-((konst + r*math.pi*10/180)/km_per_pixel))
    pensize(2)
    penup()
    setpos(0,move_up)
    pendown()
    if Yi_long[0] == 'E':
        left(Long_deg/2)
        if Long_deg/2 < 90:
            angle = 270 + Long_deg/2
        elif Long_deg >= 90 and Long_deg <= 180:
            angle = Long_deg - 90
    elif Yi_long[0] == 'W':
        right(Long_deg/2)
        angle = 270 - Long_deg/2
    if Xi_lat[0] == 'N':
        penup()
        dist = (konst + r*math.pi*(30-Lat_deg)/180)/km_per_pixel
        forward(dist + point_r)
        left(90)
        pendown()
        circle(point_r)                   
        if Yi_long[0] == 'E':
            right(90+Long_deg/2)
        elif Yi_long[0] == 'W':
            right(90-Long_deg/2)
    elif Xi_lat[0] == 'S':
        penup()
        dist = (konst + r*math.pi*(Lat_deg + 30)/180)/km_per_pixel
        forward(dist + point_r)
        left(90)
        pendown()
        circle(point_r)                   
        if Yi_long[0] == 'E':
            right(90+Long_deg/2)
        elif Yi_long[0] == 'W':
            right(90-Long_deg/2)
    if Long_deg == 0:
        x = 0.0
    else:
        x = dist*math.cos(math.radians(angle))*0.3
    y = (dist*math.sin(math.radians(angle)) + move_up)*0.3
    print('Souřadnice Vámi zadaného bodu v kartézském souřadnicovém systému jsou: (x,y) = ({},{})mm'.format(x,y))

#funkce, vytvářející zeměpisnou síť Werner-Stabova zobrazení (nepravé zobrazení)
#s povinnými parametry 'r' = poloměr Země, 'par_int' = interval rovnoběžek, 'mer_int' = interval poledníků, 'km_per_pixel' = počet kilometrů na pixel
def stab_werner_projection(r, par_int, mer_int, km_per_pixel):
    speed(9)
    left(90)
    for par in range(par_int,180,par_int):
        a_rad = 360*math.sin(math.radians(par))/par
        a_deg = a_rad*180/math.pi
        angle = (360-a_deg)/2
        left(angle)
        penup()
        forward(r*math.radians(par)/km_per_pixel)
        left(90)
        pendown()
        circle(r*math.radians(par)/km_per_pixel,a_deg)
        right(90-angle)
        penup()
        setpos(0,0)
        pendown
    X = []
    Y = []
    for par in range(1,181):
        Xi = []
        Yi = []
        a_rad = 360*math.sin(math.radians(par))/par
        a_deg = a_rad*180/math.pi
        angle = (360-a_deg)/2
        mer_diff = a_deg*mer_int/360
        for mer in range(0,int(360/mer_int)+1):
            if angle + mer*mer_diff < 90:
                Xi.append(-r*math.radians(par)*math.sin(math.radians(angle+mer*mer_diff))/km_per_pixel)
                Yi.append(r*math.radians(par)*math.cos(math.radians(angle+mer*mer_diff))/km_per_pixel)
            elif angle + mer*mer_diff > 90 and angle + mer*mer_diff < 180:
                Xi.append(-r*math.radians(par)*math.cos(math.radians(angle+mer*mer_diff-90))/km_per_pixel)
                Yi.append(-r*math.radians(par)*math.sin(math.radians(angle+mer*mer_diff-90))/km_per_pixel)
            elif angle + mer*mer_diff == 180:
                Xi.append(0)
                Yi.append(-r*math.radians(par)/km_per_pixel)
            elif angle + mer*mer_diff > 180 and angle + mer*mer_diff < 270:
                Xi.append(r*math.radians(par)*math.sin(math.radians(angle+mer*mer_diff-180))/km_per_pixel)
                Yi.append(-r*math.radians(par)*math.cos(math.radians(angle+mer*mer_diff-180))/km_per_pixel)
            elif angle + mer*mer_diff > 270 and angle + mer*mer_diff < 360:
                Xi.append(r*math.radians(par)*math.cos(math.radians(angle+mer*mer_diff-270))/km_per_pixel)
                Yi.append(r*math.radians(par)*math.sin(math.radians(angle+mer*mer_diff-270))/km_per_pixel)       
        X.append(Xi)
        Y.append(Yi)
    i = 0
    j = 0
    while True:
        X_pos = X[i][j]
        Y_pos = Y[i][j]
        pendown()
        setpos(X_pos,Y_pos)
        i += 1
        if i == len(X):
            penup()
            setpos(0,0)
            pendown()
            i = 0
            j += 1
        if j == len(X[0]):
            break

#funkce, vytvářející bod o souřadnicích Xi_lat a Yi_long v zeměpisné síti Werner-Stabova zobrazení
#s povinnými parametry 'r' = poloměr Země, 'Xi_lat' = souřadnice zeměpisné šířky zadaná uživatelem, 'Xi_long' = souřadnice zeměpisné délky zadaná uživatelem, 
#'Lat_deg' = souřadnice zeměpisné šířky ve stupních, 'Long_deg' = souřadnice zeměpisné délky ve stupních, 'km_per_pixel' = počet kilometrů na pixel
def stab_werner_projection_point(r, Xi_lat, Yi_long, Lat_deg, Long_deg, km_per_pixel):
    pensize(2)
    point_r = (r*math.radians(3) - r*math.radians(1))/km_per_pixel
    if Xi_lat[0:3] == 'N90':
        penup()
        forward(point_r)
        left(90)
        pendown()
        circle(point_r)
        right(90)
        penup()
        setpos(0,0)
        pendown()
        x = 0.0
        y = 0.0
    else:          
        if Xi_lat[0] == 'N':
            par_dist = r*math.radians(90 - Lat_deg)/km_per_pixel
            a_rad = 360*math.sin(math.radians(90 - Lat_deg))/(90 - Lat_deg)
        elif Xi_lat[0] == 'S':
            par_dist = r*math.radians(Lat_deg + 90)/km_per_pixel
            a_rad = 360*math.sin(math.radians(Lat_deg + 90))/(Lat_deg + 90)
        a_deg = a_rad*180/math.pi
        angle1 = (360 - a_deg)/2
        segment1 = a_deg/360
        angle2 = (180 - Long_deg)*segment1
        if Yi_long[0] == 'W':               
            left(angle1 + angle2)
            angle = angle1 + angle2 + 90
        elif Yi_long[0] == 'E':
            right(angle1 + angle2)
            if angle1 + angle2 <= 90:
                angle = 90 - angle1 - angle2
            elif angle1 + angle2 > 90 and angle1 + angle2 <= 180:
                angle = 450 - angle1 - angle2
        penup()
        forward(par_dist + point_r)
        pendown()
        left(90)
        circle(point_r)
        if Yi_long[0] == 'W':               
            right(angle1 + angle2 + 90)
        elif Yi_long[0] == 'E':
            left(angle1 + angle2 - 90)
        penup()
        setpos(0,0)
        pendown()
        if Xi_lat[0:3] == 'S90':
            x = 0.0
        else:
            x = par_dist*math.cos(math.radians(angle))*0.3
        y = par_dist*math.sin(math.radians(angle))*0.3
    print('Souřadnice Vámi zadaného bodu v kartézském souřadnicovém systému jsou: (x,y) = ({},{})mm'.format(x,y))

#funkce, pomocí které autor zadá souřadnici zeměpisné šířky v daném formátu
def latitude_input():
    Xi_lat = input("Zadej zeměpisnou šířku bodu ve formátu 'NDD MM SS.SSS':")
    if Xi_lat == '0':
        Xi_lat = '000 00 00.000'
    if Xi_lat[0] == 'N' or \
        Xi_lat[0] == 'S' or \
        Xi_lat[0] == '0':
        if len(Xi_lat) != 13 or \
            iserror(int,Xi_lat[1:3]) == True or \
            iserror(int,Xi_lat[4:6]) == True or \
            iserror(float,Xi_lat[7:13]) == True:
            exit('Souřadnice zeměpisné šířky byly zadány v nesprávném formátu')
    else:
        exit("Prvním znakem zeměpisné šířky musí být písmeno 'N' nebo písmeno 'S'")
    return Xi_lat

#funkce, pomocí které autor zadá souřadnici zeměpisné délky v daném formátu, při dvouciferné hodnotě stupňů je potřeba před toto číslo napsat "nulu": 0
def longitude_input():
    Yi_long = input("Zadej zeměpisnou délku bodu ve formátu 'EDDD MM SS.SSS':")
    if Yi_long == '0':
        Yi_long = '0000 00 00.000'
    if Yi_long[0] == 'E' or \
        Yi_long[0] == 'W' or \
        Yi_long[0] == '0':
        if len(Yi_long) != 14 or \
            iserror(int,Yi_long[1]) == True or \
            iserror(int,Yi_long[2:4]) == True or \
            iserror(int,Yi_long[5:7]) == True or \
            iserror(float,Yi_long[8:14]) == True:
            exit('Souřadnice zeměpisné délky byly zadány v nesprávném formátu')
    else:
        exit("Prvním znakem zeměpisné délky musí být písmeno 'E' nebo písmeno 'W'")
    return Yi_long

#funkce, přeměňující zeměpisné souřadnice z daného formátu do stupňového tvaru
def latitude_longitude_degrees(Xi_lat, Yi_long):
    Lat_deg = int(Xi_lat[1:3]) + int(Xi_lat[4:6])/60 + float(Xi_lat[7:13])/3600
    if Yi_long[1] == '0':
        Long_deg = int(Yi_long[2:4]) + int(Yi_long[5:7])/60 + float(Yi_long[8:14])/3600
    else:
        Long_deg = int(Yi_long[1:4]) + int(Yi_long[5:7])/60 + float(Yi_long[8:14])/3600

    if Lat_deg > 90:
        exit('Byla zadána příliš velká hodnota pro zeměpisnou šířku')
    if Long_deg > 180:
        exit('Byla zadána příliš velká hodnota pro zeměpisnou délku')
    return Lat_deg, Long_deg

#funkce, s parametry 'var_type' reprezentující typ proměnné a 'value' reprezentující libovolnou hodnotu, vracející hodnotu typu boolean
#pokud hodnota 'value' nelze uložit do proměnné typu 'var_type', potom iserror() = True 
def iserror(func, *var_type, **value):
    try:
        func(*var_type, **value)
        return False
    except ValueError:
        return True

#funkce, vykreslující kartografické zobrazení
def map_projection():
    print('Program podporuje Ortografickou projekci (Or), Lambertovo válcové zobrazení (Lv), Ptolemaiovo zobrazení (Pt) a Werner-Stabovo zobrazení (We).')
    
    #proměnná 'defined_names' obsahuje seznam zkratek definovaných kartografických zobrazeních ve funkci map_projection()
    defined_names = ['Or','Lv','Pt','We']
    
    #proměnná 'name' určuje zkratku kartografického zobrazení, které se má vykreslit
    name = input('Zadej zkratku názvu zobrazení:')
    if name not in defined_names:
        exit('Toto zobrazení není definováno, zadej jednu z následujících zkratek: {}'.format(defined_names))
    
    #proměnná 'scale' vyjadřuje měřítko, ve kterém bude kartografické zobrazení vytvořeno
    scale = input("Zadej číslo x vyjadřující měřítko mapy '1:x':")
    if iserror(int,scale) == True or int(scale) <= 0:
        exit('Měřítko musí být vyjádřeno kladným celým číslem')
    scale = int(scale)
    
    #proměnná 'r' v sobě uchovává poloměr Země
    r = (input('Zadej poloměr Země:'))
    if iserror(float,r) == True or float(r) < 0:
        exit('Poloměr Země musí být vyjádřen nezáporným číslem')
    r = float(r)
    if r == 0:
        r = 6371.11
    
    #v proměnné 'par_int' je uložen interval (počet stupňů), po kterém se mají zobrazit jednotlivé rovnoběžky
    par_int = input('Zadej po kolika stupních se mají vykreslit rovnoběžky:')
    if iserror(int,par_int) == True or int(par_int) < 0:
        exit('Interval rovnoběžek má být vyjádřen nezáporným celým číslem')
    par_int = int(par_int)
    if par_int == 0:
        par_int = 10
    if 90 % par_int != 0:
        exit('Interval rovnoběžek musí dělit číslo 90 beze zbytku')
    
    #v proměnné 'mer_int' je uložen interval (počet stupňů), po kterém se mají zobrazit jednotlivé poledníky
    mer_int = input('Zadej po kolika stupních se mají vykreslit poledníky:')
    if iserror(int,mer_int) == True or int(mer_int) < 0:
        exit('Interval rovnoběžek má být vyjádřen nezáporným celým číslem')
    mer_int = int(mer_int)
    if mer_int == 0:
        mer_int = 10    
    if 360 % int(mer_int) != 0:
        exit('Interval poledníků musí dělit číslo 360 beze zbytku')

    #proměnná 'km_per_pixel' vyjadřuje počet kilometrů na jeden pixel v zadaném měřítku
    km_per_pixel = 3/10000000 * scale

    if name == 'Or':
        ortographic_projection(r,par_int,mer_int,km_per_pixel)      
    elif name == 'Lv':
        lambert_projection(r, par_int, mer_int, km_per_pixel)
    elif name == 'Pt':
        ptolemys_projection(r, par_int, mer_int, km_per_pixel)
    elif name == 'We':
        stab_werner_projection(r, par_int, mer_int, km_per_pixel)
    
    #cyklus zadávání, vykreslování a vypisování souřadnic daného bodu
    #pro ukončení zadávání souřadnic: (Xi_lat,Yi_long) = (0,0)
    while True:
        Xi_lat = latitude_input()
        Yi_long = longitude_input()
        if Xi_lat == '000 00 00.000' and Yi_long == '0000 00 00.000':
            break
        
        [Lat_deg, Long_deg] = latitude_longitude_degrees(Xi_lat, Yi_long)
      
        if name == 'Or':
            ortographic_projection_point(r, Xi_lat, Yi_long, Lat_deg, Long_deg, km_per_pixel)    
        elif name == 'Lv':
            lambert_projection_point(r, Xi_lat, Yi_long, Lat_deg, Long_deg, km_per_pixel)
        elif name == 'Pt':
            konst = r*math.tan(math.radians(60))
            move_up = (konst + r*math.pi*20/180)/km_per_pixel
            ptolemys_projection_point(r, Xi_lat, Yi_long, Lat_deg, Long_deg, km_per_pixel, konst, move_up)
        elif name == 'We':
            stab_werner_projection_point(r, Xi_lat, Yi_long, Lat_deg, Long_deg, km_per_pixel)
    exitonclick()
map_projection()