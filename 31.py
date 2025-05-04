with open("sample.txt", 'r') as f:
    data = f.read()
    if (data.find("coded") != -1):
        print("found")
    else:
        print("not found")
