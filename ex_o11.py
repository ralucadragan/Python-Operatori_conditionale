'''
11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
● Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
'''

import random
dice_roll = random.randint(1,6)
print (dice_roll)
nr_utiliz = int(input('Introduceti un nr : '))
if ( nr_utiliz < dice_roll):
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {nr_utiliz}, dar a fost {dice_roll} .')
elif ( nr_utiliz > dice_roll):
    print(f'Ai pierdut. Ai ales un numar mai mmare. Ai ales {nr_utiliz}, dar a fost {dice_roll} .')
else:
    print(f'Ai castigat. Felicitari !Ai ales {nr_utiliz} si zarul a fost {dice_roll} .')