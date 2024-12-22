arr = [1, 2, 3, 4]
ha = {}
for num in arr:
    ha[num] = ha.get(num, 0) + 1


print(ha)
