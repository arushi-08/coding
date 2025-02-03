class Solution {
    public int maxProfit(int[] prices) {
        
        int maxProfitAns = 0;
        int buyPrice = Integer.MAX_VALUE;
        for (int price: prices){
            if (buyPrice > price){
                buyPrice = price;
            }
            maxProfitAns = Math.max(maxProfitAns, price - buyPrice);
        }
        return maxProfitAns;
    }
}
