"""
LeetCode
2043. Simple Bank System
October 2025 Challenge
jramaswami
"""


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = list(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        i = account1 - 1
        j = account2 - 1
        if i >= len(self.balance):
            return False
        if j >= len(self.balance):
            return False
        if money > self.balance[i]:
            return False
        self.balance[i] -= money
        self.balance[j] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        i = account - 1
        if i >= len(self.balance):
            return False
        self.balance[i] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        i = account - 1
        if i >= len(self.balance):
            return False
        if money > self.balance[i]:
            return False
        self.balance[i] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)