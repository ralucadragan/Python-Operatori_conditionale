# 1. Verifica daca X are minim 4 cifre (X este int).
# ex: 7895 are 4 cifre, 10 nu mai are min 4 cifre

x = int(input('Introduceti numarul dorit : '))
if ( x >= 1000 and x < 10000 ) :
    print (f'Numarul introdus are 4 cifre !')
elif ( x >= 0 and x < 1000):
    print (f'Nr introdus are mai putin de 4 cifre !')
else :
    print (f'Numarul introdus are mau mult de 4 cifre !')