'''
返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b
'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        if n == 0: return []
        if n == 1: return [str(nums[0])]
        res = []
        lo = hi = 0
        i = 1
        tmp = nums[0]
        while i < n:
            flag = False
            if nums[i] == nums[i - 1] + 1: hi = i
            else: flag = True
            if flag:
                if lo != hi: res.append(str(nums[lo]) + '->' + str(nums[hi]))
                else: res.append(str(nums[lo]))
                lo = hi = i
            i += 1
        hi = n - 1
        if lo != hi: res.append(str(nums[lo]) + '->' + str(nums[hi]))
        else: res.append(str(nums[lo]))
        return res