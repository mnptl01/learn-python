numbers = [10, 20, 30, 40, 50]
output = []
i = 0
sum = 0
while (i < len(numbers)):
    sum += numbers[i]
    output.insert(i, sum)
    i += 1
    print(output)
