"""
LeetCode
273. Integer to English Words
August 2024 Challenge
jramaswami
"""


LESS_THAN_TWENTY = {
    0: "",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen"
}

TENS = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety"
}


BIGNUMS = ["", "Thousand", "Million", "Billion"]


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def handle_tens(x):
            if x < 20:
                return LESS_THAN_TWENTY[x]
            x, y = divmod(x, 10)
            return " ".join((TENS[x], LESS_THAN_TWENTY[y])).strip()

        def handle_hundreds(x):
            if x < 100:
                return handle_tens(x)
            x, y = divmod(x, 100)
            return " ".join((handle_tens(x), "Hundred", handle_tens(y))).strip()

        parts = []
        while num:
            num, x = divmod(num, 1000)
            parts.append(handle_hundreds(x))

        soln = []
        for t, units in zip(parts, BIGNUMS):
            if t:
                if units:
                    soln.append(t + " " + units)
                else:
                    soln.append(t)
        return " ".join(reversed(soln)).strip()