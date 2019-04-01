""" One-way Linked List code"""


class Node():
    """Node class that has a value and is one-way linked"""
    def __init__(self, val):
        self._val = val
        self._next = None

    @property
    def data(self):
        return self._val

    @data.setter
    def data(self, _val):
        self._val = _val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, _next):
        self._next = _next

    def __repr__(self):
        return f'Node({self.data})'


class LinkedList():
    """One-way Linked List class"""
    def __init__(self, head=None):
        self.head = head
        self._count = 0

    @property
    def count(self):
        return self._count

    def insert(self, data):
        """Insert node at head"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._count += 1

    def find(self, val):
        """Find node by value"""
        item = self.head
        while item:
            if item.data == val:
                return item
            item = item.next
        return None

    def delete_at(self, idx):
        """Delete in LIFO mamner"""
        deleted_node = None
        if idx > self.count:
            return deleted_node
        if self.head:
            temp_idx = 0
            node = self.head
            while temp_idx < idx-1:
                node = node.next
                temp_idx += 1
            deleted_node = node.next
            node.next = node.next.next
            self._count -= 1
        return deleted_node

    def dump(self):
        """Dump Linked list by printing"""
        temp_node = self.head
        while temp_node:
            print('Node: ', temp_node.data)
            temp_node = temp_node.next


if __name__ == "__main__":
    # create a linked list and insert some items
    item_list = LinkedList()
    item_list.insert(73)
    item_list.insert(38)
    item_list.insert(49)
    item_list.insert(13)
    item_list.insert(15)

    item_list.dump()

    # exercise the list
    print('Item count: ', item_list.count)
    print('Finding item: ', item_list.find(13))
    print('Finding item: ', item_list.find(78))

    DELETED_NODE = item_list.delete_at(3)
    print('Deleted item at(3) -> ', DELETED_NODE)

    print('Item count: ', item_list.count)
    print('Finding item: ', item_list.find(38))
    item_list.dump()
