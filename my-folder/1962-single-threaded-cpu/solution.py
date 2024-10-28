class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        # sort tasks based on task[0]
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort()
        print('new_tasks', tasks)

        # there are 2 parts
        # many concurrent requests
        # have to compare multiple tasks with timer
        # 2nd - take min processing time
        
        timer = tasks[0][0]
        i = 0
        order = []
        candidate_tasks = []
        
        while i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= timer:
                heappush(candidate_tasks, (tasks[i][1], tasks[i][2]))
                i += 1
            if candidate_tasks:
                # print('candidate_tasks', candidate_tasks, 'timer:', timer)
                t = heappop(candidate_tasks)
                order.append(t[1])
                # print('added to order:', order)
                timer += t[0]
            else:
                timer = tasks[i][0]
            

        while candidate_tasks:
            t = heappop(candidate_tasks)
            # print('candidate_tasks', candidate_tasks)
            # print('adding to order, t:', t)
            order.append(t[1])

        return order



