
class Solution(object):
    """
    @ Amazon

    Given an index k, return the kth row of the Pascal's triangle.

    For example, given k = 3,
    Return [1,3,3,1].

    Note:
    Could you optimize your algorithm to use only O(k) extra space?
    """
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pre = [1]
        if rowIndex <= 0:
            return pre

        for row in range(1, rowIndex + 1):
            curr = []
            for col in range(0, row + 1):
                if col == 0 or col == row:
                    curr.append(1)
                else:
                    curr.append(pre[col - 1] + pre[col])
            pre = curr

        return pre