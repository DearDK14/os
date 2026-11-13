# Non-Preemptive SJF Scheduling

n = int(input("Enter the number of processes: "))

pid = []
at = []
bt = []
ct = [0] * n
wt = [0] * n
tat = [0] * n
completed = [False] * n

# Input
for i in range(n):
    print("\nProcess", i + 1)
    pid.append(input("Enter Process ID: "))
    at.append(int(input("Enter Arrival Time: ")))
    bt.append(int(input("Enter Burst Time: ")))

current_time = 0
count = 0

while count < n:

    idx = -1
    minimum = 9999

    # Find process with minimum burst time
    for i in range(n):
        if at[i] <= current_time and completed[i] == False:
            if bt[i] < minimum:
                minimum = bt[i]
                idx = i

    # If no process has arrived
    if idx == -1:
        current_time += 1
        continue

    current_time += bt[idx]
    ct[idx] = current_time
    tat[idx] = ct[idx] - at[idx]
    wt[idx] = tat[idx] - bt[idx]

    completed[idx] = True
    count += 1

# Average WT and TAT
avg_wt = sum(wt) / n
avg_tat = sum(tat) / n

# Throughput
throughput = n / max(ct)

# Output
print("\nSJF Scheduling Result")
print("-" * 65)
print("PID\tAT\tBT\tCT\tWT\tTAT")
print("-" * 65)

for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{wt[i]}\t{tat[i]}")

print("-" * 65)
print("Average Waiting Time     :", round(avg_wt, 2))
print("Average Turnaround Time  :", round(avg_tat, 2))
print("Throughput               :", round(throughput, 2), "process/unit time")