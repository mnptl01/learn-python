with open('sample.txt', 'r+') as f:
    data = f.read()
new_data = data.replace("python", 'java')

with open("sample.txt", 'w') as f:
    f.write(new_data)