# Problem 'Winning Score' ccc19j1

ap3 = int(input()) * 3
ap2 = int(input()) * 2
ap1 = int(input())
ba3 = int(input()) * 3
ba2 = int(input()) * 2
ba1 = int(input())

ap = ap3 + ap2 + ap1
ba = ba3 + ba2 + ba1

if ap > ba:
    print('A')
elif ap < ba:
    print('B')
else:
    print('T')