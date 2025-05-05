with open('sample.txt', 'r+') as f:
    data = f.read()
new_data = data.replace('java', "python")

with open("sample.txt", 'w') as f:
    f.write(new_data)