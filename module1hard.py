def average(*args): return([sum(x) / len(x) for x in args])
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
print (average(*grades))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=sorted(students)
print(students)
students_and_grades={}
for i in range(0, len(students)):
    students_and_grades[students[i]]=average(*grades)[i]
    print(students_and_grades)




