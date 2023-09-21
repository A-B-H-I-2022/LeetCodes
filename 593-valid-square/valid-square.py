class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1 == p2 == p3 == p4:
            return False
        def square(a,b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2
        ans = [square(p1,p2),square(p1,p3),square(p1,p4),square(p2,p3),square(p2,p4),square(p3,p4)]
        ans.sort()
        if ans[0]==ans[1]==ans[2]==ans[3]:
            if ans[4]==ans[5]:
                return True
        return False
        
        