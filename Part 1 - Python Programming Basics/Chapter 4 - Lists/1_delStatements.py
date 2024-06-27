
pokeTeam = ['Charizard', 'Vileplume', 'Vaporeon', 'Pidgeot', 'Raichu', 'Hypno']

pokeTeam2 = pokeTeam + ['Pikachu']

print(pokeTeam)

del pokeTeam[3] # Pidgeot 
print(pokeTeam)

del pokeTeam[3] # now position 3 is Raichu 
print(pokeTeam)

del pokeTeam[1] # Vileplume
print(pokeTeam)

del pokeTeam[-1] #  Hypno
print(pokeTeam)

print()

print(pokeTeam2)

del pokeTeam2[1:-1] # the values in indexes: 1, 2, 3, ... -1 (the last item)
print(pokeTeam2) 