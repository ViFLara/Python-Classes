import shutil


def write_file(text):
    file = open('test.txt', 'w')
    file.write(text)
    file.close()


def update_file(name_file, text):
    file = open(name_file, 'a')
    file.write(text)
    file.close()


def read_file(name_file):
    file = open(name_file, 'r')
    text = file.read()
    print(text)


def average_grades(name_file):
    file = open(name_file, 'r')
    student_grade = file.read()
    # print(student_grade)
    student_grade = student_grade.split('\n')
    # print(student_grade)
    list_average = []
    for x in student_grade:
        list_grades = x.split(',')
        student = list_grades[0]
        list_grades.pop(0)
        print(student)
        print(list_grades)
        average = lambda grades: sum([int(i) for i in grades]) / 4
        list_average.append({student: average(list_grades)})
    return list_average
    # print(average(list_grades))


def copy_file(name_file):
    shutil.copy(name_file, '/home/viviane/PycharmProjects')


def move_file(name_file):
    shutil.move(name_file, '/home/viviane/PycharmProjects')


if __name__ == '__main__':
    move_file('grades.txt')
    copy_file('grades.txt')
    # list_average = average_grades('grades.txt')
    # print(list_average)
    # write_file('First line.\n')
    # student = 'Areta, 10, 9, 7, 6\n'
    # update_file('grades.txt', student)
    # read_file('test.txt')
