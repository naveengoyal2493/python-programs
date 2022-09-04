def binary_search(elements, val):
    first = 0
    last = len(elements)
    return support(elements, val, first, last)

def support(elements, val, first, last):
    if last < first:
        return -1
    middle = (first + last) // 2
    if middle >= len(elements)-1 or middle < 0:
        return -1
    if elements[middle] == val:
        return middle
    if elements[middle] < val:
        first = middle
    if elements[middle] > val:
        last = middle

    return support(elements, val, first, last)

def find_occurances(elements, val):
    middle = binary_search(elements, val)
    occurances = [middle]
    middle_backwards = middle - 1
    middle_forwards = middle + 1
    while elements[middle_backwards] == val:
        if middle_backwards not in occurances:
            occurances.append(middle_backwards)
        middle_backwards -= 1
    while elements[middle_forwards] == val:
        if middle_forwards not in occurances:
            occurances.append(middle_forwards)
        middle_forwards += 1
    
    return occurances

def binary_search_with_while(elements, val):
    first = 0
    last = len(elements) - 1
    middle = 0

    while first <= last:
        middle = (first + last) // 2
        if elements[middle] == val:
            return middle
        elif elements[middle] < val:
            first = middle + 1
        else:
            last = middle - 1

    return -1

elements = [1,3,5,7,9,11,11,11,11,11,13,15,17,19]
# print(binary_search(elements, 11))
print(find_occurances(elements, 3))