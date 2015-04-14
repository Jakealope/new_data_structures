import timeit
import random


def r_sort(alist, base=10):

    def list_to_buckets(alist, base, iteration):
        buckets = [[] for i in range(base)]
        for number in alist:
            digit = (number // (base ** iteration)) % base
            buckets[digit].append(number)
        return buckets

    def buckets_to_list(buckets):
        alist = []
        for bucket in buckets:
            alist.extend(bucket)
        return alist

    max_val = max(alist)

    it = 0

    while ((base ** it) <= max_val):
        alist = buckets_to_list(list_to_buckets(alist, base, it))
        it += 1

    return alist


def string_radix(arr, base=128):
    try:
        longest = find_longest_string(arr)
    except IndexError:
        return arr

    index_num = 0
    index_place = (longest - 1)
    buckets = [[] for x in range(base)]

    while index_place >= 0:
        for val in arr:
            try:
                index_num = ord(val[index_place])
            except IndexError:
                index_num = 0
            buckets[index_num].append(val)

        transfer_list = []
        for bucket in buckets:
            for i in range(len(bucket)):
                transfer_list.append(bucket.pop(0))
        arr = transfer_list
        index_place -= 1
    return arr


def find_longest_string(arr):
    longest = max(map(len, arr))
    return longest


if __name__ == '__main__':

    def easy_sort():
        x = range(1000)
        r_sort(x)

    def hard_sort():
        x = random.sample(range(1000), 1000)
        r_sort(x)

    print "This is sorting a range of 1000"
    print(timeit.Timer("easy_sort()",
          setup="from __main__ import easy_sort")
          .timeit(number=1000))
    print "This is sorting a random range 1-1000"
    print(timeit.Timer("hard_sort()",
          setup="from __main__ import hard_sort")
          .timeit(number=1000))
