def check_word():   
    with open("sample.txt", 'r') as f:
        data = f.read()
        if (data.find("coded") != -1):
            print("found")
        else:
            print("not found")

def check_line(word):
    with open("sample.txt", 'r') as f:
        for i in range (1,5):
            data = f.readline()
            if (data.find(word) != -1):
                print(F"first occurence in line {i}")
                return
    return -1 

check_line("programming")