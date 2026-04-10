class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        num_set = set(nums)
        max_streak = 1
        for num in num_set:
            # Check if 'num' is the start of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                # Build the sequence
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                    max_streak = max(max_streak, current_streak)
        return max_streak