# Online Python-3 Compiler (Interpreter)

# This code looks similar to combine phase in merge sort with few updates.
def intersect_sorted_arr(A, B):
    m = len(A)
    n = len(B)
    i,j=0,0
    result = []
    while i<m and j<n:
        if A[i] == B[j]:
            result.append(A[i])
            i+=1
            j+=1
        elif A[i]<B[j]:
        # if smaller element, move further such that equal element may be found
            i+=1
        else:
            j+=1
    return result

#A=[1,2,3,8,9]
#B=[1,5,9]
#print(intersect_sorted_arr(A,B))
#O/P:[1,9]
