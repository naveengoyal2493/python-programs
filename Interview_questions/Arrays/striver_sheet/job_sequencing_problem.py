"""
Given a set of N jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the 
profit associated with job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.
Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.

Example 1:

Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).

Example 2:

Input:
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
Output:
2 127
Explanation:
2 jobs can be done with
maximum profit of 127 (100+27).
"""


class Job:
    def __init__(self, id, deadline, profit):
         self.id = id
         self.deadline = deadline
         self.profit = profit

def job_sequencing_problem(Jobs: list[Job], n):
    Jobs.sort(key = lambda x: x.profit, reverse=True)

    arr = [0] * n
    job_count = 0
    max_profit = 0
    for job in Jobs:
        index = min(job.deadline - 1, n)
        for j in range(index, -1, -1):
            if arr[j] == 0:
                max_profit += job.profit
                arr[j] = 1
                job_count += 1
                break
    
    return job_count, max_profit


jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
n = len(jobs)
job_objects = []
for job in jobs:
    job_objects.append(Job(job[0], job[1], job[2]))

print(job_sequencing_problem(job_objects, n))
