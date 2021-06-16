from lliststack import Stack


def print_stack(stk: Stack):
    unloaded = []
    length = len(stk)

    if not stk.is_empty():
        for i in range(length):
            unloaded.append(stk.pop())

        unloaded = unloaded[::-1]

        for j in range(length):
            stk.push(unloaded[j])

        unloaded = unloaded[::-1]

    print(f"TOP > {str(unloaded)}")


if __name__ == "__main__":
    stk = Stack()
    for i in range(3):
        stk.push(i)
    print_stack(stk)
    # should print "TOP > [2, 1, 0]
    print_stack(stk)
    # should print again "TOP > [2, 1, 0]
