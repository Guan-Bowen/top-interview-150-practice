'''
中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder 对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
'''
class MedianFinder(object):

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 不妨使 len(minHeap) >= len(maxHeap)，长度为奇数时，返回 minHeap[0]
        # (1) 长度相等，元素 push maxHeap，进而 pop，得到一个大顶堆的最大值
        #     将这个最大值 push minHeap，minHeap 中的值都大于 maxHeap，最接近的是 minHeap[0]
        # (2) 长度不相等，元素 push minHeap，进而 pop，得到一个小顶堆的最小值
        #     将这个最小值 push maxHeap，maxHeap 中的值都小于 minHeap，最接近的是 maxHeap[0]
        # (3) 上述的操作并未充分排序，但它保证了中间两个数字可以产生中位数
        #     产生中位数的时间复杂度 O(n) = 1，add 操作整堆的时间复杂度 O(n) = logn
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.maxHeap, -num)
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        else:
            heapq.heappush(self.minHeap, num)
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))



    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return self.minHeap[0] * 1.0
# Timeout
class MedianFinder1(object):

    def __init__(self):
        self.sortedList = []
        self.sz = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.sz == 0:
            self.sortedList.append(num)
            self.sz = 1
            return
        lo, hi, idx = 0, self.sz - 1, -1
        while lo < hi:
            curr = (lo + hi) // 2
            if self.sortedList[curr] == num:
                idx = curr
                break
            elif self.sortedList[curr] < num: 
                if lo == curr: lo += 1
                else: lo = curr
            else: hi = curr
        if idx == -1:
            if self.sortedList[lo] >= num: idx = lo
            else: idx = lo + 1
        self.sortedList = self.sortedList[:idx] + [num] + self.sortedList[idx:]
        self.sz += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.sz % 2: return self.sortedList[self.sz // 2] * 1.0
        else: return (self.sortedList[self.sz // 2 - 1] + self.sortedList[self.sz // 2]) / 2.0




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()