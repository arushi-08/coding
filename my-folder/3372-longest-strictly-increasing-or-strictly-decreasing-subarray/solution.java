class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        // longest strictly inc or strictly dec SUBARRAY

        return Math.max(
            getLongestStrictlyIncreasingSubarray(nums), 
            getLongestStrictlyDecreasingSubarray(nums)
        );
    }

    public int getLongestStrictlyIncreasingSubarray(int [] nums){

        int lengthSubarrayAns = 0;
        int start = 0;
        int end = 0;

        for(int i = 1; i < nums.length; i++){
            if (nums[end] >= nums[i]){
                lengthSubarrayAns = Math.max( lengthSubarrayAns, end - start + 1 );
                start = end+1;
            }
            end++;
        }
        return Math.max( lengthSubarrayAns, end - start + 1 );
    }
    public int getLongestStrictlyDecreasingSubarray(int [] nums){

        int lengthSubarrayAns = 0;
        int start = 0;
        int end = 0;

        for(int i = 1; i < nums.length; i++){
            if (nums[end] <= nums[i]){
                lengthSubarrayAns = Math.max( lengthSubarrayAns, end - start + 1 );
                start = end+1;
            }
            end++;
        }
        return Math.max( lengthSubarrayAns, end - start + 1 );
    }
}
