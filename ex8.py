#8. x,y,z sunt laturile unui triunghi
#   Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.

x = int(input('Introduceti prima latura : '))
y = int(input('Introduceti a doua latura : '))
z = int(input('Introduceti a treia latura : '))
if ( x == y == z ):
    print ('Triunghiul este echilateral. ')
elif ( x == y or x == z or y == z ):
    print ('Triunghiul  este isoscel. ')
else:
    print ('Triunghiul este oarecare. ')