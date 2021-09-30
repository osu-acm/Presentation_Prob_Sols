class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        https://leetcode.com/problems/3sum-closest/submissions/

        Story:
        Find three numbers that sum closest to target.
        Return the difference between target and the sum of the numbers.
        
        Algo:
        sort numbers
        for i loop first number
            l = i + 1
	    r = len(nums)
            iterate l++ if sum < target
            else iterate r-- if sum > target
        
        """
        
        offset = float('inf')
        
        # sort the nums array first - O(nlogn)
        nums.sort()
        closest_score = nums[0] + nums[1] + nums[2]
        
        # loop first pointer from each num in nums
        for i in range(len(nums) - 2):
            lptr = i + 1
            rptr = len(nums) - 1
            
            # decrease window from lptr to rptr until they meet
            while lptr < rptr:
                summation = nums[i] + nums[lptr] + nums[rptr]
                
                # preserve this offset
                prev_offset = offset
                
                # calculate how close we got. If it's the closest yet, then update closest_score
                offset = min(offset, abs(target - summation))
                if offset < prev_offset:
                    closest_score = summation

                # decrease window
                if summation > target:
                    rptr -= 1
                elif summation < target:
                    lptr += 1
                else:
                    # in this case we got the correct solution
                    return summation

        return closest_score
            
            
            
            
            
            
            
        
