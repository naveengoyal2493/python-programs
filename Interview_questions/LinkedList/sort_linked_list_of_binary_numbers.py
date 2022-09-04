from create_linked_list import LinkedList, ListNode

def sort_ll_of_binary_numbers(head):
    right = head = ListNode(0, head)

    while right and right.next:
        while right.next and right.next.val == 0:
            right.next = right.next.next
            head = ListNode(0, head)
        right = right.next

    return head

ll1 = LinkedList.insert_values([1,1,1,0,0,0,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1])
ll2 = sort_ll_of_binary_numbers(ll1)
LinkedList.print_ll(ll2)