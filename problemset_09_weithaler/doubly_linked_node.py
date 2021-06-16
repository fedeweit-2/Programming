class DoublyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedListIterator:
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


class ReverseDoublyLinkedListIterator:
    def __init__(self, tail):
        self.tail = tail

    def __iter__(self):
        return self

    def __next__(self):
        if self.tail:
            element = self.tail.data
            self.tail = self.tail.prev
            return element
        else:
            raise StopIteration
