class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        # t=1 2 tasktime - t=3
        # t=2 5 tasktime - t=3+5-2
        # t=4 3 tasktime
        pending_task_time = 0
        waittime = 0
        for i in range(len(customers)):
            arrival_time, task_time = customers[i]
            if arrival_time < pending_task_time:
                pending_task_time -= arrival_time
            else:
                pending_task_time = 0
            waittime += task_time + pending_task_time
            pending_task_time += task_time + arrival_time

        return waittime/len(customers)

