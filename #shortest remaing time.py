
# Shortest Remaining Time First

n = int(input("Enter the number of processes: "))
pid = []
at = []
bt = []

wt = [0] * n
tat = [0] * n
ct = [0] * n
rt = []

# Input
for i in range(n):
    pid.append(i + 1)
    at.append(int(input(f"Enter arrival time for process {i + 1}: ")))
    bt.append(int(input(f"Enter burst time for process {i + 1}: ")))
    rt.append(bt[i])

current_time = 0
completed = 0

while completed < n:
    idx = -1
    minimum = 9999

    for i in range(n):
        if at[i] <= current_time and rt[i] > 0:
            if rt[i] < minimum:
                minimum = rt[i]
                idx = i
            elif rt[i] == minimum:
                if idx == -1 or at[i] < at[idx]:
                    idx = i

    if idx != -1:
        rt[idx] -= 1
        current_time += 1

        if rt[idx] == 0:
            completed += 1
            ct[idx] = current_time
            tat[idx] = ct[idx] - at[idx]
            wt[idx] = tat[idx] - bt[idx]

    else:
        current_time += 1

# Average WT and TAT
avg_tat = sum(tat) / n
avg_wt = sum(wt) / n

# Output
print("\nProcess ID\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(f"{pid[i]}\t\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

print("\nAverage Turnaround Time:", round(avg_tat, 2))
print("Average Waiting Time:", round(avg_wt, 2))
