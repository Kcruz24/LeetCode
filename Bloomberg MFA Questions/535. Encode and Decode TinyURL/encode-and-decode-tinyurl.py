from random import choice

class Codec:
    def __init__(self):
        self.map = {}
        self.url = 'http://tinyurl.com/'

    # O(1) Time
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        numbers = [num for num in range(100_000)]
        random_num = choice(numbers)
        self.map[random_num] = longUrl
        return self.url + str(random_num)

    # O(N) Time
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = int(shortUrl.replace(self.url, ''))
        return self.map[key]


if __name__ == '__main__':
    codec = Codec()

    # url = "https://leetcode.com/problems/design-tinyurl"

    # short_url = codec.encode(url)
    # print(short_url)
    # print(codec.decode(short_url))

    # url = "http://example.com/art.htm"
    # short_url = codec.encode(url) # 'http://example.com/z
    # print(short_url)
    # print(codec.decode(short_url)) # http://example.com/art.htm

    url = "http://example.com/account/basin.html"
    short_url = codec.encode(url)
    print(short_url)
    print(codec.decode(short_url))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


