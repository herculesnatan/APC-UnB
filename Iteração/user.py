# Make an empty list for stroring aliens
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}

    aliens.append(new_alien)
for alien in aliens[0:3]:
   
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)

print('...')

# Show how many aliens have been created.

print(f"Total number of aliens: {str(len(aliens))}.")
