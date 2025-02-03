class Solution {
    public int maxProfit(int[] prices) {
        
        int maxProfitAns = 0;
        int buyPrice = Integer.MAX_VALUE;
        for (int price: prices){
            buyPrice = Math.min(buyPrice, price);
            if (price - buyPrice > 0){
                maxProfitAns += price - buyPrice;
                buyPrice = price;
            }
        }
        return maxProfitAns;
    }
}
