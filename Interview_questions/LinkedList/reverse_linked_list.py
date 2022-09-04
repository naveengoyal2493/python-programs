from create_linked_list import LinkedList

def reverse_a_linked_list(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# ll = LinkedList.insert_values([1,2,3,4,5,6])
# LinkedList.print_ll(ll)
# rev_ll = reverse_a_linked_list(ll)
# LinkedList.print_ll(rev_ll)
