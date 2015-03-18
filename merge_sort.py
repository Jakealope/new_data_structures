
def m_sort(self):
    if len(self) <= 1:
        return self

    middle = len(self) / 2
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
