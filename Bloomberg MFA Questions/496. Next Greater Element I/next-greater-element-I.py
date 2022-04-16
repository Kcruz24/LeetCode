from typing import List


class Solution:
    # O(M * N) time | O(1) space
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            nums1_elem = nums1[i]
            next_idx = nums2.index(nums1_elem)
            found = False

            for j in range(next_idx + 1, len(nums2)):
                next_greater_elem = nums2[j]
                if next_greater_elem > nums1_elem:
                    found = True
                    ans.append(nums2[j])
                    break

            last_idx = len(nums2) - 1
            if next_idx == last_idx or not found:
                ans.append(-1)

        return ans


# https://leetcode.com/problems/next-greater-element-i/discuss/824654/Python-3-greater-94.64-faster.-Used-stack-and-dictionary.-Explanation-added
class Solution2:
    # O(N) time | O(N) space
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None

        mapping = {}
        result = []
        stack = []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            # if stack is not empty, then compare it's last element with nums2[i]
            while stack and nums2[i] > stack[-1]:
                # if the new element is greater than stack's top element, then add this to dictionary
                mapping[stack[-1]] = nums2[i]
                # since we found a pair for the top element, remove it.
                stack.pop()
            # add the element nums2[i] to the stack because we need to find a number greater than this
            stack.append(nums2[i])

        # if there are elements in the stack for which we didn't find a greater number, map them to -1
        for element in stack:
            mapping[element] = -1

        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])
        return result


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

    nums3 = [1, 3, 5, 2, 4]
    nums4 = [6, 5, 4, 3, 2, 1, 7]

    sol = Solution()

    print(sol.nextGreaterElement(nums1, nums2))
    print(sol.nextGreaterElement(nums3, nums4))
