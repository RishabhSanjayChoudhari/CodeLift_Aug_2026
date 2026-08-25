Skills = ["python","cpp","html","css"]
RequiredSkills = ["python","java","cpp"]
Gap = []

for i in RequiredSkills:
    if i in Skills:
        continue
    else:
        Gap.append(i)
print(Gap)
