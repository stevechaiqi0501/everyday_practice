# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res_list = []

        for i in range(len(list1)):
            res_list.append(list1[i])
            
        for i in range(len(list2)):
            res_list.append(list2[i])
            
        res_list.sort
        return res_list
        