# Problem 'English or French' ccc11s1

lines = int(input())

char_s = 0
char_t = 0
char_cap_s = 0
char_cap_t = 0

for char in range(lines):
    phrase = input()
    for i in phrase:
        if i == 's':
            char_s = char_s + 1 
        elif i == 't':
            char_t = char_t + 1 
        elif i == 'S':
            char_cap_s = char_cap_s + 1 
        elif i == 'T':
            char_cap_t = char_cap_t + 1 

french = char_s + char_cap_s
english = char_t + char_cap_t

if french >= english:
    print('French')
else:
    print('English')
