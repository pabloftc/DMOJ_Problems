# Problem 'A New Hope' wc15c2j1

far_index = int(input())
if far_index == 1:
    print('A long time ago in a galaxy far away...')
else:
    print('A long time ago in a galaxy ' + 'far, ' * (far_index - 1) + 'far away...')
