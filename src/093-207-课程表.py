'''
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses <= 1 or not prerequisites: return True
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
        while q:
            courseId = q.pop(0)
            cnt += 1
            for tar in d[courseId]:
                degs[tar] -= 1
                if degs[tar] == 0: q.append(tar)
        return cnt == numCourses