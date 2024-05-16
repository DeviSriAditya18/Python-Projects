def round_robin(process_list,time_quanta):
    print("Process          Arrival Time          Burst Time          Completion Time          Turn Around Time            Waiting Time")
    t=0
    empty1=[]
    empty2=[]
    gantt=[]
    process_list.sort()
    burst_times={}
    for p in process_list:
        pid=p[2]
        burst_time=p[1]
        burst_times[pid]=burst_time

    while process_list!=[]:
        available=[]
        for p in process_list:
            at=p[0]
            if p[0]<=t:
                available.append(p)
        if available==[]:
            gantt.append("Idle")
            t+=1
            continue
        else:
            process=available[0]
            gantt.append(process[2])
            process_list.remove(process)
            rem_burst=process[1]
            if rem_burst<=time_quanta:
                t+=rem_burst
                ct=t
                pid=process[2]
                arrival_time=process[0]
                burst_time=burst_times[pid]
                tt=ct-arrival_time
                wt=tt-burst_time
                print(str(pid)+"\t\t\t\t\t"+str(arrival_time)+"\t\t\t\t\t\t"+str(burst_time)+"\t\t\t\t\t\t"+str(ct)+"\t\t\t\t\t\t"+str(tt)+"\t\t\t\t\t\t"+str(wt))
                empty1.append(wt)
                empty2.append(tt)
                continue
            else:
                t+=time_quanta
                process[1]-=time_quanta
                process_list.append(process)
    print(gantt)
    return (empty1,empty2)


if __name__=="__main__":
    process_list=[[2,6,"p1"],[5,2,"p2"],[1,8,"p3"],[0,3,"p4"],[4,4,"p5"]]
    time_quanta=2
    lis=round_robin(process_list,time_quanta)
    print("Average Waiting Time: "+str(sum(lis[0])/len(lis[0])))
    print("Average Turnaround Time: "+str(sum(lis[1])/len(lis[1])))