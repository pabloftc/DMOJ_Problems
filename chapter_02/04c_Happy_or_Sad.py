# Problem 'Happy or Sad' ccc15j2

phrase = input()

happy = phrase.count(':-)')
sad = phrase.count(':-(')

if happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
else:
    print('sad')