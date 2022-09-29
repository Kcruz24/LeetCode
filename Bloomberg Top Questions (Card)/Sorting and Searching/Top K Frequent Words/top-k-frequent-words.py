from collections import Counter
import heapq
from typing import List


class Solution:
    # O(Nlog(K)) Time | O(N) Space
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)

        ans = sorted(freq, key=lambda word: (-freq[word], word))
        return ans[:k]


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #Have a dict of word and its freq
        counts = Counter(words)

        #get a array wchich will have a tuple of word and count
        heap = [(-count, word) for word, count in counts.items()]

        #as default heap structure in python min heap and we want max heap
        # to get top frequent word, we will do a make the counter negative
        #so that the topmost element will come up (i.e -8 < -2 so in min heap -8 will come up wich is actually 8)

        heapq.heapify(heap)  # creating heap in place
        #by default it will sort by freq then word

        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    sol = Solution()

    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(sol.topKFrequent(words, k))

    words = ["the", "day", "is", "sunny", "the",
             "the", "the", "sunny", "is", "is"]
    k = 4
    print(sol.topKFrequent(words, k))
