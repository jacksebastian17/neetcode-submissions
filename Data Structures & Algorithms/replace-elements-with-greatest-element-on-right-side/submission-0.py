class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        z = len(arr) - 1
        maxNum = 0
        while z >= 0:
            if z == len(arr) - 1:
                maxNum = arr[z]
                arr[z] = -1
            elif arr[z] <= maxNum:
                arr[z] = maxNum
            else:
                temp = maxNum
                maxNum = arr[z]
                arr[z] = temp
            z -= 1
        return arr
