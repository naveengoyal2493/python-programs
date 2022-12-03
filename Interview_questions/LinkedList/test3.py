from create_linked_list import ListNode, LinkedList

def add_two_numbers(head1, head2):
    itr = head3 = ListNode(0, None)
    carry = 0

    while head1 or head1 or carry:
        val1 = head1.val if head1 else 0
        val2 = head2.val if head2 else 0

        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        total_sum = total_sum % 10

        itr.next = ListNode(total_sum, None)
        itr = itr.next

        if head1:
            head1 = head1.next

        if head2:
            head2 = head2.next

    return head3.next

# head1 = LinkedList.insert_values([5,6,7,8,9])
# head2 = LinkedList.insert_values([7,8,9,10,11,12,13,14])

# head3 = add_two_numbers(head1, head2)
# LinkedList.print_ll(head3)

def check_if_pallindrome(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    LinkedList.print_ll(slow)

    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    left, right = head, prev
    LinkedList.print_ll(left)
    LinkedList.print_ll(right)

    while right:
        if left.val != right.val:
            return False

        left = left.next
        right = right.next
    return True


ll1 = LinkedList.insert_values([1,2,3,4,3,2,1])
new_list = check_if_pallindrome(ll1)
print(new_list)