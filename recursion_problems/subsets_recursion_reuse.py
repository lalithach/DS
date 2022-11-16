# This code uses recursion and does not create new slate and subarray while
# recursive calls. Instead, it reuses the same slate and the main array by
# adding and popping elements to slate

# This is for distinct elements in the array

def printsubsets(s):
    final_list = []
    def subhelper(slate, index, arr):
        if slate == "":
            slate = []
        # When index reaches length of array, its the base case
        # as No more elements in the list
        if index == len(arr):
            final_list.append(slate[:])
        else:
            # exclude choice
            subhelper(slate, index+1, arr)
            # include choice
            slate.append(arr[index])
            subhelper(slate, index+1, arr)
            # Removing the added element as the slate should be reused
            slate.pop()
            
    subhelper("",0,s)
    
    return final_list

print(printsubsets([1,2,3]))

# Outputs:
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
