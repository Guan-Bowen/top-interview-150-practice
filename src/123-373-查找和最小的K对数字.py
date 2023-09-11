'''
给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。

定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。

请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
'''
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(nums1), len(nums2)
        res = []
        heap = []
        # 入堆元素：两数之和（排序依据） & 数对 & 数对索引
        # 该堆需要保证：在堆顶元素出堆时，经过适当入堆操作后，能保证存在下次的出堆元素
        heapq.heappush(heap, (nums1[0] + nums2[0], [nums1[0], nums2[0]], [0, 0]))
        while heap and k:
            _, pair, [i, j] = heapq.heappop(heap)
            res.append(pair)
            k -= 1
            # (1) 如果出堆的元素位于首行，将该行下一个（右侧）元素入堆
            # (2) 将出堆元素下一行（下方）的元素入堆
            # 上述操作保证了下次出堆元素的存在，原理是：
            # a. 对 sum[i,j] 而言，两个索引都小于等于（不同时等于）的元素，和值一定更小
            # b. 出堆元素右 / 下侧的入堆，代表对相邻索引和 +1 元素的入堆
            # c. 这样保证了：已经出堆的元素引入了边界上所有索引和“最极限”的元素
            if i == 0 and j + 1 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], [nums1[i], nums2[j + 1]], [i, j + 1]))
            if i + 1 < m:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], [nums1[i + 1], nums2[j]], [i + 1, j]))
        return res