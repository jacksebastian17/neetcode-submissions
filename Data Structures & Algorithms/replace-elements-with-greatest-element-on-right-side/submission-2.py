class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = -1
        for z in range(len(arr) - 1, -1, -1): # start at len(arr) - 1, stop BEFORE -1, decrement by 1 each step
            if arr[z] <= maxNum:
                arr[z] = maxNum
            else:
                temp = maxNum
                maxNum = arr[z]
                arr[z] = temp
        return arr
