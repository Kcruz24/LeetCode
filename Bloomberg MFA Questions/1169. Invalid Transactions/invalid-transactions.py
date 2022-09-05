from typing import List


class Solution:
    # Avg: O(N) time | O(N) space
    # Worst: (N^2) time | O(N) space
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_transactions = []
        for i in range(len(transactions)):
            curr_transaction = transactions[i]
            curr_name, curr_minutes, curr_amount, curr_city = curr_transaction.split(
                ',')

            if int(curr_amount) > 1000:
                invalid_transactions.append(curr_transaction)
                continue

            for j in range(len(transactions)):
                next_transaction = transactions[j]
                next_name, next_minutes, _, next_city = next_transaction.split(
                    ',')

                is_within_60_min = abs(
                    int(curr_minutes) - int(next_minutes)) <= 60
                is_equal_name = curr_name == next_name
                is_different_city = curr_city != next_city

                if is_equal_name and is_within_60_min and is_different_city:
                    invalid_transactions.append(curr_transaction)
                    break

        return invalid_transactions


if __name__ == '__main__':
    sol = Solution()

    transactions = ["alice,20,800,mtv", "alice,50,100,beijing"]
    transactions2 = ["alice,20,800,mtv", "bob,50,1200,mtv"]
    transactions3 = ["alice,20,800,mtv", "alice,50,1200,mtv"]
    transactions4 = ["alice,20,800,mtv",
                     "alice,50,100,mtv",
                     "alice,51,100,frankfurt"]

    transactions5 = ["alice,20,1220,mtv", "alice,20,1220,mtv"]
    print('transactions', transactions3)
    transactions6 = ["alice,20,800,mtv",
                     "bob,50,1200,mtv",
                     "alice,20,800,mtv",
                     "alice,50,1200,mtv",
                     "alice,20,800,mtv",
                     "alice,50,100,beijing"]
    transactions7 = ["alex,676,260,bangkok", "bob,656,1366,bangkok",
                     "alex,393,616,bangkok", "bob,820,990,amsterdam", "alex,596,1390,amsterdam"]

    # print(sol.invalidTransactions(transactions))
    # print(sol.invalidTransactions(transactions2))
    # print(sol.invalidTransactions(transactions3))
    # print(sol.invalidTransactions(transactions4))
    # print(sol.invalidTransactions(transactions5))
    print(sol.invalidTransactions(transactions7))
