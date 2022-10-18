# Problem 'Magnus' coci18c3p1 ***

word = input()
honi_count = 0
position = 0

for char in word:
    if position == 0:
        match = 'H'
    elif position == 1:
        match = 'O'
    elif position == 2:
        match = 'N'
    else:
        match = 'I'
    if char == match:
        position += 1
        if position == 4:
            position = 0
            honi_count += 1

print(honi_count)
