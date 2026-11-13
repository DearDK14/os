#round robin scheduling 
n = int(input("Enter the number of processes: "))
pid=[]
at=[]
bt=[]
rt=[]
ct=[0]*n
tat=[0]*n
wt=[0]*n

#input
for i in range(n):
    pid.append(i+1)
    at.append(int(input(f"Enter arrival time for process{i+1}:")))
    bt.append(int(input(f"Enter burst time for process{i+1}:")))
    rt.append(bt[i])

tq=int(input("Enter the time quantum: "))

current_time=0
completed=0

rounds=[]
while completed<n:
    done=True
    for i in range(n):
        if rt[i]>0:
            done=False
            if rt[i]>tq:
                current_time+=tq
                rt[i]-=tq
            else:
                current_time+=rt[i]
                ct[i]=current_time
                tat[i]=ct[i]-at[i]
                wt[i]=tat[i]-bt[i]
                rt[i]=0
                completed+=1
    rounds.append(rt.copy())
    if done:
        current_time+=1
avg_tat=sum(tat)/n
avg_wt=sum(wt)/n
throughput=n/current_time

#output
print("\nRound Wise Remaining Time")

for i in range(len(rounds)):
    print("Round", i + 1, ":", rounds[i])
    
print("\nprcess_it\tarrival_time\tburst_time\tcompletion_time\ttat\twt")
for i in range(n):
    print(f"{pid[i]}\t\t{at[i]}\t\t{bt[i]}\t\t{ct[i]}\t\t{tat[i]}\t{wt[i]}")
print(f"\nAverage Turnaround Time: {avg_tat}")
print(f"Average Waiting Time: {avg_wt}")
print(f"Throughput: {throughput}")

