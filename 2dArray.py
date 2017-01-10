# this algorthm will return the index of a 2D array


def array_index(arr, row, col, num_elements):
    return row * num_elements + col

if __name__ == '__main__':
    arr = [[1, 2], [3, 4], [12, 6], [7, 8], [9, 10]]
    print(array_index(arr, 2, 1, 2))
