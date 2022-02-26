from collections import Counter

class Solution:
    # Failed
    # O(N) time | O(min(S, M)) space - where 'S' is the length of the given
    # string and 'M' is the length of the substring
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1

        longest_substring = ''
        all_substrings = []

        while right < len(s):

            longest_substring = s[left:right + 1]
            hashMap = Counter(longest_substring)

            if s[right] in longest_substring and hashMap[s[right]] > 1:
                all_substrings.append(s[left:right])

                while hashMap[s[right]] > 1:
                    left += 1

                    if s[left] == s[right]:
                        hashMap[s[right]] -= 1
                        left += 1
                        longest_substring = s[left:right + 1]

            right += 1

        all_substrings.append(longest_substring)
        longest = max(all_substrings, key=len)

        return longest


class Solution2:
    # Solution
    # O(N) time | O(min(N, A)) space - where "A" is the unique alphabet letters
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        longest = [0, 1]

        start_idx = 0

        for idx, char in enumerate(s):
            if char in last_seen:
                start_idx = max(start_idx, last_seen[char] + 1)

            current_substring = longest[1] - longest[0]
            running_substring = idx + 1 - start_idx

            if running_substring > current_substring:
                longest = [start_idx, idx + 1]

            last_seen[char] = idx

        longest_substring = s[longest[0]: longest[1]]

        return len(longest_substring)


if __name__ == '__main__':
    s = 'pwabcktw'
    s2 = 'aw'
    s3 = "clementisacap"
    s4 = 'pwabcwkt'

    sol = Solution2()

    print(sol.lengthOfLongestSubstring(s))
    print(sol.lengthOfLongestSubstring(s2))
    print(sol.lengthOfLongestSubstring(s3))
    print(sol.lengthOfLongestSubstring(s4))


    # arr = ['pwabc', 'abcwkt']

    # print(len(arr[0]))
    # print(len(arr[1]))

    # print(max(arr))