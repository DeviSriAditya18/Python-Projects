def Priority(bursttime,priorities):
    print("Process          Burst Time          Waiting Time            Turn Around Time")
    i=0
    waiting_time=0
    turnaround_time=0
    empty1=[]
    empty2=[]
    while(i<len(bursttime)):
        k=min(priorities)
        turnaround_time+=bursttime[priorities.index(k)]
        print("  P"+str(priorities.index(k)+1)+"\t\t\t\t"+str(bursttime[priorities.index(k)])+"\t\t\t\t\t\t"+str(waiting_time)+"\t\t\t\t\t\t"+str(turnaround_time))
        empty1.append(waiting_time)
        empty2.append(turnaround_time)
        waiting_time+=bursttime[priorities.index(k)]
        i+=1
        priorities[priorities.index(k)]=max(priorities)+1
    return (empty1,empty2)
np=int(input("Enter no.of Processes: "))
burst_times=[]
priorities=[]
for i in range(np):
    burst_times.append(int(input("Enter the burst time for process "+str(i+1)+": ")))
for i in range(np):
    priorities.append(int(input("Enter the Priority for process P"+str(i+1)+": ")))
lis=Priority(burst_times,priorities)
print("Average Waiting Time: "+str(sum(lis[0])/len(lis[0])))
print("Average Turnaround Time: "+str(sum(lis[1])/len(lis[1])))