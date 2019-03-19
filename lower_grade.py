import unittest


def lowest_grade_students(students):
    # stundets is a sorted list of tuples (name, score) with at least 2 entries
    students.sort(key=lambda tupl: tupl[1])
    lowest_score = students[0][1]
    students = list(filter(lambda tupl: tupl[1] != lowest_score, students))
    lowest_score = students[0][1]
    students = list(filter(lambda tupl: tupl[1] == lowest_score, students))
    students.sort(key=lambda s: s[0])
    return [student[0] for student in students]


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = raw_input()
        score = float(input())
        students.append((name, score))
    for i in lowest_grade_students(students):
        print(i)
