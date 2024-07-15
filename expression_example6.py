from parse_tree import ExpressionParseTree, NumberParseTree, AdditionParseTree, MultiplicationParseTree, RemainderParseTree
from list_to_string import l2s
from vm import VM
from custom_exception import DivisionByZeroException

# ((3 + 4) * 5) % 0を計算する
three: NumberParseTree = NumberParseTree(3)
four: NumberParseTree = NumberParseTree(4)
five: NumberParseTree = NumberParseTree(5)
zero: NumberParseTree = NumberParseTree(0)
expression1: ExpressionParseTree = AdditionParseTree(three, four)
expression2: ExpressionParseTree = MultiplicationParseTree(expression1, five)
expression3: ExpressionParseTree = RemainderParseTree(expression2, zero)

print(l2s(expression3.compile()))

try:
    print(VM(expression3.compile()).run())
except DivisionByZeroException as e:
    print(e)
