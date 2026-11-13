# Non-Preemptive Priority Scheduling

n = int(input("Enter the number of processes: "))

pid = []
at = []
bt = []
priority = []

ct = [0] * n
wt = [0] * n
tat = [0] * n
completed = [False] * n

gantt = []

# Input
for i in range(n):
    print("\nProcess", i + 1)
    pid.append(input("Enter Process ID: "))
    at.append(int(input("Enter Arrival Time: ")))
    bt.append(int(input("Enter Burst Time: ")))
    priority.append(int(input("Enter Priority: ")))

current_time = 0
count = 0

while count < n:

    idx = -1
    highest = 9999

    for i in range(n):

        if completed[i] == False and at[i] <= current_time:

            if priority[i] < highest:
                highest = priority[i]
                idx = i

    if idx == -1:
        current_time += 1
        continue

    current_time += bt[idx]

    ct[idx] = current_time
    tat[idx] = ct[idx] - at[idx]
    wt[idx] = tat[idx] - bt[idx]

    completed[idx] = True
    count += 1

    gantt.append((pid[idx], ct[idx]))

avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
throughput = n / max(ct)

print("\nPriority Scheduling")
print("-" * 75)
print("PID\tAT\tBT\tPR\tCT\tWT\tTAT")
print("-" * 75)

for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{priority[i]}\t{ct[i]}\t{wt[i]}\t{tat[i]}")

print("-" * 75)
print("Average Waiting Time :", round(avg_wt,2))
print("Average Turnaround Time :", round(avg_tat,2))
print("Throughput :", round(throughput,2))

# Gantt Chart
print("\nGantt Chart")

print(" ", end="")
for i in range(len(gantt)):
    print("------", end="")
print()

print("|", end="")
for p in gantt:
    print(f" {p[0]} |", end="")
print()

print(" ", end="")
for i in range(len(gantt)):
    print("------", end="")
print()

print("0", end="")
for p in gantt:
    print(f"      {p[1]}", end="")
print()