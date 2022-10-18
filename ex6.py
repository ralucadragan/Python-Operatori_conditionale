# 6. Verifica daca x nu este intre 5 si 27 - a se folosi 'not,

nr = int(input('Introduceti nr dorit: '))
if not (nr > 5 and nr < 27):
    print ('Nr introdus este inafara intervalului dorit. Reintroduceti alt nr!')
else:
    print ('Nr introdus este in intervalul dorit!')