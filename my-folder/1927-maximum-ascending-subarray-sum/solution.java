class Solution {
    public int maxAscendingSum(int[] nums) {
        
        // max sum of ascending subarr

        int maxSum = nums[0];
        int currSum = nums[0];

        for (int i=1 ; i < nums.length ; i++){
            if (nums[i] > nums[i-1]){
                currSum += nums[i];
            }
            else {
                maxSum = Math.max(maxSum, currSum);
                currSum = nums[i];
            }
        }
        return Math.max(maxSum, currSum);
    }
}
