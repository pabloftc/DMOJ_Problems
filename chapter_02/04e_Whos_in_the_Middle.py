# Problem 'Who's in the Middle?' ccc07j1

bowl_1 = int(input())
bowl_2 = int(input())
bowl_3 = int(input())

arr = []

arr.append(bowl_1)
arr.append(bowl_2)
arr.append(bowl_3)

arr.sort()

print(arr[1])