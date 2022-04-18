"""
Created on Wed Mar 16 17:27:49 2022

@author: rytel
FCFS is an algorithm that is only useful if we have all of the information from the start because it is a non preemptive algorithm meaning it cannot be interupted, this makes it the simplest to implement but the least versitile. Shortests job first only compares the burst times of currently available processes preemptively giving this algorithm the major advantage of having the lowest minimum waiting time and in turn lower avgerage waiting times. Priority sort is useful for a batch system that needs additional orgraniztion in the form of certian processes needing to be completed before others.
"""
#
import sys

class process:
    def __init__(self,x,y,z,i):
        self.pid = x
        self.arrival = y
        self.burst = z
        self.complete = False
        self.completionTime = 0.0
        self.waitingTime = 0
        self.priority = i
        
        
        
def FirstComeFirstServedSort(processArr):
    curTime = 0.00
    numCompleted = 0
    previousProc = 0
    POE = []
    PCT = []
    while (numCompleted<4):
        for i in range(len(processArr)):
            if(processArr[i].complete==False and processArr[i].arrival<=curTime):
                min = i
                #print("Initial min: ", min)
                break
        
        for i in range(len(processArr)):
            if(processArr[i].arrival < processArr[min].arrival and processArr[i].arrival<=curTime and processArr[i].complete==False):
                min = i
                #print("Min changed to :", min)
                
        for i in range(len(processArr)):
            if(processArr[i].arrival == processArr[min].arrival and processArr[i].pid < processArr[min].pid and processArr[i].complete==False):
                min = i
                
        processArr[min].burst -=1
        
        if(processArr[min].burst<=0):
            processArr[min].complete = True
            processArr[min].completionTime = curTime + 1
            numCompleted+=1
            
        if(previousProc!=processArr[min].pid):
            previousProc = processArr[min].pid
            POE.append(processArr[min].pid)
            #print("Append POE", processArr[min].pid)
            
        for i in range(len(processArr)):    
            if(processArr[i].complete==False):
                processArr[i].waitingTime +=1
                
        curTime +=1
        #print(numCompleted)
        
    for i in range(len(processArr)):
        PCT.append(processArr[i].completionTime)
    #print("Completetion Times: ",PCT)
    return POE,PCT
        
def shortestJobNext(processArr):
    curTime = 0.00
    numCompleted = 0
    previousProc = 0
    POE = []
    PCT = []
    while (numCompleted<4):
    
        for i in range(len(processArr)):
            if(processArr[i].complete==False and processArr[i].arrival<=curTime):
                min = i
                break
    
        for i in range(len(processArr)):    
            if(processArr[i].burst<processArr[min].burst and processArr[i].arrival<=curTime and processArr[i].complete==False):
                min = i
                
        for i in range(len(processArr)):    
            if(processArr[i].burst == processArr[min].burst and processArr[i].arrival<=curTime and processArr[i].complete==False and processArr[i].pid < processArr[min].pid):
                min = i
                
        processArr[min].burst -=1
                
        if(processArr[min].burst<=0):
            processArr[min].complete=True
            processArr[min].completionTime = curTime + 1
            numCompleted+=1
            
        if(previousProc!=processArr[min].pid):
            previousProc = processArr[min].pid
            POE.append(processArr[min].pid)
            #print("Append POE", processArr[min].pid)
    
        for i in range(len(processArr)):    
            if(processArr[i].complete==False):
                processArr[i].waitingTime +=1
        
        #print(min,curTime,processArr[min].burst)
        curTime +=1
    
    for i in range(len(processArr)):
        PCT.append(processArr[i].completionTime)
    
    return POE,PCT

def PrioritySort(processArr):
    curTime = 0.00
    numCompleted = 0
    previousProc = 0
    POE = []
    PCT = []
    while (numCompleted<4):
        for i in range(len(processArr)):
            if(processArr[i].complete==False and processArr[i].arrival<=curTime):
                min = i
                #print("Initial min: ", min)
                break
        
        for i in range(len(processArr)):
            if(processArr[i].arrival < processArr[min].arrival and processArr[i].arrival<=curTime and processArr[i].complete==False):
                min = i
                
                
        for i in range(len(processArr)):
            if(processArr[i].arrival == processArr[min].arrival and processArr[i].priority < processArr[min].priority and processArr[i].complete==False):
                min = i
                
        for i in range(len(processArr)):
            if(processArr[i].arrival == processArr[min].arrival and processArr[i].priority == processArr[min].priority and processArr[i].complete==False and processArr[i].pid < processArr[min].pid):
                min = i
                
                
        processArr[min].burst -=1
        
        if(processArr[min].burst<=0):
            processArr[min].complete = True
            processArr[min].completionTime = curTime + 1
            numCompleted+=1
            
        if(previousProc!=processArr[min].pid):
            previousProc = processArr[min].pid
            POE.append(processArr[min].pid)
            #print("Append POE", processArr[min].pid)
            
        for i in range(len(processArr)):    
            if(processArr[i].complete==False):
                processArr[i].waitingTime +=1
                
        curTime +=1
        #print(numCompleted)
        
    for i in range(len(processArr)):
        PCT.append(processArr[i].completionTime)
    #print("Completetion Times: ",PCT)
    return POE,PCT

    

