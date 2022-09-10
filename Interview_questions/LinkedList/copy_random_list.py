from create_linked_list import NextAndRandomListNode


def copy_random_list(head):
    dictionary = {None:None}

    cur = head

    while cur:
        copy = NextAndRandomListNode(cur.val)
        dictionary[cur] = copy
        cur = cur.next

    cur = head

    while cur:
        copy = dictionary[cur]
        copy.next = dictionary[cur.next]
        copy.random = dictionary[cur.random]
        cur = cur.next

    return dictionary[head]
