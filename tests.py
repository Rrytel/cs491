# content of test_sample.py
#from main import func,func2,func3
from batchSch import process,FirstComeFirstServedSort,shortestJobNext,PrioritySort,setUpProcessArr,averageTurnaround,averageWait

	
def test_process_creation_for_correct_pid():
	proc1 = process(1,2,3,4)
	assert proc1.pid ==1
	
def test_process_creation_for_correct_arrival_time():
	proc1 = process(1,2,3,4)
	assert proc1.arrival ==2
	
def test_find_minimum_index_using_FCFS_on_the_first_run():
	processArr = []
	curTime = 0.00
	proc1 = process(1,0,20,2)
	proc2 = process(3,0,50,1)
	proc3 = process(7,9,4,3)
	proc4 = process(2,10,12,4)
	processArr.append(proc1)
	processArr.append(proc2)
	processArr.append(proc3)
	processArr.append(proc4)
	for i in range(len(processArr)):
		if(processArr[i].complete==False and processArr[i].arrival<=curTime):
			min = i
			break
	for i in range(len(processArr)):
		if(processArr[i].arrival < processArr[min].arrival and processArr[i].arrival<=curTime and processArr[i].complete==False):
			min = i

	for i in range(len(processArr)):
		if(processArr[i].arrival == processArr[min].arrival and processArr[i].pid < processArr[min].pid and processArr[i].complete==False):
			min = i
	assert min == 0
	
def test_processes_are_set_as_complete_corectly_after_sorting():
	processArr = []
	curTime = 5.00
	proc1 = process(1,0,20,2)
	proc2 = process(3,0,0,1)
	proc3 = process(7,9,4,3)
	proc4 = process(2,10,12,4)
	processArr.append(proc1)
	processArr.append(proc2)
	processArr.append(proc3)
	processArr.append(proc4)
	min = 1
	if(processArr[min].burst<=0):
		processArr[min].complete = True
		processArr[min].completionTime = curTime + 1
		
	assert processArr[1].complete ==True and processArr[1].completionTime == 6.00
	
def test_processes_are_correctly_added_to_POE_list_when_a_switch_is_made_from_empty_list():
	processArr = []
	POE = []
	curTime = 5.00
	previousProc = 1
	proc1 = process(1,0,20,2)
	proc2 = process(3,0,0,1)
	proc3 = process(7,9,4,3)
	proc4 = process(2,10,12,4)
	processArr.append(proc1)
	processArr.append(proc2)
	processArr.append(proc3)
	processArr.append(proc4)
	min = 3
	if(previousProc!=processArr[min].pid):
		previousProc = processArr[min].pid
		POE.append(processArr[min].pid)
	assert POE == [2]
	
def test_processes_are_correctly_added_to_POE_list_when_a_switch_is_made_from_populated_list():
	processArr = []
	POE = [1]
	curTime = 5.00
	previousProc = 1
	proc1 = process(1,0,20,2)
	proc2 = process(3,0,0,1)
	proc3 = process(7,9,4,3)
	proc4 = process(2,10,12,4)
	processArr.append(proc1)
	processArr.append(proc2)
	processArr.append(proc3)
	processArr.append(proc4)
	min = 3
	if(previousProc!=processArr[min].pid):
		previousProc = processArr[min].pid
		POE.append(processArr[min].pid)
	assert POE == [1,2]


def test_that_process_wait_time_is_correctly_incremented_per_every_loop_if_process_has_not_been_finished():
	processArr = []
	proc1 = process(1,0,20,2)
	proc2 = process(3,0,0,1)
	proc3 = process(7,9,4,3)
	proc4 = process(2,10,12,4)
	processArr.append(proc1)
	processArr.append(proc2)
	processArr.append(proc3)
	processArr.append(proc4)
	processArr[0].waitingTime = 5
	processArr[1].waitingTime = 15
	processArr[1].complete = True
	processArr[2].waitingTime = 25
	processArr[3].waitingTime = 35
	for i in range(len(processArr)):    
		if(processArr[i].complete==False):
			processArr[i].waitingTime +=1
	assert processArr[0].waitingTime == 6 and processArr[1].waitingTime == 15 and processArr[2].waitingTime == 26 and processArr[3].waitingTime == 36



