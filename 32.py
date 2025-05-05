num=0
with open("numbers.txt", 'r') as f:
    data = f.read()
    nums = data.split(",")
    for i in nums:
        if int(i) %2==0:
            num+=1
print(num)