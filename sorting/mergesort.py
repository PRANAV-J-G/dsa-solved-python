def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def ms(arr, low, high):
    if low >= high:
        return arr
    mid = (low + high) // 2
    ms(arr, low, mid)
    ms(arr, mid + 1, high)
    merge(arr, low, mid, high)

def mergesort(arr, n):
    ms(arr, 0, n - 1)


arr = [38, 27, 43, 3, 9, 82, 10]
mergesort(arr, len(arr))
print(arr)
