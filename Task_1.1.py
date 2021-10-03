duration = int(input('Введите любое число: '))

min = duration // 60
hour = duration // 3600
day = duration // 86400
month = duration // (86400 * 31)
year = duration // (86400 * 31) * 12

if duration >= 60 and duration < 3600:
    print(f'{min} мин {duration % 60} сек.')

elif duration >= 3600 and duration < 86400:
    print(f'{hour} час {min % 60} мин {duration % 60} ')

elif duration >= 86400 and duration < (86400 * 31):
    print(f'{day} дн {hour % 24} час {min % 60} мин {duration % 60} сек')

elif duration >= (86400 * 31) and duration < ((86400 * 31) * 12):
    print(f'{month} мес {day % 31} дн {hour % 24} час {min % 60} мин {duration % 60} сек')

elif duration >= ((86400 * 31) * 12):
    print(f'{year} лет {month % 12} мес {day % 31} дн {hour % 24} час {min % 60} мин {duration % 60} сек')

elif duration < 60 and duration > 0:
    print(f'{duration} сек')

elif duration < 0:
    print(f'Введите положительное число.')

# duration = int(input('Введите любое число: '))

# sek = duration % 60
# min = duration // 60 % 60
# hour = duration // 3600 % 24
# day = duration // 86400 * 24

# print(f'{day} дн {hour} час {min} мин  {sek} сек')