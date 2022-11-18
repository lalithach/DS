#Find all palindromic decompositions of a given string s.

#A palindromic decomposition of string is a decomposition of the string into substrings, such that all those substrings are valid palindromes.
#{
#"s": "abracadabra"
#}
#Output:

#["a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a", "a|b|r|a|c|a|d|a|b|r|a"]
#Order of characters in a decomposition must remain the same as in the given string. For example, for s = "ab", return ["a|b"] and not ["b|a"].

def is_palindrome(s):
# check if a string is palindrome or not
    left = 0
    right = len(s)-1
    
    while left<=right:
        if (s[left] == s[right]):
            left+=1
            right-=1
        else:
            return False
    return True

def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    result = []
    # convert string to char array
    arr = [char for char in s]
    # Adding helper function such that result is accessible
    def helper(slate, index, arr):
        if index == len(arr):
            # The leaf node has all possible combinations
            # [ab|a], [aba], [a|ba], [a|b|a]
            # Split by | and check if every substring is palindrome
            # Append all slate content to result only if all substrings
            # are palindromes
            slate = "".join(slate).split("|")
            if all(is_palindrome(item) for item in slate):
                result.append("|".join(slate))
            return
        else:
            # Join case
            slate.append(arr[index])
            helper(slate, index+1, arr)
            slate.pop()
            
            # Add | case
            slate.append("|")
            slate.append(arr[index])
            helper(slate, index+1, arr)
            slate.pop()
            slate.pop()
            
    # Starting with 1st index, as for non-join case,
    # we dont want | to be in the start of the string
    helper([arr[0]],1,arr)
    return result


print(generate_palindromic_decompositions("aba"))

#Outputs:
#['aba', 'a|b|a']
