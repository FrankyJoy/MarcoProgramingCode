from timeit import dummy_src_name
from typing import Optional
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 创建链表，返回链表首对象
def createlinktable(nums: List[int]) -> ListNode:
    dummy = ListNode()
    curr = dummy
    for index, val in enumerate(nums):
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


# 链表遍历
def travellinktable(head: ListNode) -> Optional[ListNode]:
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


# 插入链表.在某个节点后插入值
def insertnode(node, val):
    newnode = ListNode(val)
    newnode.next = node.next
    node.next = newnode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # travellinktable(l1)
        # travellinktable(l2)
        cur = dummy = ListNode()
        # cur = dummy.next
        carry = 0
        while (l1 or l2 or carry):
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            print("l1: " + str(num1) + "   l2:  " + str(num2))
            sum = num1 + num2 + carry
            tmp = ListNode(sum % 10)
            cur.next = tmp
            # 数字加起来超过9，说明要进位
            carry = 1 if sum > 9 else 0
            if cur.next: cur = cur.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


if __name__ == "__main__":
    # l1 = [2, 4, 3]
    l1 = [9, 9, 9, 9, 9, 9, 9]
    # l2 = [5, 6, 4, 6]
    l2 = [9, 9, 9, 9]
    l1_head = createlinktable(nums=l1)
    l2_head = createlinktable(nums=l2)

    so = Solution()
    res = so.addTwoNumbers(l1=l1_head, l2=l2_head)
    travellinktable(res)
    print(9999 + 9999999)
