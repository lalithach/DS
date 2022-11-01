# 3way lomuto partitioning
def lomuto(A, start, end):
	orange=start
	blue = start
	pivot = A[start]
	for green in range(start+1, end+1) :
		if A[green] == pivot:
			if blue==0:
				blue = orange + 1
			else:
				blue+=1
			A[blue], A[green] = A[green], A[blue]
		elif A[green] > pivot:
			orange+=1
			A[green],A[orange]=A[orange],A[green]
			if A[green] == pivot:
				blue +=1
				A[blue], A[green] = A[green], A[blue]
		else:
			pass
		#print(f"Index: {green}: {A}")
	return orange, blue

def helper(A, start, end):
  #leaf worker
	if start>=end:
		return
	#arbitary worker
	orange, blue = lomuto(A, start, end)
	A[orange], A[start] = A[start], A[orange]
	#print(A)
	helper(A, start, orange-1)
	helper(A, blue+1, end)

def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    helper(balls,0,len(balls)-1)
    return balls

 
#I/P:
#{
#"balls": ["G", "B", "G", "G", "R", "B", "R", "G"]
#}
#O/P:
#["R", "R", "G", "G", "G", "G", "B", "B"]
