def phelper(slate, arr):
    # slate represents the partial solution that carried further to subordinates
    # arr is the list of remaining choices for the subordinates
    if slate == "":
        slate = []
    if len(arr) == 0:
        return [slate]
    else:
        output = []
        # delegation based on the left over no of choices
        for i in range(0, len(arr)):
            # slate+arr[i] represents making a choice by top level manager
            # arr[:i]+arr[i+1:] - excluding arr[i] and sending all other remaining choices
            output.extend(phelper(slate+[arr[i]], arr[:i]+arr[i+1:]))
    return output        

def get_permutations(arr):
    return phelper("", arr)
  
print(get_permutations([1,2,3]))

#Ouputs:[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
