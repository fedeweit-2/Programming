from assignment_3_1_weithaler import *


class ParenthesisAndBracesChecker:
    def __init__(self):
        self._top = None
        self._size = 0

    def analyze_text(self, unbalanced: str):
        delimiters = Stack()
        left = ['[', '(', '{']
        right = [']', ')', '}']

        for e in unbalanced:
            if e in left:
                delimiters.push(e)
            elif e in right:
                if right.index(e) == left.index(delimiters.peek()):
                    delimiters.pop()
                else:
                    print(f'There is no left delimiter corresponding \'{e}\'')
                    raise UnbalancedParenthesisOrBracesError()

        if not delimiters.is_empty():
            remaining = ''
            for i in range(len(delimiters) - 1):
                remaining += delimiters.pop() + ', '

            remaining += delimiters.pop()

            print(f'Parenthesis and braces are unbalanced, remaining: {str(remaining)}')
            raise UnbalancedParenthesisOrBracesError()


class UnbalancedParenthesisOrBracesError(Exception):
    pass


if __name__ == "__main__":
    checker = ParenthesisAndBracesChecker()

    unbalanced_1 = "foo( bar { baz }]"

    try:
        checker.analyze_text(unbalanced_1)
        assert False, "should raise an exception"
    except UnbalancedParenthesisOrBracesError as e:
        print(e)

    unbalanced_2 = "foo( bar { baz [ }]"

    try:
        checker.analyze_text(unbalanced_2)
        assert False, "should raise an exception"
    except UnbalancedParenthesisOrBracesError as e:
        print(e)

    unbalanced_3 = "foo([( bar { baz [qux] })"

    try:
        checker.analyze_text(unbalanced_3)
        assert False, "should raise an exception"
    except UnbalancedParenthesisOrBracesError as e:
        print(e)

    balanced_4 = "foo( bar { baz [qux] })"

    checker.analyze_text(balanced_4)
