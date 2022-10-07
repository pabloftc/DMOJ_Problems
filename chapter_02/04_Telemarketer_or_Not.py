# Problem 'Telemarketer or Not' ccc18j1

dig_1 = int(input())
dig_2 = int(input())
dig_3 = int(input())
dig_4 = int(input())

if ((dig_1 == 8 or dig_1 == 9) and (dig_4 == 8 or dig_4 == 9) and (dig_2 == dig_3)):
    print('ignore')
else:
    print('answer')