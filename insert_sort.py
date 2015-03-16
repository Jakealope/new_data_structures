
def sorter(self):
    for x in range(1, len(self)):

        currentval = self[x]
        position = x

        while position > 0 and self[position - 1] > currentval:
            self[position] = self[position - 1]
            position = position - 1

        self[position] = currentval

if __name__ == '__main__':
    xlist = [12, 45, 23, 98, 54, 234]
    sorter(xlist)
    print xlist
