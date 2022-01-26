
from asyncio.windows_events import NULL


class Node:
    '''This Node class represents each App user or person'''

    def __init__(self, name) -> None:
        self.name: str = name
        # we don't want duplicate values so use Dict
        self.contacts: dict(str, Contact) = {}
        self._isPositive: bool = False
        self._hasCovidCase: bool = False
        self.date_of_positivity = NULL

    def connect(self, new_node: 'Node', est: str, date: str, time: str) -> None:
        '''Connect two nodes bidirectionally.'''
        # checks if new_node is already connected
        if self.contacts.get(new_node.name):
            return
        self.contacts[new_node.name] = Contact(new_node, est, date, time)
        new_node.contacts[self.name] = Contact(self, est, date, time)

    def positive(self):
        self._isPositive = True
        self._hasCovidCase = True

    def negative(self):
        self._isPositive = False

    def positive_neighbors(self) -> list:
        return [
            contact for contact in self.contacts.items() if contact[1].node._hasCovidCase
        ]


class Contact:
    '''Serves as the adjacency list of the graph'''

    def __init__(self,
                 node: Node,
                 establishment: str,
                 date: str,
                 time: str) -> None:
        self.node = node
        self.establishment = establishment
        self.date = date
        self.time = time
