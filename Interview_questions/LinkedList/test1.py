from tokenize import group
from create_linked_list import LinkedList, Node


def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

# ll1 = LinkedList()
# ll1.insert_values([1,2,3,4,5])
# ll1.printll()
# ll2 = LinkedList(reverse_linked_list(ll1.head))
# out = ll2.printll()

def find_middle_of_linked_list(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# ll1 = LinkedList()
# ll1.insert_values([1,2,3,4,5,6,7,8,9,10])
# ll1.printll()

# out = LinkedList(find_middle_of_linked_list(ll1.head))
# out.printll()

def merge_two_linked_list(list1, list2):
    list3 = head3 = Node("", None)

    while list1 and list2:
        if list1.data < list2.data:
            list3.next = Node(list1.data, None)
            list1 = list1.next
        else:
            list3.next = Node(list2.data, None)
            list2 = list2.next
        list3 = list3.next

    if list1:
        list3.next = list1

    if list2:
        list3.next = list2

    return head3.next

# ll1 = LinkedList()
# ll1.insert_values([1,3,5,7,9])
# ll2 = LinkedList()
# ll2.insert_values([2,4,6,8,10,11,12,13])
# out = LinkedList(merge_two_linked_list(ll1.head, ll2.head))
# out.printll()

def remove_nth_node_from_back(head, n):
    slow = itr = Node(0, head)
    fast = head

    while n > 0 and fast:
        fast = fast.next
        n -= 1

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return itr.next

# ll2 = LinkedList()
# ll2.insert_values([2,4,6,8,10,11,12,13])
# out = LinkedList(remove_nth_node_from_back(ll2.head, 8))
# out.printll()

def add_two_numbers_in_linkedlist(head1, head2):
    list3 = head3 = Node(0, None)
    carry = 0

    while head1 or head2 or carry:
        val1 = head1.data if head1 else 0
        val2 = head2.data if head2 else 0

        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        total_sum = total_sum % 10
        list3.next = Node(total_sum, None)
        list3 = list3.next
        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next

    return head3.next

# ll1 = LinkedList()
# ll1.insert_values([2,4,6,8,10,11,12,13])
    
# ll2 = LinkedList()
# ll2.insert_values([2,4,6,8,10,11,12,13])
# out = LinkedList(add_two_numbers_in_linkedlist(ll1.head, ll2.head))
# out.printll()

def delete_a_given_node(node):
    node.data = node.next.data
    node.next = node.next.next

# node = head = Node(0, None)
# node = node.next
# node.next = Node(10, None)
# node = node.next
# node.next = Node(20, None)
# node = node.next
# node.next = Node(30, None)
# node = node.next

# new_node = head

# delete_a_given_node(new_node.next.next)

def find_intersection_point_of_ll(head1, head2):
    ptr1 = head1
    ptr2 = head2

    while ptr1 != ptr2:
        ptr1 = ptr1.next if ptr1 else head2
        ptr2 = ptr2.next if ptr2 else head1

        print(ptr1.data)
        print(ptr2.data)

    return ptr1

# ll1 = LinkedList()
# ll1.insert_values([1,2,3,4,5])

# ll2 = LinkedList()
# ll2.insert_values([0,1,2,3,4,5,6])

# ll3 = LinkedList(find_intersection_point_of_ll(ll1.head, ll2.head))
# ll3.printll()


def check_linked_list_is_pallindrome(head):
    new_list = []
    slow = fast = head
    new_list.append(slow.data)

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        new_list.append(slow.data)

    while slow:

        slow = slow.next

    