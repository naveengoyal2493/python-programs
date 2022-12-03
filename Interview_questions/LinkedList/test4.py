

class ListNode:

    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class LinkedList:

    @staticmethod
    def insert_at_beginning(val, head: ListNode = None):
        head = ListNode(val, head)
        return head

    @staticmethod
    def create_linked_list(values: list):
        if not values:
            return None
        new_list = itr = ListNode(0, None)

        for i in range(len(values)):
            new_list.next = ListNode(values[i])
            new_list = new_list.next

        return itr.next

    @staticmethod
    def merge_two_linked_list(head1, head2):
        cur = head1
        while cur.next:
            cur = cur.next

        cur.next = head2
        return head1


    @staticmethod
    def print_ll(head = None):
        to_print = ""
        if not head:
            return to_print

        itr = head

        while itr:
            to_print += str(itr.val) + "-->"
            itr = itr.next
        
        print(to_print)

class TwoPointerListNode:

    def __init__(self, val, next = None, bottom = None):
        self.val = val
        self.next = next
        self.bottom = bottom

# ll = LinkedList.create_linked_list([1,2,3,4,5])
# LinkedList.print_ll(ll)

def reverse_linked_list(head):
    curr = head
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

# ll = LinkedList.create_linked_list([1,2,3,4,5])
# reversed = reverse_linked_list(ll)
# LinkedList.print_ll(reversed)


