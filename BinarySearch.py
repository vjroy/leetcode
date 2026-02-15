def binary_search(arr, target):
    L = 0
    R = len(arr) - 1
    while L <= R:
        M = (L + R) // 2
        if arr[M] == target:
            return f"{target} found at index {M}"
        elif arr[M] < target:
            L = M + 1
        else:
            R = M - 1
    return f"{target} not found in array"

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
print(binary_search(arr, 7))
print(binary_search(arr, 11))
print(binary_search(arr, 0))