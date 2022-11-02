
def can_attend_all_meetings(intervals):
    """
    Args:
     intervals(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    # sort it first so that, meeting order can be compared easily
    intervals.sort() # O(nlogn)
    last_end = -1
    # Intent is to check the first meeting end time with second meeting start time
    for start, end in intervals:
        if last_end <= start:
            last_end = end  # proceed to next meeting
        else:
            return 0  # cant attend
    return 1 

#I/P:
#{
#"intervals": [[1, 5], [5, 8], [10, 15]]
#}
#O/P: 1
