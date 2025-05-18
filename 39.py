class Numbers:
    def __init__(self, real, img):
        self.real = real
        self.img = img 
    
    def show(self):
        print(f"{self.real}i + {self.img}j")

    def __add__(self, num2):
        nm1 = self.real + num2.real
        nm2 = self.img + num2.img
        return Numbers(nm1, nm2)

num1 = Numbers(1,2)
num1.show()
num2 = Numbers(3,4)
num2.show()
(num1+num2).show()

