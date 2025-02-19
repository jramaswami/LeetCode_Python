"""
LeetCode
1415. The k-th Lexicographical String of All Happy Strings of Length n
February 2025 Challenge
jramaswami
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        happy_strings = []

        def rec(i, acc):
            if i >= n:
                happy_strings.append(''.join(acc))
            else:
                for char in 'abc':
                    if char != acc[-1]:
                        acc.append(char)
                        rec(i+1, acc)
                        acc.pop()
        
        rec(0, ['', ])
        happy_strings.sort()
        print(happy_strings)
        k -= 1
        if k < len(happy_strings):
            return happy_strings[k]
        return ''
