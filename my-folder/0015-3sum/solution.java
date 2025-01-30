class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        /*
        iterate on nums
        2 pointer method
        i = 2
        j = 0 to i-1 = 0-1
        k = n to i+1 = n-3
        -4,-1,-1,0,1,2
        -4-1=-5, k<5, so j++;
        -1-1=-2, k==2 -> triplet found
        j++;
        i = 3
        -4-0=-4, k<4; j++;
        -1-0=-1 k>1; k--; k==1 -> triplet found
        -1 found again -> continue
        */

        int n = nums.length;
        Arrays.sort(nums);
        
        ArrayList<List<Integer>> ans = new ArrayList<>();

        for (int i=0;i<n && nums[i] <= 0;i++){
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int j = i+1;
            int k = n-1;
            while (j < k){
                int sum = nums[j] + nums[i] + nums[k];
                if (sum == 0){
                    ans.add(Arrays.asList(nums[i], nums[j++], nums[k--]));
                    while (j < k && nums[j] == nums[j-1]){
                        j++;
                    }
                }
                else if (sum > 0){
                    k--;
                }
                else {
                    j++;
                }
            }
        }
        return ans;
    }
}
