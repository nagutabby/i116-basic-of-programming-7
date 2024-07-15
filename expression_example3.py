from parse_tree import ExpressionParseTree, NumberParseTree, MultiplicationParseTree, UnaryMinusParseTree, AdditionParseTree
from list_to_string import l2s
from vm import VM

# 3 + -(4 * 5)を計算する
three: NumberParseTree = NumberParseTree(3)
four: NumberParseTree = NumberParseTree(4)
five: NumberParseTree = NumberParseTree(5)
expression1: ExpressionParseTree = MultiplicationParseTree(four, five)
expression2: ExpressionParseTree = UnaryMinusParseTree(expression1)
expression3: ExpressionParseTree = AdditionParseTree(three, expression2)

print(expression3)
print(l2s(expression3.compile()))
print(VM(expression3.compile()).run())
