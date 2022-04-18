# content of test_sample.py
#from main import func,func2,func3
from batchSch import process,FirstComeFirstServedSort,shortestJobNext,PrioritySort

	
def test_process_creation():
	proc1 = process(1,2,3,4)
	assert proc1.pid ==1
	
def test_process_creation():
	proc1 = process(1,2,3,4)
	assert proc1.arrival ==2
	
def test_FCFS_sort():
	avgTurnAroundTime = 0
	avgWaitTime = 0
	processArr = []
	proc1 = process(1,0,20,2)
	proc2 = process(3,0,50,1)
	proc3 = process(7,9,4,3)
	proc4 = process(2,10,12,4)
	processArr.append(proc1)
	processArr.append(proc2)
	processArr.append(proc3)
	processArr.append(proc4)

	PAT = []
	PCT = []
	PTT = []
	PBT = []
	POE = []

	for i in range(len(processArr)):
	    PBT.append(processArr[i].burst)
    
	for i in range(len(processArr)):
	    PAT.append(processArr[i].arrival)
	POE,PCT=FirstComeFirstServedSort(processArr)
	assert POE == [1,3,7,2]
	
def test_SJF_sort():
	avgTurnAroundTime = 0
	avgWaitTime = 0
	processArr = []
	proc1 = process(1,0,20,2)
	proc2 = process(3,0,50,1)
	proc3 = process(7,9,4,3)
	proc4 = process(2,10,12,4)
	processArr.append(proc1)
	processArr.append(proc2)
	processArr.append(proc3)
	processArr.append(proc4)

	PAT = []
	PCT = []
	PTT = []
	PBT = []
	POE = []

	for i in range(len(processArr)):
	    PBT.append(processArr[i].burst)
    
	for i in range(len(processArr)):
	    PAT.append(processArr[i].arrival)
	POE,PCT=shortestJobNext(processArr)
	assert POE == [1,7,1,2,3]
	
def test_priorty_sort():
	avgTurnAroundTime = 0
	avgWaitTime = 0
	processArr = []
	proc1 = process(1,0,20,2)
	proc2 = process(3,0,50,1)
	proc3 = process(7,9,4,3)
	proc4 = process(2,10,12,4)
	processArr.append(proc1)
	processArr.append(proc2)
	processArr.append(proc3)
	processArr.append(proc4)

	PAT = []
	PCT = []
	PTT = []
	PBT = []
	POE = []

	for i in range(len(processArr)):
	    PBT.append(processArr[i].burst)
    
	for i in range(len(processArr)):
	    PAT.append(processArr[i].arrival)
	POE,PCT=PrioritySort(processArr)
	assert POE == [3,1,7,2]
	
