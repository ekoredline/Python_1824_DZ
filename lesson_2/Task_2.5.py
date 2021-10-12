my_list = [57.8, 46.51, 97, 55.13, 16.82, 99, 15, 33.05, 33.6, 18.1]
my_list.sort()
for i in my_list:
    rub = int(f'{i:.2f}'[:2])
    cop = int(f'{i:.2f}'[3:])
    print(f'{rub} руб {cop} коп', end=', ')

new_my_list = sorted(my_list)
print(new_my_list)