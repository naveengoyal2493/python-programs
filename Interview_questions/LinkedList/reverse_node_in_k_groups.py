from create_linked_list import LinkedList, ListNode

class ReverseByGroup:
    def reverse_linked_list_in_reverse_of_size_k(self, head, k):
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.get_kth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # Reverse Group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next


    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

ll1 = LinkedList.insert_values([1,2,3,4,5,6,7])

out = ReverseByGroup().reverse_linked_list_in_reverse_of_size_k(ll1, 3)
LinkedList.print_ll(out)