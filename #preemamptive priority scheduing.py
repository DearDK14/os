#preemamptive priority scheduing 
n = int(input("Enter the number of processes: "))
at=[]
bt=[]
pid=[]
priority=[]
rt=[]
wt=[0]*n
tat=[0]*n
ct=[0]*n

#input
for i in range(n):
    pid.append(i+1)
    at.append(int(input(f"Enter arrival time for process {i+1}: ")))
    bt.append(int(input(f"Enter burst time for process {i+1}: ")))
    priority.append(int(input(f"Enter priority for process {i+1} (lower number means higher priority): ")))
    rt.append(bt[i])  # remaining time is initially equal to burst time

current_time=0
completed=0

while completed<n:
    idx=-1
    prioritym = 9999

    for i in range(n):
        if at[i]<=current_time and rt[i]>0:
            if prioritym>priority[i]:
                prioritym=priority[i]
                idx=i
            elif prioritym==priority[i]:
                if at[i]<at[idx]:
                    idx=i
    if idx==-1:
        current_time+=1
    else:
        rt[idx]-=1
        if rt[idx]==0:
            completed+=1
            ct[idx]=current_time+1
            tat[idx]=ct[idx]-at[idx]
            wt[idx]=tat[idx]-bt[idx]
        current_time+=1
avg_tat=sum(tat)/n
avg_wt=sum(wt)/n

#output
print("\nprocess_id\tarrival_time\tburst_time\tpriority\tcompletion_time\ttat\twt")
for i in range(n):
    print(f"{pid[i]}\t\t{at[i]}\t\t{bt[i]}\t\t{priority[i]}\t\t{ct[i]}\t\t{tat[i]}\t{wt[i]}")
print(f"Average Turnaround Time: {avg_tat}")
print(f"Average Waiting Time: {avg_wt}")