def find_middle_of_linked_list(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# ll = LinkedList.create_linked_list([1,2,3,4,5,6])
# reversed = find_middle_of_linked_list(ll)
# LinkedList.print_ll(reversed)

def merge_two_sorted_linked_lists(head1, head2):
    new_list = head3 = ListNode(0)

    while head1 and head2:
        if head1.val < head2.val:
            new_list.next = ListNode(head1.val)
            head1 = head1.next
        else:
            new_list.next = ListNode(head2.val)
            head2 = head2.next
        new_list = new_list.next

    if head1:
        new_list.next = head1

    if head2:
        new_list.next = head2

    return head3.next

# head1 = LinkedList.create_linked_list([1,3,5,7,12,15,15,16])
# head2 = LinkedList.create_linked_list([2,4,6,8,9,10,11])

# merged = merge_two_sorted_linked_lists(head1, head2)
# LinkedList.print_ll(merged)


def remove_nth_node_from_back(head, n):
    slow = fast = head = ListNode(0, head)
    
    for _ in range(n):
        fast = fast.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return head.next

# head1 = LinkedList.create_linked_list([1,3,5,7,12,15,15,16])
# removed = remove_nth_node_from_back(head1, 8)
# LinkedList.print_ll(removed)

def add_two_numbers(head1, head2):
    new_list = head3 = ListNode(0)
    carry = 0

    while head1 or head2 or carry:
        val1 = head1.val if head1 else 0
        val2 = head2.val if head2 else 0

        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        total_sum = total_sum % 10
        

        new_list.next = ListNode(total_sum)
        new_list = new_list.next

        if head1:
            head1 = head1.next
        
        if head2:
            head2 = head2.next

    return head3.next

# head1 = LinkedList.create_linked_list([1,3,5,7,12,15,15,16])
# head2 = LinkedList.create_linked_list([2,4,6,8,9,10,11])

# sum_list = add_two_numbers(head1, head2)
# LinkedList.print_ll(sum_list)

def delete_a_given_node(node):
    node.val = node.next.val
    node.next = node.next.next

    return node

# head1 = LinkedList.create_linked_list([1,3,5,7,12,15,15,16])
# deleted = delete_a_given_node(head1)
# LinkedList.print_ll(deleted)

def find_intersection_point(head1, head2):
    list1 = head1
    list2 = head2
    while list1 != list2:
        list1 = list1.next if list1 else head2
        list2 = list2.next if list2 else head1
        print(list1.val if list1 else None)
        print(list2.val if list2 else None)

    return list1

# l1 = ListNode(7,None)
# l2 = ListNode(6, l1)
# l3 = ListNode(5, l2)
# l4 = ListNode(4, l3)
# l5 = ListNode(3, l4)
# l6 = ListNode(2, l5)
# first_head = ListNode(1, l6)

# il1 = ListNode(15, None)
# il2 = ListNode(14, il1)
# il3 = ListNode(13, il2)
# il4 = ListNode(12, il3)
# second_head = ListNode(11, il4)

# il4 = LinkedList.merge_two_linked_list(second_head, l4)
# ll = find_intersection_point(first_head, second_head)
# LinkedList.print_ll(ll)

def detect_a_cycle_in_linked_list(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    slow2 = head

    while slow:
        slow = slow.next
        slow2 = slow2.next

        if slow == slow2:
            return True

    return False

# ll1 = LinkedList.create_linked_list([1,2,3,4,5])
# ll1.next.next.next.next = ll1.next
# # ll1 = LinkedList.create_linked_list([1,2,3,4,5])
# new_list = detect_a_cycle_in_linked_list(ll1)
# print(new_list)

# def reverse_linked_list_in_k_groups(head, k):
    
#     def get_kth(node, k):
#         while node and k > 0:
#             node = node.next
#             k -= 1
#         return node
    
#     dummy = ListNode(0, head)
#     group_prev = dummy

#     while True:
#         kth = get_kth(group_prev, k)
#         if not kth:
#             break
#         group_next = kth.next

#         prev, curr = kth.next, group_prev.next

#         while curr != group_next:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp

#         temp = group_prev.next
#         group_prev.next = kth
#         group_prev = temp

#     return dummy.next



# ll1 = LinkedList.create_linked_list([1,2,3,4,5,6,7])

# out = reverse_linked_list_in_k_groups(ll1, 3)
# LinkedList.print_ll(out)

def reverse_linked_list_in_k_groups(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy

    def get_kth(node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node

    while True:
        kth = get_kth(group_prev, k)
        if not kth:
            break
        group_next = kth.next

        prev, curr = kth.next, group_prev.next

        while curr != group_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp

    return dummy.next

# ll1 = LinkedList.create_linked_list([1,2,3,4,5,6,7])

# out = reverse_linked_list_in_k_groups(ll1, 3)
# LinkedList.print_ll(out)

def check_if_pallindrome(head):
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None
    curr = slow
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    while prev:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next

    return True

# ll1 = LinkedList.create_linked_list([1,2,3,2,1])

# out = check_if_pallindrome(ll1)
# print(out)


def flattening_a_linked_list(head):
    if not head:
        return None

    if not head.next:
        return head

    return helper(head, flattening_a_linked_list(head.next)) 

def helper(head1, head2):
    new_list = head3 = TwoPointerListNode(0)

    while head1 and head2:
        if head1.val < head2.val:
            new_list.bottom = TwoPointerListNode(head1.val)
            head1 = head1.bottom
        else:
            new_list.bottom = TwoPointerListNode(head2.val)
            head2 = head2.bottom
        new_list = new_list.bottom

    if head1:
        new_list.bottom = head1

    if head2:
        new_list.bottom = head2

    return head3.bottom

# l1 = TwoPointerListNode(5)
# l1.next = TwoPointerListNode(6)
# l1.next.next = TwoPointerListNode(8)
# l1.next.next.bottom = TwoPointerListNode(11)
# l1.next.next.bottom.bottom = TwoPointerListNode(12)
# l1.next.bottom = TwoPointerListNode(10)
# l1.bottom = TwoPointerListNode(7)
# l1.bottom.bottom = TwoPointerListNode(9)

# head = flattening_a_linked_list(l1)
# while head:
#     print(head.val)
# #     head = head.bottom

# def rotate_a_linked_list(head, k):
#     if not head:
#         return head

#     tail = head
#     length = 1

#     while tail.next:
#         tail = tail.next
#         length += 1
    
#     k = k % length
#     if not k:
#         return head

#     curr = head
#     for _ in range(length - k - 1):
#         curr = curr.next

#     new_head = curr.next
#     curr.next = None
#     tail.next = head

#     return new_head

# ll = LinkedList().create_linked_list([1,2,3,4,5,6,7,8])
# new_ll = rotate_a_linked_list(ll, 5)
# LinkedList.print_ll(new_ll)


def rotate_linked_list(head, k):
    if not head:
        return head

    tail = head
    length = 1

    while tail and tail.next:
        tail = tail.next
        length += 1

    k = k % length
    if not k:
        return head

    curr = head
    for i in range(length - k - 1):
        curr = curr.next

    new_head = curr.next
    curr.next = None
    tail.next = head

    return new_head

# ll = LinkedList().create_linked_list([1,2,3,4,5,6,7,8])
# new_ll = rotate_linked_list(ll, 5)
# LinkedList.print_ll(new_ll)

def clone_linked_list(head):
    pass