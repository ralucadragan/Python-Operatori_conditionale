'''
6. Avand stringul: 'Coral is either the stupidest anumal or the smartest rock'
- Citeste de la tastatura un int x
- Afiseaza stringul fara ultimele x caractere
Ex: daca ai ales 7 => 'Coral is either the stupidest anumal or the smarte'
'''

text = 'Coral is either the stupidest anumal or the smartest rock'
nr = int(input('Introduceti nr dorit : '))
if ( nr == 0):
    print (text)
else:
    print (text[:- nr])