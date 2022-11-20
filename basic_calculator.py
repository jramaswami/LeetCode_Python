"""
LeetCode :: Basic Calculator
November 2022 Challenge
jramaswami
"""

GROUPER = 0
OPERATOR = 1
VALUE = 2
EOF = 3


class Solution:

    def __init__(self):
        self.opstack = []
        self.valstack = []
        self.index = 0
        self.expression = ""

    def _get_token(self):
        # Consume whitespace
        while self.index < len(self.expression) and self.expression[self.index] == ' ':
            self.index += 1

        if self.index >= len(self.expression):
            return EOF, None

        # Return an operator
        if self.expression[self.index] in ["(", ")"]:
            token = self.expression[self.index]
            self.index += 1
            return GROUPER, token

        if self.expression[self.index] in ["+", "-"]:
            token = self.expression[self.index]
            self.index += 1
            return OPERATOR, token

        # Return a value
        value = []
        while self.index < len(self.expression) and self.expression[self.index].isdigit():
            value.append(self.expression[self.index])
            self.index += 1
        return VALUE, "".join(value)

    def _operate(self):
        """Perform one operation."""
        if self.opstack[-1] == '_':
            # Negative value
            self.opstack.pop()
            x = self.valstack.pop()
            self.valstack.append(-x)
        else:
            x = self.valstack.pop()
            y = self.valstack.pop()
            op = self.opstack.pop()
            if op == '+':
                self.valstack.append(y + x)
            elif op =='-':
                self.valstack.append(y - x)

    def _evaluate(self):
        while self.opstack or self.opstack[-1] != '(':
            self._operate()

    def _compute(self):
        prev_token = "("
        token_type, token = self._get_token()
        while token_type != EOF:
            if token == '-' and prev_token == '(':
                # Negative numbers
                token = '_'

            if token_type == OPERATOR:
                self.opstack.append(token)
            elif token_type == GROUPER:
                if token == '(':
                    # Push onto stack to start new evaluation level.
                    self.opstack.append(token)
                else:
                    # Remove matching parenthesis.
                    assert self.opstack[-1] == '('
                    self.opstack.pop()
                    # If we can evaluate then do so.
                    if self.opstack and self.opstack[-1] != '(':
                        self._operate()
            else:
                # Push value on val stack.
                self.valstack.append(int(token))
                # If we can evaluate then do so.
                if self.opstack and self.opstack[-1] != '(':
                    self._operate()

            prev_token = token
            token_type, token = self._get_token()

    def calculate(self, expression):
        self.expression = expression
        self._compute()
        return None if not self.valstack else self.valstack[-1]


def test_1():
    expression = "1 + 1"
    assert Solution().calculate(expression) == 2


def test_2():
    expression = "2-1 + 2"
    assert Solution().calculate(expression) == 3


def test_3():
    expression = "(1+(4+5+2)-3)+(6+8)"
    print(expression)
    assert Solution().calculate(expression) == 23


def test_4():
    expression = "100 + (73 - 17) + (-18)"
    assert Solution().calculate(expression) == 138


def test_5():
    """RTE"""
    expression = "-2 +1"
    assert Solution().calculate(expression) == -1
