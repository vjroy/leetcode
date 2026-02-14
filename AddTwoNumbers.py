
def array(head: ListNode) -> list[int]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

def revArray(arr: list[int]) -> list[int]:
    newArr = []
    for i in range(len(arr) -1, -1, -1):
        newArr.append(arr[i])
    return newArr

def cong(arr1: list[int]) -> list[int]:
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * 10 ** (len(arr1) - i - 1)
    return sum

def lConvert(sum: int) -> ListNode:
    head = ListNode(sum % 10)
    sum //= 10
    curr = head
    while sum > 0:
        curr.next = ListNode(sum % 10)
        curr = curr.next
        sum //= 10
    return head
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return lConvert(cong(revArray(array(l1))) + cong(revArray(array(l2))))




