"""
LeetCode :: September 2021 Challenge :: Expression Add Operators
jramaswami
"""


class Solution:

    def compute(self, index, expression, numbers):
        # Hint says we can just undo last addition/subtraction when multiplying.
        if index >= len(numbers):
            print(expression)
            expression_str = "".join(expression)
            yield eval(expression_str), expression_str
        else:
            # You can add.
            expression.append("+")
            expression.append(str(numbers[index]))
            yield from self.compute(index + 1, expression, numbers)
            expression.pop()
            expression.pop()
            # You can subtract.
            expression.append("-")
            expression.append(str(numbers[index]))
            yield from self.compute(index + 1, expression, numbers)
            expression.pop()
            expression.pop()
            # You can multiply
            expression.append("*")
            expression.append(str(numbers[index]))
            yield from self.compute(index + 1, expression, numbers)
            expression.pop()
            expression.pop()

    def partition(self, index, acc, num_str):
        if index >= len(num_str):
            yield acc
        else:
            # Add the current digit to the last existing integer in acc.
            if len(acc) > 0 and acc[-1] != 0:
                acc0 = list(acc)
                acc0[-1] = (acc0[-1]) * 10 + int(num_str[index])
                yield from self.partition(index + 1, tuple(acc0), num_str)

            # Add the current digit as new number unless it is zero?
            acc1 = list(acc)
            acc1.append(int(num_str[index]))
            yield from self.partition(index + 1, tuple(acc1), num_str)

    def addOperators(self, num_str, target):
        soln = []
        for p in self.partition(0, tuple(), num_str):
            for result, expression in self.compute(1, ["+", str(p[0])], p):
                if result == target:
                    # Strip off initial "+"
                    soln.append(expression[1:])
        return soln



def test_1():
    num_str = "123"
    target = 6
    expected = ["1*2*3", "1+2+3"]
    result = Solution().addOperators(num_str, target)
    assert set(result) == set(expected)


def test_2():
    num_str = "232"
    target = 8
    expected = ["2*3+2","2+3*2"]
    result = Solution().addOperators(num_str, target)
    assert set(result) == set(expected)


def test_3():
    num_str = "105"
    target = 5
    expected = ["1*0+5","10-5"]
    result = Solution().addOperators(num_str, target)
    assert set(result) == set(expected)


def test_4():
    num_str = "00"
    target = 0
    expected = ["0*0","0+0","0-0"]
    result = Solution().addOperators(num_str, target)
    assert set(result) == set(expected)


def test_5():
    num_str = "3456237490"
    target = 9191
    expected = []
    result = Solution().addOperators(num_str, target)
    assert set(result) == set(expected)
