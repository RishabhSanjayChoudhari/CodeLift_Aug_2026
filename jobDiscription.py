AllSkills = ["python","java","cpp","html","css"]
JD = input("Enter Job Discription : ")
RequiredSkills = []
Separate = JD.split()
for i in Separate:
    i = i.lower()
    if i in AllSkills and i not in RequiredSkills:
        RequiredSkills.append(i)
print(RequiredSkills)