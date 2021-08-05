try:
    loop = int(input("Enter number: "))
except:
    print("Enter positive number")
    quit()
num = 0
las_num = 1
count = 0
while count < loop:
    result = num + las_num
    num = las_num
    las_num = result
    print(num)
    count = count + 1
