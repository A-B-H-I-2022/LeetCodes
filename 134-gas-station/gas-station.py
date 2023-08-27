class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalgain = 0
        currentgain = 0
        answer = 0
        for i in range(len(gas)):
            totalgain += gas[i] - cost[i]
            currentgain += gas[i] - cost[i]
            if currentgain < 0:
                currentgain = 0
                answer = i + 1
        return answer if totalgain >= 0 else -1
        






















        
        # start = 0
        # end = 0 
        # sum = 0
        # length = 0
        # while start<len(gas) and length < len(gas):
        #     sum += gas[end]-cost[end]
        #     length +=1
        #     while start<len(gas) and sum < 0:
        #         sum -= gas[start] - cost[start]
        #         start +=1
        #         length-=1
        #     end+=1
        #     end = end % len(gas)
        # if length == len(gas):
        #     return start
        # return -1
        