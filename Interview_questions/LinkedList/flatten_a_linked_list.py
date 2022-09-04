from create_linked_list import TwoPointerListNode
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