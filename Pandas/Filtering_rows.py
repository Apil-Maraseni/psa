import pandas as pd

# D&D characters data
characters_data = {
  'name': ['Thorne', 'Elira', 'Glim', 'Brug', 'Nyx', 'Kael', 'Mira', 'Drogan', 'Zara', 'Fenwick'],
  'race': ['Elf', 'Human', 'Gnome', 'Half-Orc', 'Tiefling', 'Dragonborn', 'Halfling', 'Dwarf', 'Aasimar', 'Goblin'],
  'class': ['Ranger', 'Cleric', 'Wizard', 'Barbarian', 'Rogue', 'Paladin', 'Bard', 'Fighter', 'Sorcerer', 'Warlock'],
  'level': [5, 3, 4, 2, 6, 7, 3, 5, 4, 2],
  'hp': [42, 28, 33, 25, 48, 56, 30, 44, 36, 24],
  'alignment': [
    'Chaotic Good', 'Lawful Good', 'Neutral', 'Chaotic Neutral', 'Chaotic Evil',
    'Lawful Neutral', 'Neutral Good', 'Neutral', 'Chaotic Good', 'Lawful Evil'
  ]
}

# Create the DataFrame
characters = pd.DataFrame(characters_data)

print(characters)

#high_level that contains all characters that are above level 5.

high_level = characters[characters['level']>5]
print(high_level)

# halfling_bards that contains all characters whose race is 'Halfling' AND whose class is 'Bard'.
halfing_bards = characters[
    (characters['race'] == 'Halfing') &
    (characters['class'] == 'Bard')
]
print(halfing_bards)

#magic_users that contains all characters whose class is Wizard OR Sorcerer OR Warlock.
magic_users = characters[
    (characters['class'] == 'Wizard')|
    (characters['class'] == 'Sorcerrer') | 
    (characters['class']=='Warlock')
]

print(magic_users)