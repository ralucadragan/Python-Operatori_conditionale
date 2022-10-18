'''
10. Transforma si printeaza notele din sistemul romanesc in:
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub 4 = F
'''

nota = float(input('Introduceti nota pentru modificare : '))
if (nota >=9 and nota <=10):
    nota = 'A'
    print (f'Nota obtinuta este {nota} . ')
elif (nota >= 8 and nota <=10):
    nota = 'B'
    print(f'Nota obtinuta este {nota} . ')
elif (nota >= 7 and nota <=10):
    nota = 'C'
    print(f'Nota obtinuta este {nota} . ')
elif (nota >= 6 and nota <=10):
    nota = 'D'
    print(f'Nota obtinuta este {nota} . ')
elif (nota >= 4 and nota <=10):
    nota = 'E'
    print(f'Nota obtinuta este {nota} . ')
elif (nota <= 4 and nota >= 0 ):
    nota = 'F'
    print(f'Nota obtinuta este {nota} . ')
else:
    print ('Nota introdusa este inafara sistemului de notare. Reintroduceti alta nota !')