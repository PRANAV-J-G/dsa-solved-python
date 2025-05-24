''' 
time complexity is the same as merge sort tc = O(n*logN) 
but space complexity is O(N) without the use of an extra array 


1) pick the pivot element and place it in the correct place in the sorted array 
2) smaller on the left and larger on the right 
'''

def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1         # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Swap arr[i+1] and arr[high] (or pivot)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)
