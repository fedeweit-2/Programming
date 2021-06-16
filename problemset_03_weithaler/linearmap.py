# Implementation of Map ADT using a single list.
class Map:
    # Creates an empty map instance.
    def __init__(self):
        self._entryList = list()

    # Returns the number of entries in the map.
    def __len__(self):
        return len(self._entryList)

    # Determines if the map contains the given key.
    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    # Adds a new entry to the map if the key does exist. Otherwise, the
    # new value replaces the current value associated with the key.
    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    # Returns the value associated with the key.
    def valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key"
        return self._entryList[ndx].value

    # Removes the entry associated with the key.
    def remove(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key"
        self._entryList.pop(ndx)

    # Returns an iterator for traversing the keys in the map.
    def __iter__(self):
        return _MapIterator(self._entryList)

    # Helper method used to find the index position of a category. If the
    # key is not found, None is returned.
    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
            else:
                return None

    # Returns an array with all the keys
    def keyArray(self):
        keys = []
        for i in range(len(self)):
            keys.append(self._entryList[i].key)

        return keys

    # Magic operators
    def __setitem__(self, key, value):
        return self.add(key, value)

    def __getitem__(self, item):
        return self.valueOf(item)


# Storage class for holding the key/value pairs.
class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class _MapIterator:
    def __init__(self, entryList):
        self._entryList = entryList
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._entryList):
            element = self._entryList[self._index]
            self._index += 1
            return element
        else:
            raise StopIteration


if __name__ == '__main__':

    # 2.1
    m = Map()
    m.add("foo", 1)
    m.add("bar", 2)
    m.add("baz", 3)

    print(m.keyArray())

    # 2.3
    for entry in m:
        print(f"{entry.key} - {entry.value}", end="\t")
