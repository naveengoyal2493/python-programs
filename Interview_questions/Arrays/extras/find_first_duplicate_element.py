def find_first_duplicate(arr):
    dict = {}
    min = -1
    
    for i in range(len(arr)-1,-1,-1):
        if arr[i] in dict.keys():
            min = i
        else:
            dict[arr[i]] = 1

    if min != -1:
        return min + 1
    else:
        return min

# print(find_first_duplicate([1,2,3,4,5,6,6]))
        