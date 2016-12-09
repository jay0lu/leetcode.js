# https://leetcode.com/problems/median-of-two-sorted-arrays/

# using merge sort
def mergeSort(list):
    result = []
    if len(list) < 2:
        return list
    mid = int(len(list)/2)
    a = mergeSort(list[:mid])
    b = mergeSort(list[mid:])
    while (len(a) > 0) or (len(b) > 0):
        if len(a) > 0 and len(b)>0:
            if a[0] > b[0]:
                result.append(b[0])
                b.pop(0)
            else:
                result.append(a[0])
                a.pop(0)
        elif len(b) > 0:
            for i in b:
                result.append(i)
                b.pop(0)
        else:
            for i in a:
                result.append(i)
                a.pop(0)
    return result


class Solution(object):
    pass

list = [1,2,3,5,6,7,8,9,0,12,13,15,36,38,49,59]
solution = Solution()
print(mergeSort(list))
