from parse_tree import ExpressionParseTree, NumberParseTree, MultiplicationParseTree, AdditionParseTree
from list_to_string import l2s
from vm import VM

# 3 + 4 * 5を計算する
three: NumberParseTree = NumberParseTree(3)
four: NumberParseTree = NumberParseTree(4)
five: NumberParseTree = NumberParseTree(5)
expression1: ExpressionParseTree = MultiplicationParseTree(four, five)
expression2: ExpressionParseTree = AdditionParseTree(three, expression1)

print(expression2)
print(l2s(expression2.compile()))
print(VM(expression2.compile()).run())
