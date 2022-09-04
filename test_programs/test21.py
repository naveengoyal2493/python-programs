from cmath import pi


def quick_sort(elements):
    pivot = elements[0]
    start = None
    end = None

    for i in range(1, len(elements)):
        start = elements[i]
        if pivot < start:
            break
    for j in range(len(elements)-1,-1,-1):
        end = elements[j]
        if pivot > end:
            break
    temp = start
    start = end
    end = temp

    

elements = [11,9,29,7,2,15,28]
quick_sort(elements)