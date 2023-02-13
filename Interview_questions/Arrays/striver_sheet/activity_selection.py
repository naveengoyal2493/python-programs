def activity_selection(start, end, n):
    activities = []

    for i in range(n):
        activities.append((start[i], end[i], i))

    activities.sort(key = lambda x: x[1])
    res = [1]
    act_end = activities[0][1]
    for i in range(1, n):
        if act_end < activities[i][0]:
            res.append(activities[i][2] + 1)
            act_end = activities[i][1]

    return len(res)

n = 6
start= [1,3,0,5,8,5]
end =  [2,4,5,7,9,9]

print(activity_selection(start, end, n))
