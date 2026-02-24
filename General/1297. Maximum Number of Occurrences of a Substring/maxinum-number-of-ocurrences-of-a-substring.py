class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = {}
        size = len(s)

        for j in range(size - minSize + 1):
            substring = s[j: j + minSize]

            if substring in counts:
                counts[substring] += 1
            else:
                if len(set(substring)) <= maxLetters:
                    counts[substring] = 1

        if len(counts) == 0:
            return 0

        return max(counts.values())
