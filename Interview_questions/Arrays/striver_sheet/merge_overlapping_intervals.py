input = [[1,3],[5,10],[6,7], [2,5]]

def merge_overlapping_sub_intervals(intervals):
    intervals.sort(key= lambda i: i[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = output[-1][1]
        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start, end])
    return output

print(merge_overlapping_sub_intervals(input))
            
    