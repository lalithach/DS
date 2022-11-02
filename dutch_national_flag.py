import random
# 3way lomuto partitioning
def lomuto(A, start, end):
	orange=start
	blue = start
	pivot = A[start]
	for green in range(start+1, end+1) :  
		if A[green] == pivot:
			# When initial element after pivot is lesser, then orange zone increases. Since blue region falls after orange
			if blue==0:
				blue = orange + 1
			else:
				blue+=1
			A[blue], A[green] = A[green], A[blue]
		elif A[green] > pivot:
			orange+=1
			A[green],A[orange]=A[orange],A[green]
			# There is a chance that the swapped element above could be pivot which could disturb the order
			if A[green] == pivot:
				blue +=1
				A[blue], A[green] = A[green], A[blue]
		else:
			pass
	return orange, blue

def quickselect(A, start, end):
  	#leaf worker
	if start>=end:
		return
	#arbitary worker
	# swap pivot with random index no, to avoid worst case
	randind = random.randint(start,end)
	A[start], A[randind] = A[randind], A[start]
	orange, blue = lomuto(A, start, end)
	A[orange], A[start] = A[start], A[orange]

	quickselect(A, start, orange-1)
	quickselect(A, blue+1, end)

def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    quickselect(balls,0,len(balls)-1)
    return balls

 
#I/P:
#{
#"balls": ["G", "B", "G", "G", "R", "B", "R", "G"]
#}
#O/P:
#["R", "R", "G", "G", "G", "G", "B", "B"]
