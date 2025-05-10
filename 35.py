class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def averageMarks(self):
        total = 0
        for i in self.marks:
            total += i
        print(f'the average is {total/3}')
    
s1 = Student("sahil", [33,33,33])
print(s1.name)
print(s1.marks)
s1.averageMarks()