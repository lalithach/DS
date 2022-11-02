import random

def lomuto_2way(numbers, start, end):
    orange = start
    for green in range(start+1, end+1):
        if numbers[green] < numbers[start]:
            orange+=1
            numbers[green], numbers[orange] = numbers[orange], numbers[green]
    return orange

def helper(numbers, start, end, index):
    # Leaf worker
    if start == end:  # No greater condition is needed, as empty partition doesnt exist in this case
        return
    # arbitary worker
    # Get a random index and swap it with pivot to not go to O(n^2) in worst case
    randind = random.randint(start,end)
    numbers[start], numbers[randind] = numbers[randind], numbers[start]
    orange = lomuto_2way(numbers, start, end)
    #swap pivot element after lomuto partitioning
    numbers[orange],numbers[start] = numbers[start],numbers[orange]
    # concentrate only on partition that has index
    if orange == index:  #best case
        return
    elif orange > index:
        helper(numbers,start, orange-1, index)
    else: # orange < index
        helper(numbers, orange+1, end, index)
    
def kth_largest_in_an_array(numbers, k):
    """
    Args:
     numbers(list_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    helper(numbers, 0, len(numbers)-1, len(numbers)-k) # As kth largest lies in n-k index
    return numbers[len(numbers)-k]

#Complexity: O(n)
#Input
#{
#"numbers": [5, 1, 10, 3, 2],
#"k": 2
#}

#output: 5
