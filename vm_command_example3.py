from command import Command
from cname import CName
from vm import VM
from list_to_string import l2s

push3 = Command(CName.PUSH, 3)
push4 = Command(CName.PUSH, 4)
add = Command(CName.ADD, None)
push2 = Command(CName.PUSH, 2)
quo = Command(CName.QUO, None)

cl = [push3, push4, add, push2, quo]
print(l2s(cl))
vm = VM(cl)
print('VM result:', vm.run())


