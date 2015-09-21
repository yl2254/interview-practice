# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        current =head
        dummy = ListNode(head.val)
        dum_curr = dummy
        
        cur_dup=False
        while (current!=None):
            while (current.next!=None and (current.next.val==current.val)):
                cur_dup=True
                current.next=current.next.next
            
            if (cur_dup):
                
                current=current.next
                dum_curr.next=current
                cur_dup=False
                dum_curr=dum_curr.next
            
            else:
                dum_curr.next=current
                current=current.next
                dum_curr=dum_curr.next
            
            
        
        return dummy.next
        
        