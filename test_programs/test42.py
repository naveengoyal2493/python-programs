input = ["new", "new1", "new1", "new1", "new3", "new4"]
count = 0
calendar_count = 0
prefix = "new"
calendar_name = prefix

while count < len(input):
    if input[count] == calendar_name:
        calendar_count += 1
        calendar_name = prefix + str(calendar_count)
    elif input[count] > calendar_name:
        break
    count += 1

print(calendar_name)