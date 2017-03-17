
class Solution(object):
    """
    @ Google, Airbnb, Facebook, Twitter, Snapchat, Pocket Gems
    
    There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
    You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this
    new language. Derive the order of letters in this language.

    For example, given the following words in dictionary, ["wrt","wrf","er","ett","rftt"],
    The correct order is: "wertf".

    Note:
    You may assume all letters are in lowercase.
    If the order is invalid, return an empty string.
    There may be multiple valid order of letters, return any one of them is fine.
    """
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def add_node(adj_dict, char):
            if not adj_dict.has_key(char):
                adj_dict[char] = []
                indegrees[char] = 0

        # corner cases
        if words is None: return ""
        if len(words) == 1: return words[0]

        n = len(words)
        # store edges
        adj_dict = {}
        # save the indegrees of each character
        indegrees = {}
        # build graph
        for i in xrange(1, n):
            pre_word = words[i - 1]
            cur_word = words[i]
            for j in xrange(min(len(pre_word), len(cur_word))):
                add_node(adj_dict, pre_word[j])
                add_node(adj_dict, cur_word[j])
                if pre_word[j] != cur_word[j]:
                    adj_dict[pre_word[j]].append(cur_word[j])
                    indegrees[cur_word[j]] += 1

                    for k in xrange(j + 1, len(pre_word)):
                        add_node(adj_dict, pre_word[k])
                    for k in xrange(j + 1, len(cur_word)):
                        add_node(adj_dict, cur_word[k])
                    break

        # save the characters with zero indegree
        queue = []
        for key, value in indegrees.items():
            if value == 0:
                queue.append(key)
        # toposort
        res = ''
        while len(queue) > 0:
            char = queue.pop(0)
            res += char
            for c in adj_dict[char]:
                indegrees[c] -= 1
                if indegrees[c] == 0:
                    queue.append(c)
        if len(res) == len(adj_dict):
            return res
        else:
            return ""


if __name__ == "__main__":
    words = ["vlxpwiqbsg","cpwqwqcd"]
    res = Solution().alienOrder(words)
    print res