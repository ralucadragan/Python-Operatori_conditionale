'''
1. Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
'''

text = input ('Introduceti cuvantul dorit : ')
prima_litera = text[0]
ultima_litera = text[-1]
print (f'Prima litera este a cuvantului introdus este : {prima_litera} ')
print (f'Ultima litera este a cuvantului introdus este : {ultima_litera}')
assert prima_litera.lower() == ultima_litera.lower()
print (f'Prima si ultima litera a cuvantului introdus sunt identice : {prima_litera} si {ultima_litera} ')

# if prima_litera.lower() == ultima_litera.lower() :
#     print(f'Prima si ultima litera a cuvantului introdus sunt identice : {prima_litera} si {ultima_litera} ')
# else:
#     print (f'Prima si ultima litera a cuvantului introdus nu sunt identice.')
