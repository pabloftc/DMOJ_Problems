# Problem 'Rijeci' coci13c3p1

button = int(input())

a = 1
b = 0

for i in range(button):
    new_a = b 
    new_b = a + b 
    a = new_a 
    b = new_b 

print(a, b) 
