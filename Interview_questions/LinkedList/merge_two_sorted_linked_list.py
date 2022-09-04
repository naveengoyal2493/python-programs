from create_linked_list import LinkedList, ListNode

def merge_two_sorted_linked_list(head1, head2):
    itr = head3 = ListNode(0, None)
    while head1 and head2:
        if head1.val < head2.val:
            itr.next = ListNode(head1.val, None)
            head1 = head1.next
        else:
            itr.next = ListNode(head2.val, None)
            head2 = head2.next
        itr = itr.next

    if head1:
        itr.next = head1
    
    if head2:
        itr.next = head2

    return head3.next

head1 = LinkedList.insert_values([1,3,5,7,15,16,17,18,19,20,21,22])
head2 = LinkedList.insert_values([2,4,6,8,9,10,11,12,13,14])

head3 = merge_two_sorted_linked_list(head1, head2)
LinkedList.print_ll(head3)