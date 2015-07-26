import sys, os, re

f = open('QuickSort.txt', 'r')
# f = open('test', 'r')
lines = f.readlines()
lst = []
for i in lines:
    lst.append(int(i.strip()))

total = 0
def partition(arr):
    global total
    total += len(arr)-1
    ### choose the first as the pivot
    p = arr[0]


    # ####choose the last as the pivot
    # p = arr[len(arr)-1]
    # arr[len(arr)-1] = arr[0]
    # arr[0] = p


    # ### choose median
    # first = arr[0]
    # last = arr[len(arr)-1]
    # if len(arr)%2==0:
    #     middle = arr[len(arr)/2-1]
    #     index = len(arr)/2-1
    # else:
    #     middle = arr[int(len(arr)/2)]
    #     index = int(len(arr)/2)
    # if first == sorted([first, middle, last])[1]:
    #     p = first
    #     index = 0
    # if last == sorted([first, middle, last])[1]:
    #     p = last
    #     index = len(arr)-1
    # if middle == sorted([first, middle, last])[1]:
    #     p = middle
    
    # arr[index] = arr[0]
    # arr[0] = p



    
    i = 1
    for j in xrange(i, len(arr)):
        if arr[j]<p:
            inter = arr[i]
            arr[i] = arr[j]
            arr[j] = inter
            i +=1
    inter = arr[0]
    arr[0] = arr[i-1]
    arr[i-1] = inter
    return i-1

    
def qs(arr):
    global total
    if len(arr) == 1:
        return
    else:
        # p = arr[0]
        i = partition(arr)
        if i>0:
            qs(arr[0:i])
            # total += len(arr[0:i+1])-1
        if len(arr)>i+1:
            qs(arr[i+1:len(arr)])
            # total += len(arr[i+1:len(arr)])-1



qs(lst)
print total


# total = 0
# def quickSort(alist):
#     quickSortHelper(alist,0,len(alist)-1)

# def quickSortHelper(alist,first,last):
#     global total 
#     if first<last:
#         total += len(alist)-1
#         splitpoint = partition(alist,first,last)

#         quickSortHelper(alist,first,splitpoint-1)
#         quickSortHelper(alist,splitpoint+1,last)


# def partition(alist,first,last):
#     pivotvalue = alist[first]

#     leftmark = first+1
#     rightmark = last

#     done = False
#     while not done:

#         while leftmark <= rightmark and \
#                   alist[leftmark] <= pivotvalue:
#             leftmark = leftmark + 1


#         while alist[rightmark] >= pivotvalue and \
#                   rightmark >= leftmark:
#             rightmark = rightmark -1

#         if rightmark < leftmark:
#             done = True
#         else:
#             temp = alist[leftmark]
#             alist[leftmark] = alist[rightmark]
#             alist[rightmark] = temp

#     temp = alist[first]
#     alist[first] = alist[rightmark]
#     alist[rightmark] = temp


#     return rightmark

# # alist = [54,26,93,17,77,31,44,55,20]
# quickSort(lst)
# # print(alist)
# print total
