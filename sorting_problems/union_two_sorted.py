# Online Python-3 Compiler (Interpreter)
def union_sorted_arr(A, B):
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
        # if smaller element, add it to the result as output should be in
        #sorted order
            result.append(A[i])
            i+=1
        else:
            result.append(B[j])
            j+=1
            
    # Gather if any pointer spills
    while i<m:
        result.append(A[i])
        i+=1
    while j<n:
        result.append(B[j])
        j+=1
    return result

#I/P:
#A=[1,2,3,8,9]
#B=[1,5,9]
#print(union_sorted_arr(A,B))
#O/P: [1,2,3,5,8,9]
