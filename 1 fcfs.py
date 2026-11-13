n = int(input("Enter the number of processes: "))
pid =[]
at = []
bt = []
ct =[]
wt =[]
tat = []

#input 
for i in range(n):
    pid.append(i+1)
    at.append(int(input(f"Enter arrival time for process {i+1}: ")))
    bt.append(int(input(f"Enter burst time for process {i+1}: ")))

current_time = 0

for i in range(n):
    if current_time < at[i]:
        current_time = at[i]
    current_time += bt[i]
    ct.append(current_time)

    tat.append(ct[i] - at[i])
    wt.append(tat[i] - bt[i])

avg_tat = sum(tat) / n
avg_wt = sum(wt) / n


print("\nProcess ID\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
print("---------------------------------------------------------------------------------------------")
for i in range(n):
    print(f"{pid[i]}\t\t{at[i]}\t\t{bt[i]}\t\t{ct[i]}\t\t{tat[i]}\t\t{wt[i]}")
print("---------------------------------------------------------------------------------------------")
print(f"Average Turnaround Time: {avg_tat}")
print(f"Average Waiting Time: {avg_wt}")