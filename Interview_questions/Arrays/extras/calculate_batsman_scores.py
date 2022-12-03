
def calculate_score(runs):
    striker = ["batsman1", 0]
    non_striker = ["batsman2", 0]
    for i in range(len(runs)):
        if runs[i] % 2 == 0:
            striker[1] += runs[i]
        else:
            striker[1] += runs[i]
            temp = striker
            striker = non_striker
            non_striker = temp

        if (i + 1) % 6 == 0:
            temp = striker
            striker = non_striker
            non_striker = temp
        

    return (striker, non_striker)

runs = [1, 2, 4, 1, 3, 1, 1, 4, 6, 0, 0, 1, 1, 1, 2, 1, 0, 6, 0, 0, 1, 2, 1, 0, 0, 4, 0, 1, 0]
print(calculate_score(runs))