from create_linked_list import LinkedList

def check_if_pallindrome(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    left, right = head, prev

    while right:
        if left.val != right.val:
            return False

        left = left.next
        right = right.next

    return True

# ll1 = LinkedList.insert_values([1,2,3,4,4,3,2,1])
# new_list = check_if_pallindrome(ll1)
# print(new_list)