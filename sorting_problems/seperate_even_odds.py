
def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    # Similar to Lomuto 2 way partitioning
    even_ptr = -1
    for odd_ptr, number in enumerate(numbers):
        if number%2 == 0:
            even_ptr+=1
            numbers[odd_ptr], numbers[even_ptr] = numbers[even_ptr], numbers[odd_ptr]
    return numbers
  
#Given an array of numbers, rearrange them in-place so that even numbers appear before odd ones.
#Example
#{
#"numbers": [1, 2, 3, 4]
#}
#Output:
#[4, 2, 3, 1] 
#order of even and odd numbers can be in any order
