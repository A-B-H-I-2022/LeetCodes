class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ans = 0
        num = [i for i in range(1,27)]
        lis = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        map = dict(zip(lis,num))
        print(map)
        for j in columnTitle:
            ans = ans*26 + map[j]
        return ans
        
        