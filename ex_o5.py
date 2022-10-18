# 5. x,y,x - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu.

x = int(input('Introduceti primul unghi : '))
y = int(input('Introduceti al doilea unghi : '))
z = int(input('Introduceti al treilea unghi : '))
if ( (x + y + z) == 180 ):
    print ('Suna unghiurilor este de 180gr, deci triunghiul este valid !')
else:
    print ('Triunghiul este invalid !')