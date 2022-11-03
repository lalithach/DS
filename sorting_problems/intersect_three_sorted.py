# Online Python-3 Compiler (Interpreter)
def intersect_3sorted_arr(A, B,C):
    m = len(A)
    n = len(B)
    o = len(C)
    i,j,k=0,0,0
    result = []
    while i<m and j<n and k<o:
        if A[i] == B[j] and B[j] == C[k]:
            result.append(A[i])
            i+=1
            j+=1
            k+=1
        elif A[i]<B[j]:
        # if smaller element, move further such that equal element may be found
            i+=1
        elif B[j]<C[k]:
            j+=1
        else:
            k+=1
    return result

#A=[1,2,5]
#B=[5,7]
#C=[1,3,4,5]
#print(intersect_3sorted_arr(A,B,C))
#O/P:[5]
