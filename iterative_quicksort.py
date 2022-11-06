import random

def lomuto_3way(arr, start, end):
    # To prevent the worst case, pick a random index
    # and swap with start 
    randind = random.randint(start, end)
    arr[start], arr[randind] = arr[randind], arr[start]
    orange = start
    blue = start
    # Make start index as pivot
    pivot = arr[start]
    for green in range(start+1, end+1):
        if (arr[green] == pivot):
        # When initial element after pivot is lesser, then orange zone increases.
        # Since blue region falls after orange, need to start blue zone after orange
            if blue == start:
                blue = orange + 1
            else:
                blue+=1
            arr[green], arr[blue] = arr[blue], arr[green]
            
        elif (arr[green] < pivot):
            orange+=1
            arr[green], arr[orange] = arr[orange], arr[green]
            if arr[green] == pivot:
            # There is a chance that the swapped element above could be pivot which could disturb             # the order
                blue+=1
                arr[green], arr[blue] = arr[blue], arr[green]
        else:
            pass
            
    # Swap the pivot to its exact position 
    arr[start], arr[orange] = arr[orange], arr[start]
    return orange, blue
    
    
def quicksort(arr, start, end):
    size = end-start +1 
    stack = []
    # Initially add first and last indices to the stack
    stack.append((start, end))
    while stack:
        start, end = stack.pop()
        orange, blue = lomuto_3way(arr, start, end)
        # Append left subarray indices
        if orange-1 > start:
            stack.append((start, orange-1))
            
        # Exclude elements equal to pivot
        if blue!=0:
            # Append right subarray indices
            if blue+1 < end:
                stack.append((blue+1, end))
        else:
            if orange+1 < end:
                stack.append((orange+1, end))
        
def iterativeQuicksort(arr):
    quicksort(arr,0, len(arr)-1)
    return arr
    

arr=[1,2,2,5,7,7,8,1,1,1,9]

print(iterativeQuicksort(arr))
