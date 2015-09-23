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
        cur=head
        newhead=None
        newcur=None
        distinct=True
        first=True
        curvalue=cur.val
        while cur!=None:
            curvalue=cur.val
            if cur.next is None or cur.next.val!=curvalue:
                
                if distinct:
                    if first:
                        newhead=ListNode(curvalue)
                        newcur=newhead
                        
                        first=False
                    else:
                        newcur.next=ListNode(curvalue)
                        newcur=newcur.next
                
                    
                distinct=True
            else:
                distinct=False
            cur=cur.next
        return newhead


        