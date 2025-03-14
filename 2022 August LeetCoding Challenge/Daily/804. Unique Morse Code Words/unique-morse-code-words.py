from typing import List
from collections import defaultdict


class Solution:
    # O(N) Time | O(N) Space
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                      "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                      "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                      "-.--", "--.."]

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        morse_code_map = defaultdict(str)

        for idx in range(len(alphabet)):
            char = alphabet[idx]
            morse_code_map[char] = morse_code[idx]

        transformations = set()

        for word in words:
            temp = []
            for letter in word:
                temp.append(morse_code_map[letter])

            transformations.add(''.join(temp))

        return len(transformations)


if __name__ == '__main__':
    sol = Solution()

    words = ["gin","zen","gig","msg"]
    print(sol.uniqueMorseRepresentations(words))