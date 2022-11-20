
#Given an array of numbers with possible duplicates, return all of its permutations in any order.
#Example
#{
#"arr": [1, 2, 2]
#}
#Output:
#
#[
#[1, 2, 2],
#[2, 1, 2],
#[2, 2, 1]
#]

def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    result = []
    def helper(slate, arr, index):
        # Base case
        if index == len(arr):
            # Appending a copy of slate instead of reference
            result.append(slate[:])
            return
        # Internal node worker
        # For every choice
        hash_map = {}
        for pick in range(index, len(arr)):
            # Do not call the subordinate if the number is already traversed in the level
            # Use dictionary, as it can be done in O(1)
            if arr[pick] in hash_map:
                # skip since its already traversed
                continue
            else:
                hash_map[arr[pick]] = pick
            # Swap such that all choices are covered and subproblem definition stays common
            arr[index], arr[pick] = arr[pick], arr[index]
            slate.append(arr[index])
            helper(slate, arr, index+1)
            # Undo the above steps
            slate.pop()
            arr[index], arr[pick] = arr[pick], arr[index]
            
    helper([],arr,0)
    return result    
