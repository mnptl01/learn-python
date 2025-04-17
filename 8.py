primeNum = [2, 5, 7, 11, 13, 17]
oddNum = [1, 3, 5, 7, 9, 11, 13, 15, 17]

common = []

for num in primeNum:
    if num in oddNum:
        common.append(num)

print(common)


a = [2, 4, 6, 8, 10, 12]
b = [3, 6, 9, 12, 15, 18]

cmn = []

for num in a:
    if num in b:
        if num % 3 == 0:
            cmn.append(num)

print(cmn)
