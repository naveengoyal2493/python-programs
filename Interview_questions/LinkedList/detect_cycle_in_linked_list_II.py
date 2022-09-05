from create_linked_list import LinkedList, ListNode

def detect_cycle_in_linked_list(head):
    if not head:
        return
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            break

    slow2 = head
    while slow.next:
        if slow == slow2:
            return slow
        slow = slow.next
        slow2 = slow2.next

    return


ll1 = LinkedList.insert_values([1,2,3,4,5])
ll1.next.next.next.next = ll1.next
ll2 = LinkedList.insert_values([1,2,3,4,5])
new_list = detect_cycle_in_linked_list(ll2)
print(new_list.val)