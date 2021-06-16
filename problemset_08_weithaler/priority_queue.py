# Implementation of the unbounded Priority Queue ADT using a Python list # with new items appended to the end.
class PriorityQueue:

    # Create an empty unbounded priority queue.
    def __init__(self):
        self._qList = list()

    # Returns True if the queue is empty.
    def is_empty(self):
        return len(self) == 0

    # Returns the number of items in the queue.
    def __len__(self):
        return len(self._qList)

    # Adds the given item to the queue.
    def enqueue(self, item, priority):
        # Create a new instance of the storage class and append it to the list.
        entry = _PriorityQEntry(item, priority)
        self._qList.append(entry)

    # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."

        # Find the entry with the highest priority.
        highest = self._qList[0].priority
        highest_index = 0
        for i in range(len(self)):
            # See if the ith entry contains a higher priority (smaller integer).
            if self._qList[i].priority < highest:
                highest = self._qList[i].priority
                highest_index = i
        # Remove the entry with the highest priority and return the item.
        entry = self._qList.pop(highest_index)
        return entry.item


# Private storage class for associating queue items with their priority.
class _PriorityQEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
