from command import Command
from cname import CName
from vm import VM
from list_to_string import l2s

push3 = Command(CName.PUSH, 3)
push4 = Command(CName.PUSH, 4)
push5 = Command(CName.PUSH, 5)
mul = Command(CName.MUL, None)
add = Command(CName.ADD, None)

cl = [push3, push4, push5, mul, add]
print(l2s(cl))
vm = VM(cl)
print('VM result:', vm.run())

