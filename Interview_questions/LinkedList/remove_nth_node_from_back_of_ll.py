from create_linked_list import LinkedList, ListNode

def remove_nth_node_from_back_of_ll(ll, n):
    list = new_list = nl = ll.head
    count = 0
    while list:
        list = list.next
        count += 1

    if count <= 1 and n == 1:
        return []

    nth_node = count - n
    new_count = 1
    while new_list:
        if new_count == nth_node:
            new_list.next = new_list.next.next
        new_count += 1
        new_list = new_list.next
    
    return nl


def remove_nth_node_from_back(head, n):
    fast = head
    slow = head = ListNode(0, head)

    while fast and n > 0:
        fast = fast.next
        n -= 1

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return head.next

ll = LinkedList.insert_values([1,2,3,4,5,6,7])
new_ll = remove_nth_node_from_back(ll, 6)
LinkedList.print_ll(new_ll)
