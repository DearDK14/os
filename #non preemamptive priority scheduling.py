#non preemamptive priority scheduling 
n = int(input("Enter the number of processes: "))
pid=[]
at=[]
bt=[]
priority=[]
wt=[0]*n
tat=[0]*n
ct=[0]*n
completed=[False]*n
gantt=[]

#input
for i in range(n):  
    pid.append(input(f"Enter process ID for process {i+1}: "))
    at.append(int(input(f"Enter arrival time for process {i+1}: ")))
    bt.append(int(input(f"Enter burst time for process {i+1}: ")))
    priority.append(int(input(f"Enter priority for process {i+1} (lower number means higher priority): ")))

count=0
current_time=0

while count<n:
    idx=-1
    minimum_priority=9999
    for i in range(n):
        if completed[i]==False and at[i]<=current_time:
            if priority[i]<minimum_priority:
                minimum_priority=priority[i]
                idx=i
            elif priority[i]==minimum_priority:
                if at[i]<at[idx]:
                    idx=i
            
    if idx==-1:
        current_time+=1
    else:
        completed[idx]=True
        ct[idx]=current_time+bt[idx]
        tat[idx]=ct[idx]-at[idx]
        wt[idx]=tat[idx]-bt[idx]
        current_time=ct[idx]
        count+=1

    gantt.append((pid[idx], ct[idx]))

avg_tat=sum(tat)/n
avg_wt=sum(wt)/n
throughput=n/current_time
#output
print("\nprcess_it\tarrival_time\tburst_time\tpriority\tcompletion_time\ttat\twt")
for i in range(n):
    print(f"{pid[i]}\t\t{at[i]}\t\t{bt[i]}\t\t{priority[i]}\t\t{ct[i]}\t\t{tat[i]}\t{wt[i]}")
print(f"\nAverage Turnaround Time: {avg_tat}")
print(f"Average Waiting Time: {avg_wt}")
print(f"Throughput: {throughput}")



