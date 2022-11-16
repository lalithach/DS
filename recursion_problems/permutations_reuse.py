# This code uses recursion to return the list of all possible permutations
# for a given list of n distinct integers, reusing the array and the slate

def phelper(slate, index, arr):
# slate determines the partial solution thats passed down to subordinate
    if slate == "":
        slate = []
    if len(arr) == index:
        return [slate[:]]
    else:
        final_result = []
        for pick in range(index, len(arr)):
            # Swapping the elements such that permuations of next element would be proceeded
            arr[pick], arr[index] = arr[index], arr[pick]
            slate.append(arr[index])
            final_result.extend(phelper(slate, index+1, arr))
            # since slate has to be reused, undoing the above operations
            slate.pop()
            arr[pick], arr[index] = arr[index], arr[pick]
    return final_result
    
def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    return phelper("", 0, arr)
    
print(get_permutations([1,2,3]))
