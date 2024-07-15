from command import Command
from cname import CName
from vm import VM
from list_to_string import l2s
from custom_exception import VMError

push3 = Command(CName.PUSH, 3)
add = Command(CName.ADD, None)

cl = [push3, add]
print(l2s(cl))
vm = VM(cl)

try:
    print('VM result:', vm.run())
except VMError as e:
    print(e)


