# -*- coding: utf-8 -*-
"""
Created on Mon May 31 18:52:06 2021

@author: lalithac
Insertion Sort in ascending order

Start from 1 to len of list
compare with predecessor
If the key element is smaller than its predecessor, 
compare it to the elements before. Move the greater elements one position up to make space for the swapped element.
"""


def insertionSort(arr):
    # start from 1 to len(list)
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        # compare with predecessor 
        while j >=0 and key < arr[j]:
            # Move the greater elements one position up to make space for the swapped element
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr
        
arr = [5, 2, 1, 3, 4, 6, 2, 8, 0]

print(insertionSort(arr))
