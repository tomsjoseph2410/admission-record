import pandas as pd
from operator import itemgetter, le
print("STUDENT RECORDS")
record_list = []

n = int(input("enter the number of students:            "))

for _ in range(n):
    name = input("Enter the Name of the Student:           ")
    roll_no = int(input("Enter the Roll Number of the Student:    "))

    maths_marks = int(
        input("enter the marks for MATHS out of 100:               "))
    while (maths_marks < 0 or maths_marks > 100):
        print("ERROR")
        maths_marks = int(
            input("enter the marks for MATHS out of 100:               "))

    science_marks = int(
        input("enter the marks of SCIENCE out of 100:              "))
    while (science_marks < 0 or science_marks > 100):
        print("ERROR")
        science_marks = int(
            input("enter the marks for SCIENCE out of 100:               "))

    socialScience_marks = int(
        input("enter the marks for social science out of 100:      "))
    while (socialScience_marks < 0 or socialScience_marks > 100):
        print("ERROR")
        socialScience_marks = int(
            input(
                "enter the marks for SOCIAL SCIENCE out of 100:               "
            ))

    studentRecord_dictionary = {
        "name": name,
        "roll_no": roll_no,
        "maths_marks": maths_marks,
        "science_marks": science_marks,
        "socialScience_marks": socialScience_marks
    }

    record_list.append(studentRecord_dictionary)
record_list = sorted(
    record_list,
    key=lambda i:
    (i['maths_marks'] + i["science_marks"] + i["socialScience_marks"]),
    reverse=True)

final = pd.DataFrame(record_list)
print("\n")
print("Top Performances")
print(final)
print("\n")


def particular():
    nn = int(input("enter the roll number "))
    ff = []

    for dicti in record_list:
        if (dicti["roll_no"] == nn):
            ff.append(dicti)
    ffdict = pd.DataFrame(ff)
    print(ffdict)


question = input(
    "Do you want to see details about a particular  student y/n  ")
if question == "y":
    particular()

question_delete = input("Do you want to delete any data y/n : ")
if question_delete == "y":
    delete_number = int(input("Enter the Roll Number You want to delete "))
    for dicti in record_list:
        if (dicti["roll_no"] == delete_number):
            record_list.remove(dicti)
    final = pd.DataFrame(record_list)
    print(final)
    print("\n")
    print("Data Removed")
else:
    print("Thank You")
