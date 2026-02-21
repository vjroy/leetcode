
def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for i in range(len(nums)):
        seen.add(nums[i])
    return len(nums) != len(seen)

nums = [1, 2, 3, 1]

print(containsDuplicate(nums))