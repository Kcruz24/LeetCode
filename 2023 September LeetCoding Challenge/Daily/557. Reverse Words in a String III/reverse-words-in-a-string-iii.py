class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')

        reversed_words = []

        for word in words:
            reversed_words.append(word[::-1])

        return ' '.join(reversed_words)


if __name__ == '__main__':
    sol = Solution()

    string = 'Dariel Yiram'

    print(sol.reverseWords(string))