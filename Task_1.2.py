my_list = []
all_sum = 0
all_sum_17 = 0
my_list_17 = []

for i in range(1, 1000, 2):
    my_list.append(i**3)

for ind, val in enumerate(my_list):
    sum = 0
    while val > 0:
        sum += val % 10
        val //= 10
    if sum % 7 == 0:
        all_sum += my_list[ind]

print(all_sum)


for i in range(len(my_list)):
    my_list[i] += 17

for ind, val in enumerate(my_list):
    sum = 0
    while val > 0:
        sum += val % 10
        val //= 10
    if sum % 7 == 0:
        all_sum_17 += my_list[ind]

print(all_sum_17)
