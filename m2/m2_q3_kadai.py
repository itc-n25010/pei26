list_a = [2.02, 2.03, 2.04]
list_b = [2.05, 2.06, -2.07]

print(list_a[1] * list_b[-2])
print(str(list_a[4] + int(list_b[2])) + '番') # 3 + 6 = 9 <-最終的に文字列として扱われる
print(divmod(list_a[3], list_b[4])) # 14 // 7 = 2, 14 % 7 = 0

list_c = list_a + list_b
list_b += list_c

print(list_a[2 % list_b[4]])
print(min(list_b[2:6]))
print(round(list_c[0], list_b[1]))
print(max(list_c))
print(min(list_c[2:5]))