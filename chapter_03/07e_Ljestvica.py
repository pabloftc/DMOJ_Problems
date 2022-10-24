# Problem 'Ljestvica' coci12c5p1

music = input()

c_major = 0
a_minor = 0

for i in range(len(music)):
    if i == 0 or music[i - 1] == '|':
        if music[i] in 'CFG':
            c_major = c_major + 1
        if music[i] in 'ADE':
            a_minor = a_minor + 1

if c_major == a_minor:
    if music[-1] == 'C':
        c_major = c_major + 1
    else:
        a_minor = a_minor + 1

if c_major > a_minor:
    print('C-dur')
else:
    print('A-mol')