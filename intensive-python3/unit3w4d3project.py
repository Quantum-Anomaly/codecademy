#!/usr/bin/env python3
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]
subjects.append('computer science')
grades.append(100)
gradebook = zip(subjects,grades)
current_gradebook = list(gradebook)
subjects.append('visual arts')
grades.append(93)
print("Current coursework: "'\n' + str(current_gradebook))
print('\n')
print("Last years coursework:"'\n' +  str(list(last_semester_gradebook)))
print('\n')
full_gradebook = [str(list(last_semester_gradebook)) + str(list(current_gradebook))]
list_full_gradebook = list(full_gradebook)
print("All years coursework: "'\n' + str(list_full_gradebook))
