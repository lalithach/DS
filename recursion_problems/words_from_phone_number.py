#Given a seven-digit phone number, return all the character combinations that can be generated according to the following mapping:
#Return the combinations in the lexicographical order.
#
#Example One
#{
#"phone_number": "1234567"
#}
#Output:
#
#[
#"adgjmp",
#"adgjmq",
#"adgjmr",
#"adgjms",
#"adgjnp",
#...
#"cfilns",
#"cfilop",
#"cfiloq",
#"cfilor",
#"cfilos"
#]


dict_chars = {
    "1": [],
    "2": ["a","b","c"],
    "3": ["d","e","f"],
    "4": ["g","h","i"],
    "5": ["j","k","l"],
    "6": ["m","n","o"],
    "7": ["p","q","r","s"],
    "8": ["t","u","v"],
    "9": ["w","x","y","z"],
    "0": []
}

def get_words_from_phone_number(phone_number):
    """
    Args:
     phone_number(str)
    Returns:
     list_str
    """
    result = []
    def helper(slate, index, arr):
        if index == len(arr):
            result.append("".join(slate))
            return
        else:
            # Since 1 and 0 dont represent any chars, send the slate
            # as it is and move to next number
            if arr[index] == "1" or arr[index] == "0":
                helper(slate, index+1, arr)
            else:
                # Add possible choices for a number based on dict_chars
                for value in dict_chars[arr[index]]:
                    slate.append(value)
                    helper(slate, index+1, arr)
                    slate.pop()
                    
    helper([],0,phone_number)
    return result
    
print(get_words_from_phone_number("4230"))

#Outputs:['gad', 'gae', 'gaf', 'gbd', 'gbe', 'gbf', 'gcd', 'gce', 'gcf', 'had', 'hae', 'haf', 'hbd', 'hbe', 'hbf', 'hcd', 'hce', 'hcf', 'iad', 'iae', 'iaf', 'ibd', 'ibe', 'ibf', 'icd', 'ice', 'icf']
