from create_linked_list import LinkedList, ListNode

def add_two_numbers_as_linked_list(head1, head2):
    itr = head3 = ListNode(0, None)
    carry = 0

    while head1 or head2 or carry:
        val1 = head1.val if head1 else 0
        val2 = head2.val if head2 else 0
        sum = val1 + val2
        total_sum = (sum % 10) + carry
        carry = sum // 10
        itr.next = ListNode(total_sum, None)
        itr = itr.next

        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next

    return head3.next

head1 = LinkedList.insert_values([5,6,7,8,9])
head2 = LinkedList.insert_values([7,8,9,10,11,12,13,14])

head3 = add_two_numbers_as_linked_list(head1, head2)
LinkedList.print_ll(head3)
