class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) == 0:
            return ['']

        res = ['']
        for ch in S:
            tmp = []
            for i in range(len(res)):
                if ch.isdigit():
                    tmp.append(res[i] + ch)
                else:
                    tmp.append(res[i] + ch.lower())
                    tmp.append(res[i] + ch.upper())
            res = tmp
        return res
