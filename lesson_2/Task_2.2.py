my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

my_list_new = []


for i in my_list:
    if i.replace('+', '').isdigit():
        if i.isdigit():
            my_list_new.append(f'"{int(i):02}"')
        else:
            my_list_new.append(f'"{i[0]}{int(i[1]):02}"')
    else:
        my_list_new.append(i)

print(' '.join(my_list_new))