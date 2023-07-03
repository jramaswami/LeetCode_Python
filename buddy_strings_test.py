from buddy_strings import Solution


def test_1():
    s, goal = "ab", "ba"
    expected = True
    assert Solution().buddyStrings(s, goal) == expected


def test_2():
    s, goal = "ab", "ab"
    expected = False
    assert Solution().buddyStrings(s, goal) == expected


def test_3():
    s, goal = "aa", "aa"
    expected = True
    assert Solution().buddyStrings(s, goal) == expected