

class Solution:
    # O(N^2) Time | O(N) Space
    def longestPalindrome(self, s: str) -> str:
        i = 0
        back_ptr = 0
        front_ptr = 0

        size = len(s)
        longest = ''
        while i < size:

            while front_ptr < size and s[i] == s[front_ptr]:
                front_ptr += 1

            front_ptr -= 1

            while back_ptr >= 0 and front_ptr < size and s[front_ptr] == s[back_ptr]:
                curr_palindrome = s[back_ptr: front_ptr + 1]
                if len(curr_palindrome) > len(longest):
                    longest = curr_palindrome

                back_ptr -= 1
                front_ptr += 1

            i += 1
            back_ptr = i
            front_ptr = i

        return longest


# 116/140 Test cases passed.
class Solution:
    # O(N) Time | O(N) Space
    def longestPalindrome(self, s: str) -> str:
        i = 0
        back_ptr = 0
        front_ptr = 0

        size = len(s)
        longest = 0
        idxes = [0, 0]

        while i < size:
            count = 0
            while front_ptr < size and s[i] == s[front_ptr]:
                front_ptr += 1
                count += 1

            front_ptr -= 1

            while back_ptr >= 0 and front_ptr < size and s[front_ptr] == s[back_ptr]:
                count += 1
                if count > longest:
                    longest = count
                    idxes[0] = back_ptr
                    idxes[1] = front_ptr + 1

                back_ptr -= 1
                front_ptr += 1

            i += 1
            back_ptr = i
            front_ptr = i

        return s[idxes[0]: idxes[1]]


if __name__ == '__main__':
    sol = Solution()

    s = 'babad'
    print(sol.longestPalindrome(s))

    s = 'cbbd'
    print(sol.longestPalindrome(s))

    s = 'bbb'
    print(sol.longestPalindrome(s))

    s = 'a'
    print(sol.longestPalindrome(s))
