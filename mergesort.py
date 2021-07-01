def merge_sort(array):
    if len(array) < 2:
        return array

    # get the mid of the array
    midpoint = len(array) // 2
    
    # recursive call until the array is broken into a list of len 1
    return merge(merge_sort(array[:midpoint]), merge_sort(array[midpoint:]))

def merge(left,right):
    l = len(left)
    m = len(right)
    result = []
    left_index=right_index=0
    while(len(result)<=(l+m)):
        # first element of both lists is compared 
        # append the lesser one and increment the index
        if left[left_index]<=right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
        # copy the other list contents into the result
        # if a list reaches its end
        if left_index == l:
            result += right[right_index:]
            break
        if right_index == m:
            result += left[left_index:]
            break
    return result


print(merge_sort([9,8,7,6,5,4,3,2,1]))  # prints [1,2,3,4,5,6,7,8,9]
