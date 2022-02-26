from typing import List


class Solution3:

    # O(N) time | O(N) space
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        name_idx = 0
        time_idx = 1
        amount_idx = 2
        city_idx = 3

        invalid_transactions = []

        for transaction in transactions:
            split_t1 = transaction.split(',')

            if int(split_t1[amount_idx]) > 1000:
                invalid_transactions.append(transaction)
                continue

            for transaction2 in transactions:
                split_t2 = transaction2.split(',')

                is_name_equal = split_t1[name_idx] == split_t2[name_idx]
                is_within_60_min = abs(
                    int(split_t1[time_idx]) - int(split_t2[time_idx])) <= 60
                is_city_different = split_t1[city_idx] != split_t2[city_idx]

                if is_name_equal and is_within_60_min and is_city_different:
                    invalid_transactions.append(transaction)
                    break

        return invalid_transactions

class Solution2:
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        T = []
        for t in transactions:
            temp = t.split(',')
            temp[1] = int(temp[1])
            temp[2] = int(temp[2])
            T.append(temp)

        print('T', T)
        invalidT = []
        for t in T:
            if t[2] > 1000:
                t[1] = str(t[1])
                t[2] = str(t[2])
                invalidT.append(','.join(t))
                continue
            # print('t', t)
            # print('T inside', T)
            for x in T:
                # print('x', x)
                if t[0] == x[0] and abs(t[1] - int(x[1])) <= 60 and t[3] != x[3]:
                    t[1] = str(t[1])
                    t[2] = str(t[2])
                    invalidT.append(','.join(t))
                    break

        return invalidT

class Solution:
    def __init__(self):
        self.name_idx = 0
        self.time_idx = 1
        self.amount_idx = 2
        self.city_idx = 3

    # O(N) time | O(N) space
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if len(transactions) == 1:
            split_transaction = transactions[0].split(',')
            transaction_amount = split_transaction[self.amount_idx]

            if int(transaction_amount) > 1000:
                return transactions

            return []

        invalid_transactions = []

        for idx in range(len(transactions) - 1):
            curr_transaction = transactions[idx].split(',')
            next_transaction = transactions[idx + 1].split(',')

            if self.__get_amount(curr_transaction) > 1000:
                invalid_transactions.append(transactions[idx])

            is_name_equal = self.__get_name(
                curr_transaction) == self.__get_name(next_transaction)
            is_city_different = self.__get_city(
                curr_transaction) != self.__get_city(next_transaction)
            is_within_60_min = abs(self.__get_time(
                curr_transaction) - self.__get_time(next_transaction))

            if is_name_equal and is_city_different and is_within_60_min:
                invalid_transactions.append(transactions[idx])
                invalid_transactions.append(transactions[idx + 1])
            elif is_name_equal and is_within_60_min and not is_city_different:
                invalid_transactions.append(transactions[idx])

        last_transaction = transactions[len(transactions) - 1].split(',')

        if self.__get_amount(last_transaction) > 1000:
            invalid_transactions.append(transactions[len(transactions) - 1])

        return invalid_transactions

    def __get_amount(self, transaction):
        return int(transaction[self.amount_idx])

    def __get_name(self, transaction):
        return transaction[self.name_idx]

    def __get_city(self, transaction):
        return transaction[self.city_idx]

    def __get_time(self, transaction):
        return int(transaction[self.time_idx])


if __name__ == '__main__':
    sol = Solution2()
    sol3 = Solution3()

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
    print(sol3.invalidTransactions(transactions7))
