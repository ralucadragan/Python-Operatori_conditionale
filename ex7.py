#7. x si y (int)
#   Verifica si afiseaza daca sunt egale, daca nu afiseaza care dintre ele este mai mare.

x = int(input('Introduceti primul nr : '))
y = int(input('Introduceti al doilea nr : '))
if ( x==y):
    print('Cele doua numere introduse sunt egale')
elif (x > y):
    print(f'Numarul introdus {x} este numarul cel mai mare.')
elif (x < y ):
    print(f'Numarul introdus {y} este numarul cel mai mare.')