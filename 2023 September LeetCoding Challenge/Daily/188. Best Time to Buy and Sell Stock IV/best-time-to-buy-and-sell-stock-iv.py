from typing import List

'''
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6),
profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3),
profit = 3-0 = 3.

prices = [3,2,6,5,0,3]
                  |

[1, 3, 4, 5, 6, 8]

- find the highest price
- get the minimum price up until the index of the highest price
- get the profit
- start at the index of the highest price
- repeat
'''


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        size = len(prices)

        transactions = []
        start = 0
        end = 0

        for i in range(1, size):
            if prices[i] >= prices[i - 1]:
                end = i
            else:
                if end > start:
                    transactions.append([start, end])
                start = i

        if end > start:
            transactions.append([start, end])

        self.delete_or_merge(transactions, prices, k)

        profit = 0
        for start, end in transactions:
            profit += prices[end] - prices[start]

        return profit


    def delete_or_merge(self, transactions, prices, k):
        while len(transactions) > k:
            delete_idx = 0
            min_delete_loss = float('inf')
            for i in range(len(transactions)):
                dip, tip = transactions[i]
                profit_loss = prices[tip] - prices[dip]
                if profit_loss < min_delete_loss:
                    min_delete_loss = profit_loss
                    delete_idx = i

            merge_idx = 0
            min_merge_loss = float('inf')
            for i in range(1, len(transactions)):
                _, tip1 = transactions[i - 1]
                dip2, _ = transactions[i]
                profit_loss = prices[tip1] - prices[dip2]
                if profit_loss < min_merge_loss:
                    min_merge_loss = profit_loss
                    merge_idx = i

            if min_delete_loss <= min_merge_loss:
                transactions.pop(delete_idx)
            else:
                transactions[merge_idx - 1][1] = transactions[merge_idx][1]
                transactions.pop(merge_idx)


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # no transaction, no profit
        if k == 0:
            return 0
        # dp[k][0] = min cost you need to spend at most k transactions
        # dp[k][1] = max profit you can achieve at most k transactions
        dp = [[1000, 0] for _ in range(k + 1)]
        for price in prices:
            for i in range(1, k + 1):
                # price - dp[i - 1][1] is how much you need to spend
                # i.e use the profit you earned from previous transaction to buy the stock
                # we want to minimize it
                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
                # price - dp[i][0] is how much you can achieve from previous min cost
                # we want to maximize it
                dp[i][1] = max(dp[i][1], price - dp[i][0])
        # return max profit at most k transactions
		# or you can write `return dp[-1][1]`
        return dp[k][1]

    
if __name__ == '__main__':

    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    #print(prices.index(5))

    sol = Solution()
    print(sol.maxProfit(k, prices))
