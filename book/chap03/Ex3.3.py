int_list = [ 10, 100, 100, 20, 14, 5, 22, 60, 554, 11, 2 ]

min = 2000000
second_min = 0

for i in range(len(int_list)):
    if int_list[i] < min:
        second_min = min
        min = int_list[i]
    elif int_list[i] < second_min:
        second_min = int_list[i]

print(f'最小値: {min}, 次点: {second_min}')
        


