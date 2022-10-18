'''
2. Având stringul '0123456789'
- Afișează doar numerele pare
- Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
'''

text = ('0123456789')
print(f'Numerele pare sunt: {text[0:10:2]}')
print(f'Numerele impare sunt: {text[1:10:2]}')