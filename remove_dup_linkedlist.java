/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head==null || head.next==null) return head;
        ListNode current =head;
        ListNode previous=head;
        
        Boolean cur_dup=false;
        while (current!=null){
            while (current.next!=null && (current.next.val==current.val)){
                cur_dup=true;
                current.next=current.next.next;
                previous=null;
            }
            if (cur_dup){
                cur_dup=false;
                if (previous==null){
                    if (current.next==null){
                        head=null;
                    }
                    else{
                        head=current.next.next;
                        current=head;
                    }
                
                }
                else{
                    previous.next=current.next.next;
                    current=previous.next;
                    previous=current;
                }
               
            }
            else{
                previous=current;
                current=current.next;
            }
            
        }
        return head;
    }
    
}