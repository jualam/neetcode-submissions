# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergePair(p1,p2):
            dummy=curr=ListNode()
            while p1 and p2:
                if p1.val>p2.val:
                    curr.next=p2
                    p2=p2.next
                else:
                    curr.next=p1
                    p1=p1.next

                curr=curr.next

            if p1:
                curr.next=p1
            else:
                curr.next=p2

            return dummy.next

        while len(lists)>1:
            merged=[]
            for i in range(0,len(lists),2):
                l1=lists[i]

                if i+1<len(lists):
                    l2=lists[i+1]
                else:
                    l2=None

                merged.append(mergePair(l1,l2))

            lists=merged

        if len(lists)==0:
            return None
        else:
            return lists[0]
            