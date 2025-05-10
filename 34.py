rooster = {
    "Name" : "Group"

}
list=[
    "Liam Foster", "Emma Hayes", "Noah Grant", "Olivia Rivera", "Elijah Brooks",
    "Ava Chapman", "James Holloway", "Isabella Reeves", "Lucas Barrett", "Mia Erickson",
    "Benjamin Wu", "Charlotte Bass", "Henry Chandler", "Amelia Yates", "Sebastian Wolfe",
    "Harper Lloyd", "Ethan Glass", "Sofia Davidson", "Jack Frye", "Chloe Nixon"
]


# class StudentDistribution:

#     def __init__(self, fullName, groupNumber):
#         self.name = fullName
#         self.group = groupNumber


for i in range(0, 20):
    group = int(input(F"Enter the group numer of roll {i}: "))
    rooster[list[i]]=group
    
print(rooster)
