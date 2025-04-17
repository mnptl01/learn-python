numbers=[1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    divisor=[]
    for i in numbers:
        if i%num==0:
            divisor.append(i)
    print(f"{num}:{divisor}")


