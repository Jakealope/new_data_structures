

def sort_radix(alist):
    length = len(alist)
    total = 10
    bucket = 1
    while True:
        new_list = [[] for i in range(total)]
        for value in alist:
            smallest_val = value % total
            smallest_val /= bucket
            new_list[smallest_val].append(value)
        total = total * 10
        bucket = bucket * 10
    if len(new_list[0]) == length:
        return new_list[0]

    rand_list = []
    rand_list_append = rand_list.append
    for x in new_list:
        for y in x:
            rand_list_append(y)
