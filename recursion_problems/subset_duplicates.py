#Given a string that might contain duplicate characters, find all the possible distinct subsets of that string.
#Example One
#{
#"s": "aab"
#}
#Output:
#
#["", "a", "aa", "aab", "ab", "b"]

def get_distinct_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    arr = [char for char in s]
    arr.sort()
    result = []
    def helper(slate, arr, index):
        # Leaf node
        if index == len(arr):
            result.append("".join(slate))
            return

        # Internal node workers
        # Get the count of a specific element, thats why sort all
        # the elements first
        count = 0
        for pick in range(index, len(arr)):
            if arr[index] == arr[pick]:
                count+=1
        # Exclude choice
        # subordinate should get the element after all duplicates
        # So, index+count
        helper(slate, arr, index+count)
        
        # Include choice
        # Iterate over all duplicate choices
        for pick in range(0, count):
            slate.append(arr[index])
            helper(slate, arr, index+count)
            # pop is skipped here, as the other nodes in same level
            # should have the previous choice appended
        
        # pop all of them while returning back to higher manager
        for pick in range(0, count):
            slate.pop()

    helper([],arr, 0)
    return result
