# FCFS Scheduling Algorithm

n = int(input("Enter the number of processes: "))

pid = []
at = []
bt = []
ct = []
wt = []
tat = []

# Input
for i in range(n):
    print("\nProcess", i + 1)
    pid.append(input("Enter Process ID: "))
    at.append(int(input("Enter Arrival Time: ")))
    bt.append(int(input("Enter Burst Time: ")))

current_time = 0

# FCFS Calculation
for i in range(n):

    if current_time < at[i]:
        current_time = at[i]

    current_time += bt[i]
    ct.append(current_time)

    tat.append(ct[i] - at[i])
    wt.append(tat[i] - bt[i])

# Average WT and TAT
avg_wt = sum(wt) / n
avg_tat = sum(tat) / n

# Throughput
throughput = n / ct[-1]

# Output
print("\nFCFS Scheduling Result")
print("-" * 65)
print("PID\tAT\tBT\tCT\tWT\tTAT")
print("-" * 65)

for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{wt[i]}\t{tat[i]}")

print("-" * 65)
print("Average Waiting Time     :", round(avg_wt, 2))
print("Average Turnaround Time  :", round(avg_tat, 2))
print("Throughput               :", round(throughput, 2), "process/unit time")