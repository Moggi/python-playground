

def insertion_sort(lista):
    steps = []
    unsorted_number = lista[-1]
    i = len(lista) - 2

    while lista[i] > unsorted_number and i >= 0:
        lista[i+1] = lista[i]
        steps += [' '.join(map(str, lista))]
        i -= 1

    lista[i+1] = unsorted_number
    steps += [' '.join(map(str, lista))]
    return lista, steps


if __name__ == "__main__":
    tests = [
        (
            [2, 3, 4, 1],
            [1, 2, 3, 4],
            ['2 3 4 4', '2 3 3 4', '2 2 3 4', '1 2 3 4']
        ),
        (
            [1, 3, 4, 2],
            [1, 2, 3, 4],
            ['1 3 4 4', '1 3 3 4', '1 2 3 4']
        ),
        (
            [2, 4, 6, 8, 3],
            [2, 3, 4, 6, 8],
            ['2 4 6 8 8', '2 4 6 6 8', '2 4 4 6 8', '2 3 4 6 8']
        ),
    ]

    for i in tests:
        lista, steps = insertion_sort(i[0])
        # for i in steps:
        #     print(i)
        assert lista == i[1]
        assert steps == i[2]
