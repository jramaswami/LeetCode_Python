"""
LeetCode
726. Number of Atoms
July 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def parse(i):
            elements = []
            current_element = ''
            current_count = 0
            while i >= 0:
                if formula[i].islower():
                    # Add to element
                    current_element = formula[i] + current_element
                elif formula[i].isupper():
                    current_element = formula[i] + current_element
                    elements.append((current_element, max(current_count, 1)))
                    current_element = ''
                    current_count = 0
                elif formula[i].isdigit():
                    current_count = (current_count * 10) + int(formula[i])
                elif formula[i] == ')':
                    sub_formula, i = parse(i - 1)
                    if current_count:
                        sub_formula = [(t, x*current_count) for t, x in sub_formula]
                    elements.extend(sub_formula)
                    current_count = 0
                    current_element = ''
                elif formula[i] == '(':
                    return elements, i
                i -= 1
            return elements, i

        elements, _ = parse(len(formula)-1)
        freqs = collections.defaultdict(int)
        for t, x in elements:
            freqs[t] += x
        return ''.join(f'{k}{freqs[k] if freqs[k] > 1 else ""}' for k in sorted(freqs))


def test_1():
    formula = "H2O"
    expected = "H2O"
    result = Solution().countOfAtoms(formula)
    assert result == expected


def test_2():
    formula = "Mg(OH)2"
    expected = "H2MgO2"
    result = Solution().countOfAtoms(formula)
    assert result == expected


def test_3():
    formula = "K4(ON(SO3)2)2"
    expected = "K4N2O14S4"
    result = Solution().countOfAtoms(formula)
    assert result == expected


def test_4():
    """
LeetCode
726. Number of Atoms
July 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def parse(i):
            elements = []
            current_element = ''
            current_count = 0
            while i >= 0:
                if formula[i].islower():
                    # Add to element
                    current_element = formula[i] + current_element
                elif formula[i].isupper():
                    current_element = formula[i] + current_element
                    elements.append((current_element, max(current_count, 1)))
                    current_element = ''
                    current_count = 0
                elif formula[i].isdigit():
                    current_count = (current_count * 10) + int(formula[i])
                elif formula[i] == ')':
                    sub_formula, i = parse(i - 1)
                    if current_count:
                        sub_formula = [(t, x*current_count) for t, x in sub_formula]
                    elements.extend(sub_formula)
                    current_count = 0
                    current_element = ''
                elif formula[i] == '(':
                    return elements, i
                i -= 1
            return elements, i

        elements, _ = parse(len(formula)-1)
        freqs = collections.defaultdict(int)
        for t, x in elements:
            freqs[t] += x
        return ''.join(f'{k}{freqs[k] if freqs[k] > 1 else ""}' for k in sorted(freqs))


def test_1():
    formula = "H2O"
    expected = "H2O"
    result = Solution().countOfAtoms(formula)
    assert result == expected


def test_2():
    formula = "Mg(OH)2"
    expected = "H2MgO2"
    result = Solution().countOfAtoms(formula)
    assert result == expected


def test_3():
    formula = "K4(ON(SO3)2)2"
    expected = "K4N2O14S4"
    result = Solution().countOfAtoms(formula)
    assert result == expected


def test_4():
    "WA"
    formula = "Be32"
    expected = "Be32"
    result = Solution().countOfAtoms(formula)
    assert result == expected