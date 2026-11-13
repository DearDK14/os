# Round Robin Scheduling

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

tq = int(input("\nEnter Time Quantum: "))

current_time = 0
completed = 0
gantt = []

# Store Remaining Burst Time after each round
rounds = []
rounds.append(rt.copy())

while completed < n:

    done = True

    for i in range(n):

        if rt[i] > 0 and at[i] <= current_time:

            done = False

            if rt[i] > tq:

                current_time += tq
                rt[i] -= tq
                gantt.append((pid[i], current_time))

            else:

                current_time += rt[i]
                rt[i] = 0

                ct[i] = current_time
                tat[i] = ct[i] - at[i]
                wt[i] = tat[i] - bt[i]

                gantt.append((pid[i], current_time))
                completed += 1 

    # Save remaining burst time after each round
    rounds.append(rt.copy())

    if done:
        current_time += 1

# Average
avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
throughput = n / max(ct)

# Round Table
print("\nRemaining Burst Time After Each Round")
print("-" * 55)

print("Round\t\t", end="")
for p in pid:
    print(p, end="\t")
print()

print("-" * 55)

for i in range(len(rounds)):

    if i == 0:
        print("Initial\t\t", end="")
    else:
        print(f"Round {i}\t\t", end="")

    for x in rounds[i]:
        print(x, end="\t")
    print()

print("-" * 55)

# Final Output
print("\nRound Robin Scheduling")
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