def averageTurnaround(PCT,PAT):
    PTT = []
    temp = 0.00
    avg = 0.00
    for i in range(len(PCT)):
        temp = (PCT[i]-PAT[i])
        PTT.append(temp)
        #avg += (processArr[i].completionTime - processArr[i].arrival)
        avg += temp
    return (avg/(i+1)),PTT
    
def averageWait(PTT,PBT):
    temp = 0.0
    avg = 0.0
    for i in range(len(PTT)):
    	temp = (PTT[i]-PBT[i])
    	avg += temp
    return (avg/(i+1))
   
   
def setUpProcessArr(lines):
	arr = []
	txt = lines.replace(" ","")
	txt = txt.split("\n")
	txt[0] = txt[0].split(",")
	txt[1] = txt[1].split(",")
	txt[2] = txt[2].split(",")
	txt[3] = txt[3].split(",")
	proc1 = process(int(txt[0][0]),int(txt[0][1]),int(txt[0][2]),int(txt[0][3]))
	proc2 = process(int(txt[1][0]),int(txt[1][1]),int(txt[1][2]),int(txt[1][3]))
	proc3 = process(int(txt[2][0]),int(txt[2][1]),int(txt[2][2]),int(txt[2][3]))
	proc4 = process(int(txt[3][0]),int(txt[3][1]),int(txt[3][2]),int(txt[3][3]))
	arr.append(proc1)
	arr.append(proc2)
	arr.append(proc3)
	arr.append(proc4)
	return arr

def main():
	avgTurnAroundTime = 0
	avgWaitTime = 0
	processArr = []
	if (len(sys.argv)!= 3):
	    print("Not enough arguments, please try again")
	    sys.exit()
	filename = sys.argv[1]
	algorithm = sys.argv[2]


	try:
	    with open(filename) as f:
	        lines = f.read()
	except IOError:
	    print("Failed to read file")
	    sys.exit()

	processArr = setUpProcessArr(lines)
	
	#txt = lines.replace(" ","")
	#txt = txt.split("\n")
	#txt[0] = txt[0].split(",")
	#txt[1] = txt[1].split(",")
	#txt[2] = txt[2].split(",")
	#txt[3] = txt[3].split(",")

	#proc1 = process(int(txt[0][0]),int(txt[0][1]),int(txt[0][2]),int(txt[0][3]))
	#proc2 = process(int(txt[1][0]),int(txt[1][1]),int(txt[1][2]),int(txt[1][3]))
	#proc3 = process(int(txt[2][0]),int(txt[2][1]),int(txt[2][2]),int(txt[2][3]))
	#proc4 = process(int(txt[3][0]),int(txt[3][1]),int(txt[3][2]),int(txt[3][3]))
	#processArr.append(proc1)
	#processArr.append(proc2)
	#processArr.append(proc3)
	#processArr.append(proc4)

	PAT = []
	PCT = []
	PTT = []
	PBT = []
	POE = []

	for i in range(len(processArr)):
	    PBT.append(processArr[i].burst)
    
	for i in range(len(processArr)):
	    PAT.append(processArr[i].arrival)


	if algorithm == 'FCFS':
	        POE,PCT = FirstComeFirstServedSort(processArr)
	elif algorithm == 'ShortestFirst':
		POE,PCT = shortestJobNext(processArr)
	elif algorithm == 'Priority':
		POE,PCT = PrioritySort(processArr)
	else:
		print("Enter FCFS, ShortestFirst, or Priority")
		sys.exit()       



	avgTurnAroundTime,PTT = averageTurnaround(PCT, PAT)
	avgTurnAroundTime = "{:.2f}".format(avgTurnAroundTime)
	avgWaitTime = averageWait(PTT,PBT)

	print("Process order of execution: ", POE)

	print("Average turn around time: ",avgTurnAroundTime)

	print("Average wait time: ", avgWaitTime)
	
	
	
#main()
