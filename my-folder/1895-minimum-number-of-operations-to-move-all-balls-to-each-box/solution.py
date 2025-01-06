class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        # given n boxes
        # given binary string boxes of length n
        # boxes[i] is 0, if box is empty, else contains 1 ball
        # 
        # 1 op: move 1 ball from box to adjacent box
        # box i is adjacent to box j if abs(i-j)==1
        # min num of moves to move all balls to each box

        ans = [0]*len(boxes)
        lsum = [0]*len(boxes)
        rsum = [0]*len(boxes)
        ones_seen = 0
        for i in range(len(boxes)):
            
            if i>0:
                lsum[i] += lsum[i-1] + ones_seen

            if boxes[i]=='1':
                # lsum[i] = 1
                ones_seen += 1

        print(lsum)
        ones_seen = 0
        for i in range(len(boxes)-1,-1,-1):
            
            if i<len(boxes)-1:
                rsum[i] += rsum[i+1] + ones_seen
            if boxes[i]=='1':
                # rsum[i] = 1
                ones_seen += 1
        print(rsum)

        for i in range(len(boxes)):
            ans[i] = lsum[i] + rsum[i]
        return ans

        # 112
        #   
        
        

