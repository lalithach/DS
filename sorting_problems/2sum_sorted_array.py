
def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    start = 0
    end = len(numbers)-1
    while start < end:
        compliment = target - numbers[start]
        if compliment == numbers[end]:
            return [start, end]
        elif compliment < numbers[end]:
            end = end -1
        else: # compliment > numbers[end]
            start = start+1 # not found a correct pair so move further            
    return [-1, -1] # when nothing is returned, just return -1


#Problem: Output the indices of elements that contribute to target sum.
#Can output any one pair if multiple are found.
#I/P:
#{
#"numbers": [1, 2, 3, 5, 10],
#"target": 7
#}
#O/p:
#[1,3]
