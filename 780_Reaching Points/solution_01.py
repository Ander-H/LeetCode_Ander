class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            elif tx > sx and ty == sy:
                if tx <= ty:
                    return False
                else:
                    return (tx - sx) % ty == 0
            elif tx == sx and ty > sy:
                if tx >= ty:
                    return False
                else:
                    return (ty - sy) % tx == 0
            else:
                if tx >= ty:
                    tx -= ty
                else:
                    ty -= tx
        return False