def test_the_process_array_is_set_up_correctly_given_valid_text_input():
	processArr=[]
	lines = "1, 0, 20, 2\n3, 0, 50, 1\n7, 9, 4, 3\n2, 10, 12, 4"
	processArr = setUpProcessArr(lines)
	assert processArr[0].burst == 20 and processArr[1].pid == 3 and processArr[2].priority == 3 and processArr[3].arrival == 10
	
def test_average_turn_around_calculations():
	PCT = [70,40,80,100]
	PAT = [50,15,25,60]
	PTT = []
	temp = 0
	temp,PTT = averageTurnaround(PCT,PAT)
	assert temp == 35
	
def test_average_wait_calculations():
	PTT = [20,40,80,120]
	PBT = [10,20,40,80]
	temp = averageWait(PTT,PBT)
	assert temp ==27.5
	
def test_average_wait_integration_with_avg_turn_around():
	ATT = 0
	PCT =[70,40,80,100]
	PAT =[50,15,25,60]
	PTT=[]
	PBT=[5,12,6,17]
	ATT,PTT = averageTurnaround(PCT,PAT)
	AWT = averageWait(PTT,PBT)
	assert AWT == 25
	
def test_resluting_POE_array_with_integration_of_process_array_creation_followed_by_FCFS_sort():
	avgTurnAroundTime = 0
	avgWaitTime = 0
	processArr = []
	PAT = []
	PCT = []
	PTT = []
	PBT = []
	POE = []
	lines = "1, 0, 20, 2\n3, 0, 50, 1\n7, 9, 4, 3\n2, 10, 12, 4"
	processArr = setUpProcessArr(lines)
	POE,PCT=FirstComeFirstServedSort(processArr)
	assert POE == [1,3,7,2]
	
def test_resluting_PCT_array_with_integration_of_process_array_creation_followed_by_FCFS_sort():
	avgTurnAroundTime = 0
	avgWaitTime = 0
	processArr = []
	PAT = []
	PCT = []
	PTT = []
	PBT = []
	POE = []
	lines = "1, 0, 20, 2\n3, 0, 50, 1\n7, 9, 4, 3\n2, 10, 12, 4"
	processArr = setUpProcessArr(lines)
	POE,PCT=FirstComeFirstServedSort(processArr)
	assert PCT == [20.0,70.0,74.0,86.0]
	
def test_resluting_POE_array_with_integration_of_process_array_creation_followed_by_SJF_sort():
	avgTurnAroundTime = 0
	avgWaitTime = 0
	processArr = []
	PAT = []
	PCT = []
	PTT = []
	PBT = []
	POE = []
	lines = "1, 0, 20, 2\n3, 0, 50, 1\n7, 9, 4, 3\n2, 10, 12, 4"
	processArr = setUpProcessArr(lines)
	POE,PCT=shortestJobNext(processArr)
	assert POE == [1,7,1,2,3]
	
def test_resluting_PCT_array_with_integration_of_process_array_creation_followed_by_SJF_sort():
	avgTurnAroundTime = 0
	avgWaitTime = 0
	processArr = []
	PAT = []
	PCT = []
	PTT = []
	PBT = []
	POE = []
	lines = "1, 0, 20, 2\n3, 0, 50, 1\n7, 9, 4, 3\n2, 10, 12, 4"
	processArr = setUpProcessArr(lines)
	POE,PCT=shortestJobNext(processArr)
	assert PCT == [24.0,86.0,13.0,36.0]
	
def test_resluting_POE_array_with_integration_of_process_array_creation_followed_by_priorty_sort():
	avgTurnAroundTime = 0
	avgWaitTime = 0
	processArr = []
	PAT = []
	PCT = []
	PTT = []
	PBT = []
	POE = []
	lines = "1, 0, 20, 2\n3, 0, 50, 1\n7, 9, 4, 3\n2, 10, 12, 4"
	processArr = setUpProcessArr(lines)
	POE,PCT=PrioritySort(processArr)
	assert POE == [3,1,7,2]
	
def test_resluting_PCT_array_with_integration_of_process_array_creation_followed_by_priorty_sort():
	avgTurnAroundTime = 0
	avgWaitTime = 0
	processArr = []
	PAT = []
	PCT = []
	PTT = []
	PBT = []
	POE = []
	lines = "1, 0, 20, 2\n3, 0, 50, 1\n7, 9, 4, 3\n2, 10, 12, 4"
	processArr = setUpProcessArr(lines)
	POE,PCT=PrioritySort(processArr)
	assert PCT == [70.0,50.0,74.0,86.0]
	
