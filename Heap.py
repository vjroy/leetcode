A = [-4, 3, 1, 0, 2]
import heapq
heapq.heapify(A)
print(A)

heapq.heappush(A, -5)
print(A)

min = heapq.heappop(A)
print(min)
print(A)

def heapSort(A: list[int]) -> list[int]:
    heapq.heapify(A)
    arr = []
    while A:
        arr.append(heapq.heappop(A))
    return arr

print(f"Sorted array: {heapSort(A)}")

D = [5, 5, 1, 1, 1, 3, 2, 4, 2]
from collections import Counter
counter = Counter(D)
print(counter)

heap = []

for k, v in counter.items():
    heapq.heappush(heap, (v, k))

print(heap)