/**
 * @param {number[]} nums
 * @return {number}
 */
//  start with initial positive value startValue
// in each iteration, calculate the step by step sum of startValue plus elmeents in nums
var minStartValue = function(nums) {
    // -3+2-3+4 = 0
    let minPrefixSum = Infinity;
    let psum = 0;
    for (let num of nums){
        psum += num;
        minPrefixSum = Math.min(minPrefixSum, psum);
    }
    const startVal = -(minPrefixSum)+1;
    if (startVal > 0){
        return startVal;
    }
    return 1;
};
