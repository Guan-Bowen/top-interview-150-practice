'''
现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。

例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
'''
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        q = []
        degs = [0] * numCourses
        d = dict()
        for tar, pre in prerequisites: 
            degs[tar] += 1
            if pre in d: (d[pre]).append(tar)
            else: d[pre] = [tar]
        for i in range(numCourses):
            if degs[i] == 0: q.append(i)
            if i not in d: d[i] = []
        cnt = 0
        res = []
        while q:
            courseId = q.pop(0)
            res.append(courseId)
            cnt += 1
            for tar in d[courseId]:
                degs[tar] -= 1
                if degs[tar] == 0: q.append(tar)
        if cnt == numCourses: return res
        else: return []