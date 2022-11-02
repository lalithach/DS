
def helper(arr, start, end):
    # leaf worker
    if (start == end):
        return
    # arbitary worker
    mid = (start+end)//2
    # delegate
    helper(arr, start, mid)
    helper(arr, mid+1, end)
    # combine
    i = start
    j = mid+1
    aux_arr = []
    # compare first half with second half
    # The lesser element goes to aux array
    while i<=mid and j<=end:
        if arr[i] <= arr[j]:
            aux_arr.append(arr[i])
            i+=1
        else:
            aux_arr.append(arr[j])
            j+=1
            
    # if in one half, index reaches the end,
    # append contents of other half
    while i<=mid:
        aux_arr.append(arr[i])
        i+=1
    while j<=end:
        aux_arr.append(arr[j])
        j+=1

    arr[start:end+1] = aux_arr
    return
    
def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    helper(arr, 0, len(arr)-1)
    return arr

