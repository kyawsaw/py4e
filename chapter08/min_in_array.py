list = [22, 14, 27, 55, 11]
min = list[0]
max = list[0]
for (i, item) in enumerate(list):
    if min > item:
        min = item
        min_found = i
    if max < item:
        max = item
        max_found = i
print("Max value is", max, "found at", max_found)
print("Min value is", min, "found at", min_found)
list[max_found] = min
list[min_found] = max
print(list)
