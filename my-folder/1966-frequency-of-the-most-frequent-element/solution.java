class Solution {
    public int maxFrequency(int[] nums, int k) {
        
        // choose an index of nums and increment the element at that index by 1
        // return max possible freq of element after performing at most k ops

        // get diff between elements
        // [1,4,8,13] = [3,0,4,7] | [7,4,0,5] | ans = 2
        // we cannot compute for each element the diff - tle

        // find how many nums diff is <= k
        // sort the array
        // see num of elements whose diff <= k

        // 1,4,8,13 - 1-4 | 4-8 | 8-13
        // 3,6,9 - 0

        if (nums.length == 1) return 1;

        Arrays.sort(nums);

        long [] prefixSum = new long [nums.length+1];
        for (int i = 0; i < nums.length; i++){
            prefixSum[i+1] = prefixSum[i] + nums[i];
        }
        int start = 0;
        int MaxFreq = 0;

        // formula = window_size - 1 * end - sum from (start to end-1)
        for (int end = 1; end < nums.length; end++ ){
            long cost = (long) (end - start) * nums[end] - (prefixSum[end] - prefixSum[start]);
            while (cost > k && start < end ) {
                start++;
                cost = (long) (end - start) * nums[end] - (
                    prefixSum[end] - prefixSum[start]
                    );
            }
            MaxFreq = Math.max(MaxFreq, end - start + 1);
        }
        return MaxFreq;
    }
}
