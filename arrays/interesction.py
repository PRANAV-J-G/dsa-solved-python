def intersection(arr1,arr2):
    visited = []

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j] and arr1[i] not in visited:
                visited.append(arr1[i])
            if arr2[j] > arr1[i]:
                break 
    return visited

arr1 = [1,2,3,4,5,6]
arr2 = [2,3]
print(intersection(arr1,arr2))

#tc = o{n2}
#sc = o(n2)

# optimal approach 
# two pointer
def optimal(arr1,arr2):
    i = 0 
    j = 0 
    n = len(arr1)
    m = len(arr2)
    ans = []
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            ans.append(arr1[i])
            i+= 1
            j += 1 
    return ans

arr1 = [1,2,3,4,5,6]
arr2 = [4,5,6]
print(optimal(arr1,arr2))  # tc = O(n1+n2) and sc = O(1)