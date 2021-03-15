"""
LeetCode :: March 2021 Challenge :: Encode and Decode TinyURL
jramaswami
"""
import string

class Codec:

    def __init__(self):
        self.urls = []
        self.digits = string.digits + string.ascii_letters

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        index = len(self.urls)
        self.urls.append(longUrl)
        
        S = []
        q = index
        for _ in range(7):
            q, r = divmod(q, len(self.digits))
            S.append(r)
        return "http//tinyurl.com/" + "".join(self.digits[r] for r in reversed(S))

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        _, encoded = shortUrl.rsplit('/', 1)
        b = 1
        index = 0
        for c in reversed(encoded):
            index += (b * self.digits.find(c))
            b *= len(self.digits)
        return self.urls[index]

        
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
    url = "https://www.google.com/"
    codec = Codec()
    assert codec.decode(codec.encode(url))
    url = "https://www.leetcode.com/"
    assert codec.decode(codec.encode(url))

def test_3():
    codec = Codec()
    for _ in range(50000):
        url = random.choices(string.ascii_letters, k=20)
        assert codec.decode(codec.encode(url))
