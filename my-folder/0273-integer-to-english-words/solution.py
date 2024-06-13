class Solution:
    def numberToWords(self, num: int) -> str:

        tens = ['', 'Ten', 'Twenty', 'Thirty','Forty','Fifty', 'Sixty','Seventy',
        'Eighty', 'Ninety']
        numbers = ['','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        if num == 0:
            return 'Zero'
        def helper(num):
            ans = ''
            if num < 20:
                ans = numbers[num]
            elif num < 100:
                ans = tens[num//10] + " " + numbers[num%10]
            elif num < 1000:
                ans = numbers[num//100] + " Hundred " + helper(num%100)
            elif num < 1000000:
                ans = helper(num//1000) + " Thousand " + helper(num%1000)
            elif num < 1000000000:
                ans = helper(num//1000000) + " Million " + helper(num%1000000)
            elif num < 1000000000000:
                ans = helper(num//1000000000) + " Billion " + helper(num%1000000000)

            return ans.strip()

        return helper(num)
