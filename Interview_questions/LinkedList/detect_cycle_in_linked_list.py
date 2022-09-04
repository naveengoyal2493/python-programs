from create_linked_list import LinkedList

def detect_cycle_in_linked_list(ll1):
    slow = ll1
    fast = ll1
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    slow2 = ll1
    while slow and slow.next:
        slow = slow.next
        slow2 = slow2.next

        if slow == slow2:
            return True

    return False


ll1 = LinkedList.insert_values([1,2,3,4,5])
ll1.next.next.next.next = ll1.next
ll2 = LinkedList.insert_values([1,2,3,4,5])
new_list = detect_cycle_in_linked_list(ll2)
print(new_list)

# new_ll = LinkedList(new_list)
# new_list.printll()