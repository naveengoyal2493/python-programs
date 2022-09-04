from create_linked_list import LinkedList, ListNode

def find_intersection_point_of_y_linked_list(head1, head2):
    list1 = head1
    list2 = head2
    while list1 != list2:
        list1 = list1.next if list1 else head2
        list2 = list2.next if list2 else head1
    return list1

###########################################################################
l1 = ListNode(1,None)
l2 = ListNode(2, l1)
l3 = ListNode(3, l2)
l4 = ListNode(4, l3)
l5 = ListNode(5, l4)
l6 = ListNode(6, l5)
first_head = ListNode(7, l6)

il1 = ListNode(11, None)
il2 = ListNode(12, il1)
second_head = ListNode(13, il2)

il4 = LinkedList.merge_two_linked_lists(second_head, l4)
ll = find_intersection_point_of_y_linked_list(first_head, second_head)
LinkedList.print_ll(ll)





        