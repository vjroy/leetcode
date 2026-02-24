from collections import deque

def sortedSquares(nums: list[int]) -> list[int]:
        n2 = [i ** 2 for i in nums]
        ptr1 = 0
        ptr2 = len(n2) - 1
        l = deque([])
        while ptr1 <= ptr2:
            if n2[ptr1] > n2[ptr2]:
                l.appendleft(n2[ptr1])
                ptr1 += 1
            else:
                l.appendleft(n2[ptr2])
                ptr2 -= 1

        return list(l)

nums = [-4,-1,0,3,10]

print(sortedSquares(nums))

