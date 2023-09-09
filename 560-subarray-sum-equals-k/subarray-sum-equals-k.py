class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # count = 0
        # dic = {0 : 1}
        # summ = 0
        # for i in nums:
        #     summ += i
        #     if summ - k in dic:
        #         count += dic[summ-k]
        #     if summ in dic:
        #         dic[summ] += 1
        #     else:
        #         dic[summ] = 1
        # return count

        anscount = 0
        prefixsum = 0
        
        d ={0:1}
        
        for i in nums:
            
            prefixsum = prefixsum + i
            
            if prefixsum - k in d:
                anscount = anscount + d[prefixsum - k]
                #print(d)
                #print(k)
                #print(prefixsum)
                #print(prefixsum-k)
                #print(d[prefixsum-k])
                #print(d[0])
            if prefixsum not in d:
                d[prefixsum] = 1
            else:
                d[prefixsum] = d[prefixsum] + 1                                                
        
        return anscount
        