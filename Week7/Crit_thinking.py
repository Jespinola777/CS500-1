course_room = {
    "CSC101": 3005,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411,
}

course_intructor = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

course_time = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.", 
}

course = input("What course do you need information for?")

if course_room.get(course) is None:
    print(f"The course {course} does not exist, please enter a valid class.")
else:
    print(f"Your class room rumber is {course_room.get(course)} with Professor {course_intructor.get(course)}, starting at {course_time.get(course)}")