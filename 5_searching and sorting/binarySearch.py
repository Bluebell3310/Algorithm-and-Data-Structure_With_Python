def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

testlist = [0, 1, 2, 3, 6, 14, 15, 18, 20]
print(binarySearch(testlist, 5))
print(binarySearch(testlist, 15))