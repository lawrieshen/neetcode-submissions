class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total  = len(nums1) + len(nums2)
        half  = total // 2

        if len(nums1) > len(nums2): # make A the shorter one
            A, B = B, A

        left, right = 0, len(A) - 1
        
        while True:
            i = (left + right) // 2 # mid index for A
            j = half - (i + 1) - 1 # mid index for B

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            # check if the partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # if odd: meidan is the the min of Aright and Bright
                if total % 2 == 1:
                    return min(Aright, Bright)
                # if even: median is the average of max of left/right and min of left/right
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # element in A needs to be moved out
                right = i - 1
            elif Bleft > Aright:
                # element in B needs to be moved out
                left = i + 1