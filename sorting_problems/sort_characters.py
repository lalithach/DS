import random
    
def sort_array(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    
    # Since its characters and are limited (0 to 127), counting sort can be used
    res = []
    frequency = {}
    for char in arr:
        if ord(char) in frequency:
            frequency[ord(char)]+=1
        else:
            frequency[ord(char)]=1
    
    for i in range(0, 128):
        number = frequency.get(i, 0)
        if number !=0:
            char = chr(i)
            res.extend(number*[char])
    return res

# I/p:
#arr=["a", "s", "d", "f", "g", "*", "&", "!", "z", "y"]
#O/P:
#["!", "&", "*", "a", "d", "f", "g", "s", "y", "z"]
