arr = [5, 3, 8, 4, 2]

def bubble_sort(arr: list[int]) -> list[int]:
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swapped = True
        
    return arr

def insertion_sort(arr: list[int]) -> list[int]:

print(arr)
print(bubble_sort(arr))


            
