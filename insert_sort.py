import timeit


def sorter(self):
    for x in range(1, len(self)):

        currentval = self[x]
        position = x

        while position > 0 and self[position - 1] > currentval:
            self[position] = self[position - 1]
            position = position - 1

        self[position] = currentval
    return self

if __name__ == '__main__':

    def easy_sort():
        x = range(100)
        sorter(x)

    def hard_sort():
        x = range(100, 0, -1)
        sorter(x)

    def long_sort():
        x = range(1000)
        sorter(x)

    def long_hard_sort():
        x = range(1000, 0, -1)
        sorter(x)

    print "This is sorting a range from 1-100"
    print(timeit.Timer("easy_sort()", setup="from __main__ import easy_sort").timeit(number=100))
    print "This is sorting a range 100-1"
    print(timeit.Timer("hard_sort()", setup="from __main__ import hard_sort").timeit(number=100))
    print "This is sorting a range from 1-1000"
    print(timeit.Timer("long_sort()", setup="from __main__ import long_sort").timeit(number=100))
    print "This is sorting a range 1000-1"
    print(timeit.Timer("long_hard_sort()", setup="from __main__ import long_hard_sort").timeit(number=100))
