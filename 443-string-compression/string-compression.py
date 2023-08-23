class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i,answer = 0,0
        while i < len(chars):
            a = chars[i]
            count = 0
            while i < len(chars) and chars[i] == a:
                count += 1
                i += 1
            chars[answer] = a
            answer += 1
            if count > 1:
                for j in str(count):
                    chars[answer] = j
                    answer += 1
        return answer