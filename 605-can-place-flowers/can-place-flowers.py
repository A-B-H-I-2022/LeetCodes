class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        answer = [0] + flowerbed + [0]
        count = 0
        for i in range(0,len(answer)):
            if answer[i:i+3] == [0,0,0]:
                count += 1
                answer[i+1] = 1
        if count >= n:
            return True
        else:
            return False