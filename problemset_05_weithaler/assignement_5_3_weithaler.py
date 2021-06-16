class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.age}"


def compare_by_age(person, other):
    if person.age > other.age:
        return 1
    elif person.age == other.age:
        return 0
    else:
        return -1


def compare_by_name(person, other):
    if person.age > other.age:
        return 1
    elif person.age == other.age:
        return 0
    else:
        return -1


def insertion_sort(theSeq, compare):
    n = len(theSeq)
    for i in range(1, n):
        value = theSeq[i]
        pos = i
        while pos > 0 and compare(theSeq[i], theSeq[pos - 1]) == -1:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
            theSeq[pos] = value
    return theSeq

def print_list(theSeq):
    text_p = ""
    for i in theSeq:
        text_p += f"({i}), "
    print(text_p[:-1])


if __name__ == '__main__':
    people = [
        Person("Fede", "Weit", 22),
        Person("Mario", "Rossi", 31),
        Person("Marco", "Biaggi", 12),
        Person("Gio", "Vanni", 87),
    ]

    print("Original list: ")
    print_list(people)

    print("sorted by name list: ")
    insertion_sort(people, compare_by_name)
    print_list(people)

    print("sorted by age list: ")
    insertion_sort(people, compare_by_age)
    print_list(people)
