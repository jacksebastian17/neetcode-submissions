class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = -1
        for z in range(len(arr) - 1, -1, -1):
            if arr[z] <= maxNum:
                arr[z] = maxNum
            else:
                temp = maxNum
                maxNum = arr[z]
                arr[z] = temp
        return arr
