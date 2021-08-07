list = [22, 14, 27, 55, 11]
min = list[0]
fount = 0
for (i, item) in enumerate(list):
    if min > item:
        min = item
        found = i
print("Min value is", min, "found at", found)
