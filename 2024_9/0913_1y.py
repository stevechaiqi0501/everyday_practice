# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:

class Solution(object):
       def mergeTwoLists(self, list1, list2):
       dummy = ListNode()
       cur = dummy

       while list1 and list2:
           if list1.val > list2.val:
               cur.next = list2
               list2 = list2.next
           else:
               cur.next = list1
               list1 = list1.next
           
           
           cur = cur.next
       
       if list1:
           cur.next = list1
       else:
           cur.next = list2
       
       return dummy.next