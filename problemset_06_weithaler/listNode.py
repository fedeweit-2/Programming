class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, head=None):
        self._head = head

    def __str__(self):
        toString = []
        curNode = self._head
        while curNode is not None:
            toString.append(curNode.data)
            curNode = curNode.next

        return str(toString)

    def __contains__(self, target):
        curNode = self._head

        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        return curNode is not None

    def __iter__(self):
        return LinkedListIterator(self._head)

    def __len__(self):
        curNode = self._head
        count = 0
        while curNode:
            count += 1
            curNode = curNode.next
        return count

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise ValueError
        if item not in range(0, len(self)):
            raise IndexError

        curNode = self._head
        count = 0

        while curNode:
            if count == item:
                return curNode.data
            count += 1
            curNode = curNode.next

    def clear(self):
        self._head = None

    def swap(self, idx_a, idx_b):
        if idx_a == idx_b:
            return

        node_a = self[idx_a]
        node_b = self[idx_b]

        prevNode_a = None
        curNode_a = self._head
        while curNode_a is not None and curNode_a.data != node_a:
            prevNode_a = curNode_a
            curNode_a = curNode_a.next

        prevNode_b = None
        curNode_b = self._head
        while curNode_b is not None and curNode_b.data != node_b:
            prevNode_b = curNode_b
            curNode_b = curNode_b.next

        if curNode_a is None or curNode_b is None:
            return

        if prevNode_a is not None:
            prevNode_a.next = curNode_b
        else:
            self._head = curNode_b

        if prevNode_b is not None:
            prevNode_b.next = curNode_a
        else:
            self._head = curNode_a

        temp = curNode_a.next
        curNode_a.next = curNode_b.next
        curNode_b.next = temp

    def add_node(self, item):
        new_node = ListNode(item)
        new_node.next = self._head
        self._head = new_node
        return item

    def remove_node(self, item):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.data != item:
            predNode = curNode
            curNode = curNode.next

        if curNode is not None:
            if curNode is self._head:
                self._head = curNode.next
            else:
                predNode.next = curNode.next
            return item
        else:
            raise ValueError("Value to remove not found")


class LinkedListIterator:
    def __init__(self, head):
        self.head = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.head:
            element = self.head.data
            self.head = self.head.next
            return element
        else:
            raise StopIteration
