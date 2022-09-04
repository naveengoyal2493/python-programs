from create_linked_list import ListNode, LinkedList

def rotate_linked_list(head, k):
    if not head:
        return 0
    dummy = head
    length = 0
    while dummy:
        dummy = dummy.next
        length += 1



ll = LinkedList().insert_values([1,2,3])
new_ll = rotate_linked_list(ll, 4)
LinkedList.print_ll(new_ll)


    

    
