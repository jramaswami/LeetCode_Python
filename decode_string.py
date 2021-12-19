"""
LeetCode :: December 2021 Challenge ::  394. Decode String
jramaswami
"""


import collections
import enum


class TType(enum.Enum):
    string = enum.auto()
    number = enum.auto()
    open_p = enum.auto()
    close_p = enum.auto()


Token = collections.namedtuple('Token', ['token', 'type'])


class Solution:
    def decodeString(self, s):

        def tokenize(s):
            tokens = []
            number = 0
            parsing_number = False
            string = []
            parsing_string = False
            for c in s:
                if c.isdigit():
                    parsing_number = True
                    number *= 10
                    number += int(c)
                else:
                    if parsing_number:
                        tokens.append(Token(number, TType.number))
                        number = 0
                        parsing_number = False

                if c.isalpha():
                    parsing_string = True
                    string.append(c)
                else:
                    if parsing_string:
                        tokens.append(Token("".join(string), TType.string))
                        string = []
                        parsing_string = False

                if c == '[':
                    tokens.append(Token(c, TType.open_p))

                if c == ']':
                    tokens.append(Token(c, TType.open_p))

            return tokens

        print(tokenize(s))



def test_1():
    s = "3[a]2[bc]"
    assert Solution().decodeString(s) == "aaabcbc"


