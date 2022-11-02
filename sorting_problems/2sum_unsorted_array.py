
def two_sum(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    hash_map = {} # aux space of O(n)
    # Since indices are asked, sorting is not possible here. 
    for index,number in enumerate(numbers):
        if target - number in hash_map: # checks in O(1)
            return [index, hash_map[target-number]]
        else:
            # Add that index to hash map
            hash_map[number] = index

    return [-1,-1]

#I/P:
#{
#"numbers": [5, 3, 10, 45, 1],
#"target": 6
#}
#O/P:
#[0,4]
