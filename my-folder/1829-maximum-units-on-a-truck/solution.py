class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # sort boxes by number of units - boxTypes[i][1]
        # get top k boxes

        boxTypes.sort(key=lambda x:x[1], reverse=True)
        i = 0
        count = 0
        while truckSize and i < len(boxTypes):
            num_boxes, num_units = boxTypes[i]
            if num_boxes <= truckSize:
                count += num_units * num_boxes
                truckSize -= num_boxes
            else:
                count += num_units * truckSize
                truckSize = 0
            i += 1
        
        return count

