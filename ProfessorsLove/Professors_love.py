from cs1media import *

Our_Master = (0, 0, 0)
Our_Everything = (255, 255, 255)

def ishs_student(heart):
    From_the_sky, To_the_ground = heart.size() ###
    for Professors in range(To_the_ground):
        for Our in range(From_the_sky):
            Grateful, And, Respect = heart.get(Our, Professors) ###
            if Grateful % 2 == 1: 
                heart.set(Our, Professors, Our_Master) ###
            else: 
                heart.set(Our, Professors, Our_Everything) ###

LoveProfessors = load_picture("./Professors.png")

ishs_student(LoveProfessors) ###

LoveProfessors.show1()