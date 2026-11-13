list_a = [4,8,3,7,9]
list_b = [10,3,6,7,2]
list_c = []
i = 0
while i < 5:
    if list_a[i] > list_b[i]:
        list_c.append(list_a[i] - list_b[i] ** 2)
    elif list_a[i] == list_b[i]:
            list_c.append(list_a[i] * 2 % 4)
    else:
        list_c.append((list_b[i] - list_a[i]) // 2)
    i += 1
print(list_c)
print(max(list_c))

"""
list_a = [4,8,3,7,9]
list_b = [10,3,6,7,2]
4と10: 4 < 10なので、(10 - 4) // 2 = 3
8と3:  8 > 3なので、8 - 3 ** 2 = -1
3と6:  3 < 6なので、(6 - 3) // 2 = 1
7と7:  7 == 7なので、(7 * 2) % 4 = 2
9と2:  9 > 2なので、9 - 2 ** 2 = 5
list_c = [3, -1, 1, 2, 5]
max(list_c) = 5
"""