from tokenize import group


class ListNode:

    def __init__(self, val, next):
        self.val = val
        self.next = next

    
class LinkedList:

    @staticmethod
    def insert_at_beginning(val, head = None):
        return ListNode(val, head)        

    @staticmethod
    def insert_values(values, head = None):
        for i in range(len(values) - 1, -1, -1):
            head = LinkedList.insert_at_beginning(values[i], head)
        return head

    @staticmethod
    def merge_two_linked_lists(firsthead, lasthead):
        itr = firsthead
        while itr.next:
            itr = itr.next
        itr.next = lasthead
        return firsthead

    @staticmethod
    def print_ll(head):
        if not head:
            return "Linked list is empty"
        itr = head
        ll = ""
        while itr:
            ll += str(itr.val) + "-->"
            itr = itr.next

        print(ll)

# ll = LinkedList.insert_values([1,2,3,4,5,6])
# LinkedList.print_ll(ll)

class TwoPointerListNode:

    def __init__(self, val, next = None, bottom = None):
        self.val = val
        self.next = next
        self.bottom = bottom


def reverse_a_linked_list(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# ll = LinkedList.insert_values([1,2,3,4,5,6])
# LinkedList.print_ll(ll)
# rev_ll = reverse_a_linked_list(ll)
# LinkedList.print_ll(rev_ll)
    
def find_middle_of_linked_list(head):
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow

# ll = LinkedList.insert_values([1,2,3,4,5,7,8,9])
# new_head = find_middle_of_linked_list(ll)
# print(new_head.val)

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

# head1 = LinkedList.insert_values([1,3,5,7,15,16,17,18,19,20,21,22])
# head2 = LinkedList.insert_values([2,4,6,8,9,10,11,12,13,14])

# head3 = merge_two_sorted_linked_list(head1, head2)
# LinkedList.print_ll(head3)

def remove_nth_node_from_back(head, n):
    fast = head
    slow = head = ListNode(0, head)

    while fast and n > 0:
        fast = fast.next
        n -= 1

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return head.next

# ll = LinkedList.insert_values([1,2,3,4,5,6,7])
# new_ll = remove_nth_node_from_back(ll, 6)
# LinkedList.print_ll(new_ll)

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

# head1 = LinkedList.insert_values([5,6,7,8,9])
# head2 = LinkedList.insert_values([7,8,9,10,11,12,13,14])

# head3 = add_two_numbers_as_linked_list(head1, head2)
# LinkedList.print_ll(head3)


def delete_a_node_when_node_is_given(node):
    node.val = node.next.val
    node.next = node.next.next

    return node

# head = LinkedList.insert_values([1,2,3,4,5,6,7])
# ll = delete_a_node_when_node_is_given(head.next)
# LinkedList.print_ll(ll)

def find_intersection_point_of_y_linked_list(head1, head2):
    list1 = head1
    list2 = head2
    while list1 != list2:
        list1 = list1.next if list1 else head2
        list2 = list2.next if list2 else head1
    return list1

# l1 = ListNode(1,None)
# l2 = ListNode(2, l1)
# l3 = ListNode(3, l2)
# l4 = ListNode(4, l3)
# l5 = ListNode(5, l4)
# l6 = ListNode(6, l5)
# first_head = ListNode(7, l6)

# il1 = ListNode(11, None)
# il2 = ListNode(12, il1)
# second_head = ListNode(13, il2)

# il4 = LinkedList.merge_two_linked_lists(second_head, l4)
# ll = find_intersection_point_of_y_linked_list(first_head, second_head)
# LinkedList.print_ll(ll)

def detect_cycle_in_linked_list(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    slow2 = head

    while slow and slow.next:
        slow = slow.next
        slow2 = slow2.next

        if slow == slow2:
            return True
    
    return False

# ll1 = LinkedList.insert_values([1,2,3,4,5])
# ll1.next.next.next.next = ll1.next
# ll2 = LinkedList.insert_values([1,2,3,4,5])
# new_list = detect_cycle_in_linked_list(ll1)
# print(new_list)

# class ReverseLinkedList:

#     def reverse_linked_list_in_group_k(self, head, k):
#         dummy = ListNode(0, head)
#         group_prev = dummy

#         while True:
#             kth = self.get_kth(group_prev, k)
#             if not kth:
#                 break
#             group_next = kth.next

#             prev, curr = kth.next, group_prev.next
#             while curr != group_next:
#                 temp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = temp

#             temp = group_prev.next
#             group_prev.next = kth
#             group_prev = temp

#         return dummy.next

#     def get_kth(self, node, k):
#         while node and k > 0:
#             node = node.next
#             k -= 1
#         return node

# ll1 = LinkedList.insert_values([1,2,3,4,5,6,7])

# out = ReverseLinkedList().reverse_linked_list_in_group_k(ll1, 3)
# LinkedList.print_ll(out)


# class ReverseLinkedList:

#     def reverse_by_k_group(self, head, k):
#         dummy = ListNode(0, head)
#         group_prev = dummy

#         while True:
#             kth = self.get_kth(group_prev, k)
#             if not kth:
#                 break
#             group_next = kth.next

#             prev, curr = kth.next, group_prev.next

#             while curr != group_next:
#                 temp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = temp

#             temp = group_prev.next
#             group_prev.next = kth
#             group_prev = temp

#         return dummy.next

#     def get_kth(self, node, k):
#         while node and k > 0:
#             node = node.next
#             k -= 1
#         return node

# ll1 = LinkedList.insert_values([1,2,3,4,5,6,7])

# out = ReverseLinkedList().reverse_by_k_group(ll1, 3)
# LinkedList.print_ll(out)


# class ReverseKGroup:

#     def reverse_k_groups(self, head, k):
#         dummy = ListNode(0, head)
#         group_prev = dummy

#         while True:
#             LinkedList.print_ll(dummy)
#             kth = self.get_kth(group_prev, k)
#             if not kth:
#                 break
            
#             group_next = kth.next

#             prev, curr = kth.next, group_prev.next
#             LinkedList.print_ll(dummy)

#             while curr != group_next:
#                 temp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = temp

#             LinkedList.print_ll(dummy)

#             temp = group_prev.next
#             group_prev.next = kth
#             group_prev = temp

#             LinkedList.print_ll(dummy)

#         return dummy.next


#     def get_kth(self, node, k):
#         while node and k > 0:
#             node = node.next
#             k -= 1
#         return node

# ll1 = LinkedList.insert_values([1,2,3,4,5,6,7])

# out = ReverseKGroup().reverse_k_groups(ll1, 3)
# LinkedList.print_ll(out)

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


def find_cycle_in_linked_list_II(head):
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


# ll1 = LinkedList.insert_values([1,2,3,4,5])
# ll1.next.next.next.next = ll1.next.next
# ll2 = LinkedList.insert_values([1,2,3,4,5])
# new_list = find_cycle_in_linked_list_II(ll2)
# print(new_list)


def mergeList(headA,headB):
    fh=None
    ft=None
    while headA and headB:
        if fh==None:
            if headA.val<headB.val:
                fh=headA
                ft=headA
                headA=headA.bottom
            else:
                fh=headB
                ft=headB
                headB=headB.bottom
        else:
            if headA.val<headB.val:
                ft.bottom=headA
                headA=headA.bottom
                ft=ft.bottom
            else:
                ft.bottom=headB
                headB=headB.bottom
                ft=ft.bottom
                
                
    if headA:
        ft.bottom=headA
    if headB:
        ft.bottom=headB
    
    return fh    


def flatten(root):
    #Your code here
    if root==None:
        return None
        
    if root.next==None:
        return root
    return mergeList(root,flatten(root.next)) 

l1 = TwoPointerListNode(5)
l1.next = TwoPointerListNode(6)
l1.next.next = TwoPointerListNode(8)
l1.next.next.bottom = TwoPointerListNode(11)
l1.next.next.bottom.bottom = TwoPointerListNode(12)
l1.next.bottom = TwoPointerListNode(10)
l1.bottom = TwoPointerListNode(7)
l1.bottom.bottom = TwoPointerListNode(9)

flatten(l1)