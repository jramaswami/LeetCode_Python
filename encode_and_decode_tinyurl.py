"""
LeetCode :: April 2022 Challenge :: Encode and Decode TinyURL
jramaswami
"""


import string


class Codec:

    def __init__(self):
        self.urls = []
        self.alpha = string.ascii_uppercase

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        i = len(self.urls)
        self.urls.append(longUrl)
        shortUrl = []
        for _ in range(7):
            i, r = divmod(i, len(self.alpha))
            shortUrl.append(self.alpha[r])
        return "".join(reversed(shortUrl))

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        i = 0
        m = 1
        for c in reversed(shortUrl):
            i += m * (ord(c) - ord(self.alpha[0]))
            m *= len(self.alpha)
        return self.urls[i]


#
# Testing
#


import random


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


def test_1():
    url = "https://www.google.com/"
    codec = Codec()
    assert codec.decode(codec.encode(url))


def test_2():
    codec = Codec()
    url = "https://www.leetcode.com/"
    assert codec.decode(codec.encode(url))


def test_3():
    codec = Codec()
    for _ in range(50000):
        url = random.choices(string.ascii_letters, k=20)
        assert codec.decode(codec.encode(url))
