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
    pass

#print(arr)
#print(bubble_sort(arr))

def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

    return arr

def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        min = arr[i]
        index = i
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                index = j
        arr[i], arr[index] = arr[index], arr[i]

    return arr

arr = [5, 4, 3]

#print(insertion_sort(arr))
print(selection_sort(arr))

