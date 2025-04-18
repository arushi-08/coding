class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        res = [0] * n
        pending_tasks = []
        prev_time = 0

        for log in logs:
            fnum, event_type, etime = log.split(':')
            fnum, etime = int(fnum), int(etime)

            if event_type == 'start': 
                if pending_tasks:
                    # ie., curr log is a new task start
                    # log previous work
                    res[pending_tasks[-1]] += etime - prev_time
                    
                pending_tasks.append(fnum)
                prev_time = etime
            else:
                res[pending_tasks.pop()] += etime - prev_time + 1
                prev_time = etime + 1
        
        return res

