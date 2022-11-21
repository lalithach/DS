#Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.
#
#Example One
#{
#"n": 5,
#"k": 2
#}
#Output:
#[
#[1, 2],[1, 3],[1, 4],[1, 5],[2, 3],[2, 4],[2, 5],[3, 4],[3, 5],[4, 5]
#]

def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    result = []
    arr = [i for i in range(1,n+1)]
    def helper(slate, index, arr):
        
        # Backtracking case: constraint is size k
        if len(slate) == k:
            # If size is equal to k, then add it to global result
            # and dont traverse further
            result.append(slate[:])
            return
        # if length of slate is less than k
        # base case
        if index == len(arr):
            # since size is < k, but we reached leaf node, 
            # this solution wont go to result as it doesnt
            # meet the constraint, so directly return 
            return
        
        # Recursive case
        # Exclude choice
        helper(slate, index+1, arr)
        # Include choice
        slate.append(arr[index])
        helper(slate, index+1, arr)
        slate.pop()
        
    helper([],0,arr)
    return result
    
        
