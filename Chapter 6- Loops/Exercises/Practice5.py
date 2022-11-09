student_name = "Afra"
marks = {"James" : 90 , "Chris" : 55 , "Evelyn" : 77}
for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print("No entry name found")
