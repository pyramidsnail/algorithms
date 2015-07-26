import sys, os, re

# f = open('QuickSort.txt', 'r')
f = open('test', 'r')

lines = f.readlines()
lst = []
for i in lines:
    lst.append(int(i.strip()))


def partition(arr):
    p = arr[0]
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

    
def qs(arr, total):
    if len(arr) == 1:
        return total
    else:
        # p = arr[0]
        i = partition(arr)
        total += len(arr)
        qs(arr[0:i+1], total)
        qs(arr[i+1:len(arr)], total)


total = 0
print qs(lst, total)


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
