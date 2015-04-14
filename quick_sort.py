import timeit
import random


def q_sort(alist):
    lower = []
    p_list = []
    higher = []

    try:
        pivot = random.choice(alist)
        for i in alist:
            if i < pivot:
                lower.append(i)
            elif i > pivot:
                higher.append(i)
            else:
                p_list.append(i)
        lower = q_sort(lower)
        higher = q_sort(higher)
        return lower + p_list + higher
    except:
            if len(alist) <= 1:
                return alist
if __name__ == '__main__':

    def hard_sort():
        x = random.sample(range(100), 100)
        q_sort(x)

    def easy_sort():
        x = range(100)
        q_sort(x)

    print("This is sorting a random range of 100")
    print(timeit.Timer("easy_sort()",
                       setup="from __main__ import easy_sort").timeit(number=1000))
    print("This is sorting a range 1-100")
    print(timeit.Timer("hard_sort()",
                       setup="from __main__ import hard_sort").timeit(number=1000))
