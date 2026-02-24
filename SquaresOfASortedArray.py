def sortedSquares(nums: list[int]) -> list[int]:
    n2 = [i ** 2 for i in nums]
    return sorted(n2)

nums = [-4,-1,0,3,10]

print(sortedSquares(nums))
