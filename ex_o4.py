# 4. x,y,z (int)
# Afiseaza care este cel mai mare dintre ele.

x = int(input('Introduceti primul numar : '))
y = int(input('Introduceti al doilea numar : '))
z = int(input('Introduceti al treilea numar : '))
if ( x > y and x > z ):
    print (f'{x} este cel mai mare numar. ')
elif ( y > x and y > z ):
    print (f'{y} este cel mai mare numar. ')
elif ( z > x and z > y ):
    print (f'{z} este cel mai mare numar. ')
else:
    print ('Numerele sunt egale ')
