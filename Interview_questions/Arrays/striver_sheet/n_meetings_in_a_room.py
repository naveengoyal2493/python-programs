# Greedy Algorithm
def n_meetings_in_a_room(start_list, end_list):
    meetings = []
    correct = []
    for i in range(len(start_list)):
        meetings.append((start_list[i], end_list[i], i + 1))

    meetings.sort(key = lambda i: i[1])
    correct.append(meetings[0][2])
    prev_end = meetings[0][1]

    for j in range(1, len(meetings)):
        next_start = meetings[j][0]
        if prev_end < next_start:
            correct.append(meetings[j][2])
            prev_end = meetings[j][1]
        
    return len(correct)

start_list = [1,3,0,5,8,5]
end_list = [2,4,6,7,9,9]
print(n_meetings_in_a_room(start_list, end_list))
