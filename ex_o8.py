'''
8. Acelasi string.
- Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
- Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
- output: 'Coral is either the stupidest animal or the smartest'
'''


text = 'Coral is either the stupidest anumal or the smartest rock'
cuvant = text.index('rock')
print (f'Indexul de start al cuvantului "rock" este {cuvant}.')
print (text[:cuvant])

