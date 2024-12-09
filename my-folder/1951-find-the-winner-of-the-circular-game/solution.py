class Solution:
    def findTheWinner(self, n_friends: int, k: int) -> int:
        # moving clockwise from ith friend to i+1th friend
        # 1 <= i < n
        # start at 1st friend
        # count the next k friends in clockwise direction including the friend you started at
        # last friend you counted leaves the circle and loses the game
        # if there's still more than one friend in circle, go back to step 2 starting from friend immediately clockwise
        
        # while n_friends:
        # go from 1 to n_friends
        # kth person = 0
        
        # linear time and constant space
        # right now
        # loop: n_friends * n_friends
        # 2, 4, (5+1), (5+5)
        
        if n_friends == 1: return 1
        
        hop = 0
        j = 0
        friends_list = [1] * n_friends
        n = n_friends
        while n_friends:
            if friends_list[j%n] == 1:
                hop += 1

            if hop == k:
                n_friends -= 1
                hop = 0
                # print('j%n',j%n, friends_list)
                friends_list[j%n] = 0
                if n_friends == 1:
                    break
            
            j += 1
        
        return friends_list.index(1) + 1
            
            
