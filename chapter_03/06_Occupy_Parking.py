# Problem 'Occupy Parking' ccc18j2

n = int(input())
yesterday = input()
today = input()

occupied = 0

for i in range(0, n):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied += 1

print(occupied)
