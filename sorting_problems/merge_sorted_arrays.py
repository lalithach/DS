
def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    first_ptr = len(first) - 1
    zero_ptr = len(second) - 1
    second_ptr = len(second) - len(first) -1
    
    while first_ptr >=0 and second_ptr >=0:
        # Place the largest element into the last and increment the zero section
        if first[first_ptr] > second[second_ptr]:
            second[zero_ptr] = first[first_ptr]
            first_ptr-=1
        else:
            second[zero_ptr] = second[second_ptr]
            second_ptr-=1
        zero_ptr-=1
        
    # Below should be done for only first array because if second array
    #elements are remaining, they neednt be rearranged as the array is already sorted
    while first_ptr >=0: 
        second[zero_ptr] = first[first_ptr]
        first_ptr-=1
        zero_ptr-=1
    
    return second

#I/p:
#Given second array is of size 2n where n is the size of first array 
#{
#"first": [1, 3, 5],
#"second": [2, 4, 6, 0, 0, 0]
#}
#O/p:
#[1, 2, 3, 4, 5, 6]
