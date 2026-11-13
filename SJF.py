#decleration
n = int(input("Enter the number of processes: "))

pid=[]
at=[]
bt=[]
ct=[0]*n
tat=[0]*n
wt=[0]*n
completed=[False]*n

#input
for i in range(n):
    pid.append(i+1)
    at.append(int(input(f"Enter arrival time for process {i+1}: ")))
    bt.append(int(input(f"Enter burst time for process {i+1}: ")))

current_time = 0
count = 0

while count < n:
    idx =-1
    minimum =9999
    for i in range(n):
        if at[i]<= current_time and completed[i]==False:
            if bt[i]<minimum:
                minimum = bt[i]
                idx=i
    if idx == -1:
        current_time+=1
        continue

    ct[idx]=current_time+bt[idx]
    tat[idx]=ct[idx]-at[idx]
    wt[idx]=tat[idx]-bt[idx]
    completed[idx]=True
    count+=1


avg_tat = sum(tat) / n
avg_wt = sum(wt) / n
throughput = n / max(ct)

#output
print("\nProcess ID\tArrivel ID \tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
for i in range(n):
    print(f"{pid[i]}\t\t{at[i]}\t\t{bt[i]}\t\t{ct[i]}\t\t{tat[i]}\t\t{wt[i]}")
print(f"\nAverage Turnaround Time: {avg_tat}")
print(f"Average Waiting Time: {avg_wt}")
print(f"Throughput: {throughput}")