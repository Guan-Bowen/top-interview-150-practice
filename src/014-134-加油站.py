'''
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        l = len(cost)
        sumGas = sumCost = 0
        for i in range(l):
            sumGas += gas[i]
            sumCost += cost[i]
        if sumCost > sumGas: return -1

        startPoint = 0
        while True:
            left = gas[startPoint] - cost[startPoint]
            flag = True
            for i in range(l):
                if left < 0: 
                    flag = False
                    startPoint = (startPoint + i + 1) % l
                    break
                left += gas[(startPoint + i + 1) % l] - cost[(startPoint + i + 1) % l]
            if flag: return startPoint

class Solution1(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        for i in range(l):
            if gas[i] < cost[i]: continue
            flag = True
            left = gas[i] - cost[i]
            pos = (i + 1) % l
            while pos != i:
                left += gas[pos] - cost[pos]
                if left < 0:
                    flag = False
                    break
                pos = (pos + 1) % l
            if not flag: continue
            else: return i
        return -1
        # Time out

