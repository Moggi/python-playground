

def insertion_sort(n, lista):
    if n <= 1:
        return lista, []
    steps = []
    unsorted_number = lista[-1]
    i = n - 2

    while lista[i] > unsorted_number and i >= 0:
        lista[i+1] = lista[i]
        steps += [' '.join(map(str, lista))]
        i -= 1

    lista[i+1] = unsorted_number
    steps += [' '.join(map(str, lista))]
    return lista, steps


def gradual_insertion_sort(n, lista):
    steps = []
    for i in range(2, n+1):
        l, _ = insertion_sort(i, lista[:i])
        lista = l + lista[i:]
        steps += [' '.join(map(str, lista))]

    return lista, steps


if __name__ == "__main__":
    tests = [
        (
            [8, 7, 6, 5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5, 6, 7, 8],
            ['7 8 6 5 4 3 2 1', '6 7 8 5 4 3 2 1', '5 6 7 8 4 3 2 1',
                '4 5 6 7 8 3 2 1', '3 4 5 6 7 8 2 1', '2 3 4 5 6 7 8 1',
                '1 2 3 4 5 6 7 8']
        ),
        (
            [1, 4, 3, 5, 6, 2],
            [1, 2, 3, 4, 5, 6],
            ['1 4 3 5 6 2', '1 3 4 5 6 2', '1 3 4 5 6 2', '1 3 4 5 6 2',
                '1 2 3 4 5 6']
        ),
    ]

    for i in tests:
        lista, steps = gradual_insertion_sort(len(i[0]), i[0])
        # for i in steps:
        #     print(i)
        assert lista == i[1]
        assert steps == i[2]
