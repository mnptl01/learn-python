vowels = ['a', 'e', 'i', 'o', 'u']
words=['apple', 'banana','orange']
count=[]

for alph in words:
    vowelCounter=0
    for x in words:
        if x.lower() in words:
            vowelCounter+=1
    count.append(vowelCounter)
print(count)