from create_linked_list import ListNode, LinkedList

def rotate_linked_list(head, k):
    if not head:
        return head
    
    tail = head
    length = 1
    while tail and tail.next:
        tail = tail.next
        length += 1

    k = k % length 
    if k == 0:
        return head

    curr = head
    for i in range(length - k - 1):
        curr = curr.next

    new_head = curr.next
    curr.next = None
    tail.next = head

    return new_head

ll = LinkedList().insert_values([1,2,3])
new_ll = rotate_linked_list(ll, 4)
LinkedList.print_ll(new_ll)


    

    
