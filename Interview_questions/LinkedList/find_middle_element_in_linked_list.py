from create_linked_list import LinkedList
def find_middle_of_linked_list(head):
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow

ll = LinkedList.insert_values([1,2,3,4,5,7,8,9])
new_head = find_middle_of_linked_list(ll)
print(new_head.val)

