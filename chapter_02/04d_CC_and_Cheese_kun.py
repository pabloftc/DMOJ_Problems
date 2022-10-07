# Problem 'C.C. and Cheese-kun' dmopc16c1p0

width = int(input())
cheese = int(input())

sat = ''
if width >= 3 and cheese >= 95:
    sat = 'absolutely '
elif width == 1 and cheese <= 50:
    sat = 'fairly '
else:
    sat = 'very '
    
    
print('C.C. is ' + sat +  'satisfied with her pizza.')
