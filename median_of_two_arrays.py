# https://leetcode.com/problems/median-of-two-sorted-arrays/

# using merge sort
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            
    print("Merging ",alist)

    # while (len(leftHalf) > 0) or (len(rightHalf) > 0):
    #     if len(leftHalf) > 0 and len(rightHalf)>0:
    #         if leftHalf[0] > rightHalf[0]:
    #             result.append(rightHalf[0])
    #             rightHalf.pop(0)
    #         else:
    #             result.append(leftHalf[0])
    #             leftHalf.pop(0)
    #     elif len(rightHalf) > 0:
    #         for i in rightHalf:
    #             result.append(i)
    #             rightHalf.pop(0)
    #     else:
    #         for i in leftHalf:
    #             result.append(i)
    #             leftHalf.pop(0)
    # return result


class Solution(object):
    pass

list = [1,2,3,5,6,7,8,9,0,12,13,15,36,38,49,59]
solution = Solution()
print(mergeSort(list))
