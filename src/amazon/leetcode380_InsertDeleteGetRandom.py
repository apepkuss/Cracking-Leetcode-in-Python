
class RandomizedSet(object):
    """
    @ Google, Uber, Twitter, Amazon, Yelp, Pocket Gems
    
    Design a data structure that supports all following operations in average O(1) time.

    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements. Each element must have 
               the same probability of being returned.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.adict = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.adict:
            self.data.append(val)
            idx = len(self.data)-1
            self.adict[val] = idx
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.adict:
            idx = self.adict[val]
            self.adict.pop(val)
            for i in range(idx+1, len(self.data)):
                key = self.data[i]
                self.adict[key] -= 1
            self.data.pop(idx)
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        idx = random.randint(0, len(self.data)-1)
        return self.data[idx]