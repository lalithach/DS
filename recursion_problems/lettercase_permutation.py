# This code uses recursion. This has the similar pattern as subsets
# There are 2 choices the top level manager should make 
# 1, to change case of the character 2, to not change case
# This logic reuses the array and slate (partial solution) by adding and removing
# the elements in to the slate

def casehelper(slate, index, arr):
    if slate == "":
        slate = []
    if index == len(arr):
        # join the characters to string
        return ["".join(slate)]
    
    else:
        final_list = []
        # if the element is numeric, put as it is as no swapcase
        # would work on numbers
        if arr[index].isnumeric():
            slate.append(arr[index])
            final_list.extend(casehelper(slate, index+1, arr))
            slate.pop()
        else:
            # Swap case
            slate.append(arr[index].swapcase())
            final_list.extend(casehelper(slate, index+1, arr))
            slate.pop()
            # No Swap case - put as it is
            slate.append(arr[index])
            final_list.extend(casehelper(slate, index+1, arr))
            slate.pop()
    return final_list

def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    s = [string for string in s]
    return casehelper("",0, s)
    
print(letter_case_permutations("abc"))

#outputs: ['aB1', 'ab1', 'AB1', 'Ab1']
