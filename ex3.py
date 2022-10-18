# 3. Verifica si afiseaza daca x este un nr pozitiv, negativ sau neutru

nr = int(input('Introduceti nr dorit: '))
if (nr < 0):
    print ('Nr introdus este un nr. negativ!')
elif (nr > 0):
    print ('Nr introdus este un nr pozitiv!')
else:
    print ('Nr introdus este un nr neutru!')