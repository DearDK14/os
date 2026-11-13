# Shortest Remaining Time First (SRTF)

n = int(input("Enter the number of processes: "))

pid = []
at = []
bt = []

rt = []
ct = [0] * n
wt = [0] * n
tat = [0] * n

# Input
for i in range(n):
    print("\nProcess", i + 1)
    pid.append(input("Enter Process ID: "))
    at.append(int(input("Enter Arrival Time: ")))
    bt.append(int(input("Enter Burst Time: ")))
    rt.append(bt[i])

current_time = 0
completed = 0

gantt = []

while completed < n:

    idx = -1
    minimum = 9999

    # Find process with shortest remaining time
    for i in range(n):
        if at[i] <= current_time and rt[i] > 0:
            if rt[i] < minimum:
                minimum = rt[i]
                idx = i

            elif rt[i] == minimum:
                if at[i] < at[idx]:
                    idx = i

    # CPU Idle
    if idx == -1:
        current_time += 1
        continue

    # Execute for 1 unit
    rt[idx] -= 1
    gantt.append(pid[idx])
    current_time += 1

    # Process completed
    if rt[idx] == 0:
        completed += 1
        ct[idx] = current_time
        tat[idx] = ct[idx] - at[idx]
        wt[idx] = tat[idx] - bt[idx]

avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
throughput = n / max(ct)

# Output
print("\nShortest Remaining Time First (SRTF)")
print("-" * 70)
print("PID\tAT\tBT\tCT\tWT\tTAT")
print("-" * 70)

for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{wt[i]}\t{tat[i]}")

print("-" * 70)
print("Average Waiting Time :", round(avg_wt, 2))
print("Average Turnaround Time :", round(avg_tat, 2))
print("Throughput :", round(throughput, 2))

# Gantt Chart
print("\nGantt Chart")

print(" ", end="")
for i in range(len(gantt)):
    print("----", end="")
print()

print("|", end="")
for p in gantt:
    print(p, end="|")
print()

print(" ", end="")
for i in range(len(gantt)):
    print("----", end="")
print()

print("0", end="")
for i in range(1, len(gantt) + 1):
    print(f"    {i}", end="")
print()