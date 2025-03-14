from typing import List
from collections import Counter, defaultdict


# Checking All indices using a hashtable
class Solution:
    # O(N*A*B - (A*B)^2) Time | O(A + B) Space - "N" is the length of "s"
    # "B" is the length of each word. "A" is the length of "words".
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        string_length = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = k * word_length
        word_count = Counter(words)

        answer = []
        for i in range(string_length - substring_size + 1):
            if self.check(i, word_count, substring_size, word_length, k, s):
                answer.append(i)

        return answer


    def check(self, start_idx, word_count, substring_size, word_length, k, s):
        remaining = word_count.copy()
        words_used = 0

        end_idx = start_idx + substring_size
        for i in range(start_idx, end_idx, word_length):
            substring = s[i : i + word_length]

            if remaining[substring] > 0:
                remaining[substring] -= 1
                words_used += 1
            else:
                break

        return words_used == k



# Sliding Window
class Solution:
    # O(A + N * B) Time | O(A + B) Space - "N" is the length of "s"
    # "B" is the length of each word. "A" is the length of "words"
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        string_length = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = Counter(words)

        answer = []

        # O(N*B) Time
        def sliding_window(left):
            words_found = defaultdict(int)
            words_used = 0
            excess_word = False

            for right in range(left, string_length, word_length):
                if right + word_length > string_length:
                    break

                sub = s[right : right + word_length]
                if sub not in word_count:
                    words_found = defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length

                else:
                    while right - left == substring_size or excess_word:
                        leftmost_word = s[left : left + word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1

                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            excess_word = False
                        else:
                            words_used -= 1

                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        excess_word = True

                    if words_used == k and not excess_word:
                        answer.append(left)

            
            for i in range(word_length):
                sliding_window(i)

            return answer



if __name__ == '__main__':
    s = 'barfoothefoobarman'

    print(s[0:9])