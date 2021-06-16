# Implementation of the Set ADT container using a Python list.
class Set:
    # Creates an empty set instance.
    def __init__(self, *initElements):
        self._theElements = list()
        for i in initElements:
            self.add(i)

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        return element in self._theElements

    # Make a set printable
    def __str__(self):
        text = "{"
        first = True
        for e in self:
            if first:
                text += f'{e}'
                first = False
            else:
                text += f',{e}'
        return text + "}"

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:
            self._theElements.append(element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(element)

    # Determines if two sets are equal.
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    # Determines if this set is a subset of setB.
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    # Creates a new set from the union of this set and setB.
    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    # Creates a new set from the intersection: self set and setB.
    def interset(self, setB):
        newSet = Set()
        for element in self:
            if element in setB:
                newSet._theElements.append(element)
        return newSet

    # Creates a new set from the difference: self set and setB.
    def difference(self, setB):
        newSet = Set()
        for element in self:
            if element not in setB:
                newSet._theElements.append(element)
        return newSet

    # Check if a given set is a proper subset of another set
    def is_proper_subset(self, setB):
        if self.isSubsetOf(setB):
            if not self.__eq__(setB):
                return True

        return False

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self._theElements)

    # Magic operators
    def __add__(self, setB):
        return self.union(setB)

    def __mul__(self, setB):
        return self.interset(setB)

    def __sub__(self, setB):
        return self.difference(setB)

    def __lt__(self, setB):
        return self.isSubsetOf(setB)


class _SetIterator:
    def __init__(self, setElements):
        self._elements = setElements
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._elements):
            e = self._elements[self._index]
            self._index += 1
            return e
        else:
            raise StopIteration


if __name__ == '__main__':
    # 1.2
    s = Set(150, 23, 23, 86, 49, 23)
    print(len(s))

    # 1.3
    setA = Set(2, 0, 1)
    setB = Set(2, 0, 1)
    setC = Set(2, 0)

    print(setA.isSubsetOf(setB))
    print(setA.is_proper_subset(setB))
    print(setC.is_proper_subset(setA))

    # 1.4
    print(setA)

    # 1.6
    for e in setA:
        print(f"{e}", end="")
