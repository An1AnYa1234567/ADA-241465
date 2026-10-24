'''Write a program Implement fractional_knapsack(weights: List[int], values: List[int], capacity: int)
-> float and job_scheduling(jobs: List[Job]) -> List[int] functions returning maximum
attainable profit and optimal job sequence.'''

# Fractional Knapsack and Job Scheduling
# Fractional Knapsack
def fractional_knapsack(weights, values, capacity):
    items = sorted(
        zip(weights, values),
        key=lambda item: item[1] / item[0],
        reverse=True
    )

    total_profit = 0

    for weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_profit += value
            capacity -= weight
        else:
            total_profit += value * capacity / weight
            capacity = 0

    return total_profit
# Job Scheduling with Deadlines
def job_scheduling(jobs):
    jobs = sorted(jobs, key=lambda job: job[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * max_deadline

    for name, deadline, profit in jobs:
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = name
                break

    return [job for job in slots if job is not None]
# Main Program
print("FRACTIONAL KNAPSACK")

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

profit = fractional_knapsack(weights, values, capacity)

print("Maximum Profit:", profit)

print("\nJOB SCHEDULING")

jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15)
]

sequence = job_scheduling(jobs)

print("Job Sequence:", sequence)

total_profit = 0

for job in sequence:
    for name, deadline, profit in jobs:
        if name == job:
            total_profit += profit

print("Total Job Profit:", total_profit)
