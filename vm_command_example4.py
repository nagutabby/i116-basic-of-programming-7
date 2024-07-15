from command import Command
from cname import CName
from vm import VM
from list_to_string import l2s
from custom_exception import DivisionByZeroException

push3 = Command(CName.PUSH, 3)
push4 = Command(CName.PUSH, 4)
add = Command(CName.ADD, None)
push0 = Command(CName.PUSH, 0)
rem = Command(CName.QUO, None)

cl = [push3, push4, add, push0, rem]
print(l2s(cl))
vm = VM(cl)

try:
    print('VM result:', vm.run())
except DivisionByZeroException as e:
    print(e)
