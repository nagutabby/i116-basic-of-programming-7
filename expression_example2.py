from parse_tree import ExpressionParseTree, NumberParseTree, AdditionParseTree, MultiplicationParseTree
from list_to_string import l2s
from vm import VM

# (3 + 4) * 5を計算する
three: NumberParseTree = NumberParseTree(3)
four: NumberParseTree = NumberParseTree(4)
five: NumberParseTree = NumberParseTree(5)
expression1: ExpressionParseTree = AdditionParseTree(three, four)
expression2: ExpressionParseTree = MultiplicationParseTree(expression1, five)

print(expression2)
print(l2s(expression2.compile()))
print(VM(expression2.compile()).run())
