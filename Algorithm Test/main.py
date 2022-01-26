from asyncio.windows_events import NULL
from posixpath import basename
from classes.Node import Node
import os
os.system("cls")

# Persons
pa = Node('alice')
pb = Node('bob')
pc = Node('casi')
pd = Node('dony')
pe = Node('eric')

pe.positive()
pc.positive()
pb._hasCovidCase = True

pa.connect(pb, 'office', '12-12-21', '1:00 pm')
pa.connect(pd, 'office', '12-12-21', '1:00 pm')
pa.connect(pc, 'office', '12-12-21', '1:00 pm')
pc.connect(pd, 'office', '12-12-21', '1:00 pm')
pc.connect(pe, 'office', '12-12-21', '1:00 pm')
pe.connect(pd, 'office', '12-12-21', '1:00 pm')

# TODO
'''Create the algorithm'''


def trace(node: 'Node', _trace: dict = {}, visited: dict = {}) -> dict:
    if not node:
        return
    contacts = node.contacts.items()
    if len(contacts) is 0:
        print('Nothing to trace because the root has no travel history')
        return
    for contact in contacts:  # shape of contact: (str, Contact)
        name = contact[0]
        contact_node = contact[1].node
        if visited.get(name) is True:
            continue
        visited[name] = True
        if contact_node._hasCovidCase:
            _trace[name] = contact[1]
        trace(contact_node, _trace, visited)

    return _trace


tracing = trace(pe).items()
for each in tracing:
    name = each[0]
    print(name)
