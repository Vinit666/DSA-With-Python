class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = [-1] * len(nums2)
        stack = []
        d = dict()
        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums2[i]:
                stack.pop()
            if len(stack) != 0:
                result[i] = stack[-1]
            stack.append(nums2[i])

            # adding values in dictionary
            d[nums2[i]] = result[i]

        ans = []
        for i in range(len(nums1)):
            ans.append(d[nums1[i]])
        return ans


s1 = Solution()
print(s1.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(s1.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))
