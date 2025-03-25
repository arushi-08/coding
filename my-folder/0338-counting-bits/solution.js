/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    const ans = Array(n+1).fill(0);
    let offset = 1;
    for (let i = 1; i < n+1; i++){
        if (i === offset * 2){
            offset = i;
        }
        // i = 1, offset = 1, ans[1] = 1 + ans[0]
        // i = 2, offset = 2, ans[2] = 1 + ans[0]
        // i = 3, offset = 2, ans[3] = 1 + ans[1]
        // i = 4, offset = 4, ans[4] = 1 + ans[0]
        // i = 5, offset = 4, ans[5] = 1 + ans[1]
        // i = 6, offset = 4, ans[6] = 1 + ans[2]
        // i = 7, offset = 4, ans[7] = 1 + ans[3]
        ans[i] = 1 + ans[i-offset];
    }
    return ans;
};

// [2-3] [4-7] [8-15]
// they have same number of binary digits
// 10, 11.  100 101                   110 111
//          4.  count(4) + count(1)  count(4) + count(2)
