class Solution:
    # O(N) Time | O(1) Space
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'

        # 3400700800
        b = 1000000000
        m = 1000000
        t = 1000

        billion = num // b
        million = (num - billion * b) // m
        thousand = ((num - billion * b) - (million * m)) // t
        rest = ((num - billion * b) - (million * m)) - (thousand * t)

        result = ''
        if billion:
            result = three(billion) + ' Billion'

        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'

        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'

        if rest:
            result += ' ' if result else ''
            result += three(rest)

        return result


def map_base_one(num):
    base_nums = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
    }
    return base_nums.get(num)


def map_two_less_than_20(num):
    two_less_than_20 = {
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen'
    }
    return two_less_than_20.get(num)


def map_two_greater_than_20(num):
    two_greater_than_20 = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety'
    }
    return two_greater_than_20.get(num)


def two(num):
    if not num:
        return ''
    elif num < 10:
        return map_base_one(num)
    elif num < 20:
        return map_two_less_than_20(num)
    else:
        tenner = num // 10
        rest = num % 10

        get_ten_str = map_two_greater_than_20(tenner)  # 20 - 99
        get_base_str = map_base_one(rest)  # 1 - 9

        return get_ten_str + ' ' + get_base_str if rest else get_ten_str


def three(num):
    hundred = num // 100
    rest = num % 100

    if hundred and rest:
        get_base_str = map_base_one(hundred)
        get_two_str = two(rest)
        return get_base_str + ' Hundred ' + get_two_str
    elif not hundred and rest:
        return two(rest)
    elif hundred and not rest:
        get_base_str = map_base_one(hundred)
        return get_base_str + ' Hundred'


if __name__ == '__main__':
    sol = Solution()

    num = 3400700800

    print(sol.numberToWords(num))
    # for i in range(10000):
    #     print(sol.numberToWords(i))
