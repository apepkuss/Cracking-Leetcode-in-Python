
class Solution(object):
    # tortoise and hare principle
    def findDuplicate1(self, nums): # RT: O(n)
        # The "tortoise and hare" step.  We start at the end of the array and try
        # to find an intersection point in the cycle.
        slow = 0
        fast = 0

        # Keep advancing 'slow' by one step and 'fast' by two steps until they
        # meet inside the loop.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Start up another pointer from the end of the array and march it forward
        # until it hits the pointer inside the array.
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]

            # If the two hit, the intersection index is the duplicate element.
            if slow == finder:
                return slow
