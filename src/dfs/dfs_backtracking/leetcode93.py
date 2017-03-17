

class Solution(object):
    def restoreIpAddresses1(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(k, s, address):
            # At the k-th segment, the length of s should be between 4-k and (4-k)*3
            if not ((4-k)<=len(s)<=(4-k)*3):
                return

            # At the last segment
            if k == 3:
                if ((1<len(s)<=3 and s[0]!='0') or len(s)==1) and 0<=int(s)<= 255:
                    res.append(address[1:] + '.' + s)
                return

            for l in xrange(1, 4):
                if l>1 and s[0]=='0':
                    return
                if 0 <= int(s[:l]) <= 255:
                    dfs(k + 1, s[l:], address + '.' + s[:l])
        res = []
        dfs(0,s,'')
        return res

    def restoreIpAddresses(self, s):

        def dfs(sub, s, ip):
            if sub == 4 and len(s) == 0:
                ips.append(ip[1:])
                return
            # check if the length of the string exceeds the maximum length of a ip address
            if len(s) > (4 - sub) * 3:
                return

            for l in xrange(1, min(4, len(s)+1)):
                c = s[:l]
                if l > 1 and c[0] == '0':
                    return
                if 0 <= int(c) <= 255:
                    dfs(sub + 1, s[l:], ip + '.' + c)

        ips = []
        n = len(s)
        # check the format: x.x.x.x or xxx.xxx.xxx.xxx
        # (x in [0,9], xxx<=255, 0x or 0xx is invalid)
        if n < 4 or n > 12:
            return ips

        dfs(0, s, "")
        return ips


if __name__ == "__main__":
    s = "0000"
    res = Solution().restoreIpAddresses(s)
    print res
