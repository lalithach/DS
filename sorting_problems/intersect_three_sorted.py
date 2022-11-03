
def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    i,j,k=0,0,0
    result = []
    
    # Return [-1] when one of the arrays is empty
    if len(arr1) == 0 or len(arr2) == 0 or len(arr3) == 0:
        return [-1]
    while i<len(arr1) and j<len(arr2) and k<len(arr3):
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            result.append(arr1[i])
            i+=1
            j+=1
            k+=1
        elif arr1[i]<arr2[j]:
        # if smaller element, move further such that equal element may be found
            i+=1
        elif arr2[j]<arr3[k]:
            j+=1
        else:
            k+=1
            
    # return [-1] when no intersection elements are found        
    if len(result) == 0:
        result.append(-1)
        
    return result

#I/P:
#[5,6]
#[1,5,6]
#[1,2,3,4,5]
#O/P:[5]
