class Solution:

    def __init__(self, nums: List[int]):
        self.N = nums
        self.origin = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.N)
        return self.N