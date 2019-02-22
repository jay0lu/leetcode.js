# https://leetcode.com/problems/median-of-two-sorted-arrays/

def mergeSort(alist):
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

        return alist

class Solution(object):
    # using merge sort
    def findMedianSortedArrays(self, nums1, nums2):
        list = nums1 + nums2
        if len(list) < 2:
            return list[0]
        else:
            mergeList = mergeSort(list)
            mid = len(mergeList)//2
            if len(mergeList) % 2 == 1:
                medianNum = mergeList[mid]
            else:
                medianNum = (mergeList[mid] + mergeList[mid-1]) / 2
            return medianNum


list = [1,2,3,5,6,7,8,9,0,12,13,15,36,38,49,59]
nums1 = [1,2]
nums2 = [3,4]
solution = Solution()
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)
# print(mergeSort(list))
