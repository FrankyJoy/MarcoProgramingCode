from typing import List
from typing import Optional


# 类的定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 创建链表
def creat_link_table(nums: List[int]) -> ListNode:
    curr = dummy = ListNode()

    for elm in nums:
        curr.next = ListNode(elm)
        curr = curr.next
    return dummy.next


# 遍历链表
def travel_link_table(head: ListNode) -> Optional[ListNode]:
    dummy = head
    res_str = ""
    while dummy:
        res_str += str(dummy.val) + " "
        # print(dummy.val)
        dummy = dummy.next
    print(res_str)


# 节点插入
def insert_link_table(node: ListNode, val):
    newnode = ListNode(val=val)
    old_before_nextnode = node.next
    node.next = newnode
    newnode.next = old_before_nextnode


# 节点删除
def delete_link_table(head: ListNode, index=0) -> Optional[ListNode]:
    # 删除头节点
    if index == 0:
        head = head.next
        return head
    else:
        dummy = head
        for i in range(index):
            print("i= " + str(i))
            if i == index - 1:
                print("will delte val: " + str(dummy.next.val))
                print("dummy's value: " + str(dummy.val))
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return head


# 链表反向
def reverse_link_table(head: ListNode) -> ListNode:
    prev = None
    while head:
        # 把每个节点的下一个节点，指向当前节点，返回最后1个上一个节点
        next_node = head.next
        head.next = prev
        # 下一个节点指向当前节点后 prev往后滑动
        prev = head
        head = next_node
    return prev

def reverse_link_table2(head:ListNode) -> ListNode:
    prev = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp
    return prev 


if __name__ == "__main__":
    nums = [1, 2, 3]
    head = creat_link_table(nums=nums)
    travel_link_table(head)
    insert_link_table(head, val=4)
    travel_link_table(head)
    head = delete_link_table(head, 1)
    travel_link_table(head)
    head = reverse_link_table(head)
    travel_link_table(head)
    # for i in range(2):
    #     print(i)
    # print(head.val)
