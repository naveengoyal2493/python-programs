def get_unique_cal(arr, cal_name="new"):
    count = 0
    local = cal_name
    while count < len(arr):
        if arr[count] == cal_name:
            cal_name = local + str(count + 1)
        count += 1
    return cal_name

arr = ["new", "new1", "new5"]
print(get_unique_cal(arr))