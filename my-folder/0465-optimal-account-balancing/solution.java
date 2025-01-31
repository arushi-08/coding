class Solution {
    public int minTransfers(int[][] transactions) {
        // return min num of transactions required to settle debt
        /*
        person 0: -10 -9  -4    -10
        person 1:  10 9 4        20
        person 2:       5 0     -50
        person 3:                40
        person 0 gets 10 from next person 1 20 (10 left)
        person 1 gives 10 to person 2
        person 3 gives 40 to person 3
        3 transactions
        
        count the num of people who owe or are owed and create transaction

        sort ascending order of negatives and positives
        -10 -50 | 20 40

        10  50 | -20 -40
        i.        j
        make each = 0, move ptr forward
        count transaction
        */

        int [] debt = new int[12];

        for (int i=0; i < transactions.length; i++){
            int amt = transactions[i][2];
            debt[transactions[i][0]] -= amt;
            debt[transactions[i][1]] += amt;
        }
        // backtracking
        return backtrack(0, debt);
    
    }
    
    public int backtrack(int idx, int[] debt){

        while (idx < debt.length && debt[idx]==0) idx++;
        if (idx == debt.length) return 0;

        int result = Integer.MAX_VALUE;
        for (int i=idx+1; i < debt.length; i++){
            if (debt[idx] * debt[i] < 0) {
                debt[i] += debt[idx];
                result = Math.min(result, backtrack(idx+1, debt)+1);
                debt[i] -= debt[idx];
            } 
        }
        return result;

    }
}
