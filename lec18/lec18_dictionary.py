majors = {
    "CS": "Computer Science", 
    "EE": "Electrical Engineering", 
    "MAS": "Mathematical Sciences", 
    "ME": "Mechanical Engineering"
}

d1 = dict() # an empty dictionary
d2 = {} # an empty dictionary

majors["PH"] = "Physic"
print(majors["PH"])

majors["PH"] = "Physics"
print(majors["PH"])

majors[0]=0.001
print(majors)

print(len(majors) )
del majors[0]
print(majors)
print(len(majors))
print("CS" in majors)
print("AI" in majors)

print(majors.keys())
print(majors.values())
print(majors.items())

for key in majors:
    print("%s is %s." % (key, majors[key]))

for key, value in majors.items():
    print("%s is %s." % (key, value))