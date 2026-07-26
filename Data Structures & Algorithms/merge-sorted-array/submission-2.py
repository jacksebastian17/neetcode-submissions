class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1       # last valid element in nums1
        j = n - 1       # last element in nums2
        k = m + n - 1   # last available position in nums1
        while k >= 0:
            if i < 0:
                nums1[0:n] = nums2
                break
            if j < 0:
                return
            n1 = nums1[i]
            n2 = nums2[j]
            if n1 > n2:
                nums1[k] = n1
                i -= 1
            else:
                nums1[k] = n2
                j -= 1
            k -= 1
            print(nums1)
