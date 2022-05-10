class Student:
    def __init__(self, student_id: int):
        assert isinstance(student_id, int), 'неверный номер студента'
        self.student_id = student_id  # Номер ученика
        print('\n%d ученик' % student_id)

        while True:
            try:
                user_input = input('Рост и длина рук (через пробел): ')
                splitted_user_input = user_input.split(' ')
                assert len(splitted_user_input) == 2, 'неверный формат ввода'

                self.height = splitted_user_input[0]
                self.length = splitted_user_input[1]
                return
            except AssertionError as error:
                print(error)
                continue

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height: str):
        assert height.isdigit() and int(height) in range(1, 10**5 + 1), 'неверный рост'
        self._height = int(height)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length: str):
        assert length.isdigit() and int(length) in range(1, 10**5 + 1), 'неверная длина рук'
        self._length = int(length)
