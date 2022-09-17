from test_programs.test56 import ListNode


def find_the_starting_point_of_loop(head):
    if not head:
        return

    if not head.next:
        return

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    slow2 = head
    while slow.next:
        if slow == slow2:
            return slow
        slow = slow.next
        slow2 = slow2.next

    return

