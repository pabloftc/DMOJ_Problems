# Problem 'Canadian Calorie Counting' ccc06j1

burger = [461, 431, 420, 0]
side = [100, 57, 70, 0]
drink = [130, 160, 118, 0]
dessert = [167, 266, 75, 0]

bu = int(input())
si = int(input())
dr = int(input())
de = int(input())

cal = str(burger[bu - 1] + side[si - 1] + drink[dr - 1] + dessert[de - 1])

print('Your total Calorie count is ' + cal + '.')
