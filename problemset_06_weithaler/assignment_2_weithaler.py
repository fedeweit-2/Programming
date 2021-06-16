from listNode import *

if __name__ == '__main__':

    # Test main developed by Christian Pala, modified by me

    # set up the current linked list as per the exercise setup.
    node_1 = ListNode(25)
    node_2 = ListNode(21)
    node_3 = ListNode(6)
    node_4 = ListNode(93)
    node_5 = ListNode(34)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    my_linked_list = SinglyLinkedList(node_1)

    # Testing __str__
    print(f'my linked list is:{my_linked_list}')
    print('-' * 100)

    # Testing add:
    my_linked_list.add_node(63)
    print(f'I can prepend an element: {my_linked_list}')
    print('-' * 100)

    # Testing __contains__
    print(f'Is 36 in my linked list? {36 in my_linked_list}')
    print(f'Is 50 in my linked list? {21 in my_linked_list}')
    print('-' * 100)

    # testing remove
    print(f'I can remove 63 from my linked list: {my_linked_list.remove_node(63)}')
    print('-' * 100)

    # testing iterator
    for i, value in enumerate(my_linked_list):
        print(f'Index {i} has a value: {value}')
    print('-' * 100)

    # testing length:
    print(f'We have {len(my_linked_list)} elements in my linked list.')
    print('-' * 100)

    # testing getter:
    print(f'The value of the node at index 1 is: {my_linked_list[1]}')
    print('-' * 100)

    # testing swaps:
    print(f'Testing swap, original list: {my_linked_list}')
    my_linked_list.swap(2, 3)
    print(f'Swapping index 2 with index 3: {my_linked_list}')
    my_linked_list.swap(3, 2)
    my_linked_list.swap(0, 4)
    print(f'Swapping index 0 with index 4: {my_linked_list}')
    my_linked_list.swap(4, 0)
    my_linked_list.swap(3, 0)
    print(f'Swapping index 3 with index 0: {my_linked_list}')
    my_linked_list.swap(0, 3)

    # testing cases where my linked list should not change, commented to remove Errors raised:
    # my_linked_list.swap(5, 0)
    # my_linked_list.swap(2, 2)
    print(f'Back to original list: {my_linked_list}')
    print('-' * 100)

    # testing clear:
    my_linked_list.clear()
    print(f'Empty list: {my_linked_list}')
