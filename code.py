AllSkills = ["python","java","cpp","html","css"]
Skills = []
while True:
    Skill = input("Enter Skill or END : ")
    if Skill == "END" :
        break
    elif Skill.lower() in AllSkills :
        Skills.append(Skill)
    else:
        print("Invalid SKill")
        print("Valid Skills : ",AllSkills)
print(Skills)


