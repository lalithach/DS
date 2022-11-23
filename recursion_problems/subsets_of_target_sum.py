#Given an integer array, generate all the unique combinations of the array numbers that sum up to a given target value.
#
#Example One
#{
#"arr": [1, 2, 3],
#"target": 3
#}
#Output:
#
#[
#[3],
#[1, 2]
#]

def generate_all_combinations(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    
    # Sort the array first to bring all duplicates
    # at same place
    arr.sort(reverse=True)
    result = []
    def helper(slate, arr, index, partial_sum):
        # Back tracking case: constraint is target sum
        if partial_sum == target:
            result.append(slate[:])
            return
        
        if partial_sum > target:
            # doesnt satisfy constraint, so just return
            return
        
        if partial_sum + sum(arr[index:]) < target:
            # Even the partial sum and rest of all elememts sum,
            # Not reach the target sum. So just return
            return
        
        # partial_sum < target
        # Base case
        if len(arr) == index:
            # you reached leaf node, but sum doesnt meet constraint
            # as sum < target, so just return without adding to result
            return
        
        count = 0
        # Internal node
        # Find duplicates
        for pick in range(index, len(arr)):
            if arr[pick] == arr[index]:
                count+=1
        
        # Exclude choice
        helper(slate, arr, index+count, partial_sum)
        for pick in range(0, count):
            slate.append(arr[index])
            partial_sum+=arr[index]
            helper(slate, arr, index+count, partial_sum)
        
        for pick in range(0, count):
            slate.pop()
            
    helper([],arr,0,0)
    return result
