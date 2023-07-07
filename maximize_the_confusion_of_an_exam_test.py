"""
LeetCode
2024. Maximize the Confusion of an Exam
July 2023 Challenge
jramaswami
Tests
"""


from maximize_the_confusion_of_an_exam import Solution


def test_1():
    answerKey = "TTFF"
    k = 2
    expected = 4
    assert Solution().maxConsecutiveAnswers(answerKey, k) == expected


def test_2():
    answerKey = "TFFT"
    k = 1
    expected = 3
    assert Solution().maxConsecutiveAnswers(answerKey, k) == expected


def test_3():
    answerKey = "TTFTTFTT"
    k = 1
    expected = 5
    assert Solution().maxConsecutiveAnswers(answerKey, k) == expected
