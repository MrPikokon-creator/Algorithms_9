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

    get_out_list = []  # Список учеников, которые могут выбраться
    for top_student in students:
        max_height = 0
        temp_list = []

        for student in students:
            if student is top_student:
                continue

            if max_height + student.height >= pit_depth:
                temp_list.append(student)

            max_height += student.height

        if temp_list or max_height + top_student.height + top_student.length >= pit_depth:
            temp_list.append(top_student)

        if len(temp_list) > len(get_out_list):
            get_out_list = temp_list.copy()

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
