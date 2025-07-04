"""
Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, 
return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Solution:
We can get maximum profit by using two pointers.
"""

def maxProfit(prices):
    left, right = 0, 1
    maxProfit = 0
    while right < len(prices):
        if prices[left] > prices[right]:
            left = right
        else:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        right += 1
    return maxProfit

l = list(map(int, input("Enter array elements: ").split()))

print(maxProfit(l))

"""
Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the 
stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the 
maximum profit of 0.
"""
def maxProfit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit