class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        # for i in range(len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] > prices[i] and (prices[j]-prices[i]) > maxProfit:
        #             maxProfit = prices[j]-prices[i]
        # return maxProfit
        # for i in range(len(prices) - 1):
        #     diff = max(prices[i:]) - prices[i]
        #     if diff > maxProfit:
        #         maxProfit = diff
        left = 0
        right = 1
        while right < len(prices):
            currProfit = prices[right] - prices[left]
            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, currProfit)
            else:
                left = right
            right += 1
        return maxProfit
        