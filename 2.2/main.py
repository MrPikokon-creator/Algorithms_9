def get_input() -> dict:
    """Извлечение входных данных из файла input.txt."""

    with open('input.txt', 'r') as read_file:
        file = read_file.readlines()

    N = file[0].split(' ')[0].strip()  # Количество групп
    assert N.isdigit() and 1 <= int(N) <= 1_000, 'некорректное количество групп'
    N = int(N)

    M = file[0].split(' ')[1].strip()  # Количество аудиторий
    assert M.isdigit() and 1 <= int(M) <= N <= 1_000, 'некорректное количество аудиторий'
    M = int(M)

    counter = 1
    X = []
    for x in file[1]:
        if x.isdigit() and 1 <= int(x) <= 1_000:
            X.append({'count': int(x) + 1, 'index': counter})
            counter += 1
    assert len(X) == N, 'некорректный список с количеством студентов'

    counter = 1
    Y = []
    for y in file[2]:
        if y.isdigit() and 1 <= int(y) <= 1_000:
            Y.append({'count': int(y), 'index': counter})
            counter += 1
    assert len(Y) == M, 'некорректный список с количеством мест в аудиториях'

    return {'X': X, 'Y': Y}


def main():
    try:
        input_data = get_input()
    except AssertionError as error:
        print(error)
        return

    X = input_data['X']
    Y = input_data['Y']

    X.sort(key=lambda x: x['count'])
    Y.sort(key=lambda y: y['count'])

    i = 0
    while i < len(X):
        j = i
        while j < len(Y):
            if X[i]['count'] <= Y[j]['count']:
                X[i]['auditory'] = Y[j]
                break
            else:
                j += 1
        i += 1

    count = len([x for x in X if x.get('auditory') is not None])  # Количество групп, которым хватит аудиторий
    print(count)

    # Раскомментируйте для удобного вывода
    # print(f'Аудиторий хватит на {count} групп')
    #
    # print('\nРаспределение по количеству')
    # for x in X:
    #     print(x['count'] - 1, end='\t')
    #
    # print()
    # for x in X:
    #     if 'auditory' in x:
    #         print(x['auditory']['count'], end='\t')
    #     else:
    #         print(0, end='\t')
    #
    # print('\n\nРаспределение по номерам')
    # for x in X:
    #     print(x['index'], end='\t')
    #
    # print()
    for x in X:
        if 'auditory' in x:
            print(x['auditory']['index'], end='\t')
        else:
            print(0, end='\t')


if __name__ == '__main__':
    main()
