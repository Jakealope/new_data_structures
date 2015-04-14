import timeit


def m_sort(self):
    if len(self) <= 1:
        return self

    middle = len(self) // 2
    left = self[:middle]
    right = self[middle:]

    left = m_sort(left)
    right = m_sort(right)
    return list(merger(left, right))


def merger(left, right):
    final = []
    l_index, r_index = 0, 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            final.append(left[l_index])
            l_index += 1
        else:
            final.append(right[r_index])
            r_index += 1

    if left:
        final.extend(left[l_index:])
    if right:
        final.extend(right[r_index:])
    return final


if __name__ == '__main__':

    def easy_sort():
        x = range(100)
        m_sort(x)

    def hard_sort():
        x = range(100, 0, -1)
        m_sort(x)

    def long_sort():
        x = range(1000)
        m_sort(x)

    def long_hard_sort():
        x = range(1000, 0, -1)
        m_sort(x)

    print("This is sorting a range from 1-100")
    print(timeit.Timer("easy_sort()",
                       setup="from __main__ import easy_sort").timeit(number=1000))
    print("This is sorting a range 100-1")
    print(timeit.Timer("hard_sort()",
                       setup="from __main__ import hard_sort").timeit(number=1000))
    print("This is sorting a range from 1-1000")
    print(timeit.Timer("long_sort()",
                       setup="from __main__ import long_sort").timeit(number=1000))
    print("This is sorting a range 1000-1")
    print(timeit.Timer("long_hard_sort()",
                       setup="from __main__ import long_hard_sort").timeit(number=1000))
