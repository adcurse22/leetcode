# def mergeTwoLists(l1: list, l2: list):
#     merged_list = l1+l2
#     merged_list.sort()
#     return merged_list
#
# print(mergeTwoLists([1, 2, 3, 4,3,10], [5, 6, 7,1,2,4]))
#first solution ain't working for leetcode cuz of time error

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        if list1: tail.next=list1
        elif list2: tail.next=list2
        return dummy.next