# 2. Verifica daca X are exact 6 cifre


x = int(input('Introduceti numarul dorit : '))
if ( x >= 100000 and x < 1000000 ) :
    print (f'Numarul introdus are 6 cifre !')
else:
    print (f'Nr introdus nu are 6 cifre !')

