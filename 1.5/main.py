from Student import Student


def input_students_count() -> int:
    """Ввод пользователем количества учеников."""

    while True:
        user_input = input('Количество учеников: ')

        if user_input.isdigit() and int(user_input) in range(1, 2_000):
            return int(user_input)


def input_pit_depth() -> int:
    """Ввод пользователем глубины ямы."""

    while True:
        user_input = input('Глубина ямы: ')

        if user_input.isdigit() and int(user_input) in range(1, 10**5 + 1):
            return int(user_input)


def solve(students: list[Student], pit_depth: int) -> list[Student]:
    """Возвращает список с максимальным количеством учеников, которые смогут выбраться."""

    students.sort(key=lambda x: x.height)
    get_out_list = []  # Список учеников, которые могут выбраться
    height = 0

    for student in reversed(students):
        height += student.height

        if height + student.length >= pit_depth:
            get_out_list.append(student)

    return get_out_list


def main():
    students_count = input_students_count()  # Количество учеников
    students = [Student(student_id) for student_id in range(1, students_count + 1)]  # Список с объектами учеников
    print()
    pit_depth = input_pit_depth()  # Глубина ямы

    get_out_list = solve(students, pit_depth)  # Список с максимальным количеством учеников, которые смогут выбраться

    print('\n\nВыберутся: %d' % len(get_out_list))
    if get_out_list:
        print('Номера: ', end='')

        for s in get_out_list:
            print(s.student_id, end=' ')


if __name__ == '__main__':
    main()
