def merge_two_sorted_arrays_without_extra_space(arr1, arr2):
    i = len(arr1) - 1
    j = 0

    while(i >= 0 and j < len(arr2)):
        if arr1[i] > arr2[j]:
            temp = arr1[i]
            arr1[i] = arr2[j]
            arr2[j] = temp
        i -= 1
        j += 1
    
    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)

arr1 = [1,3,5,7]
arr2 = [4,6,10]
merge_two_sorted_arrays_without_extra_space(arr1, arr2)

    
    