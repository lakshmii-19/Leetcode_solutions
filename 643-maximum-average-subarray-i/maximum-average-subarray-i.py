class Solution(object):
    def findMaxAverage(self, nums, k):
        currSum=0
        for i in range(k):
            currSum += nums[i]
        maxSum=currSum
        for i in range(k, len(nums)):
            currSum += nums[i]
            currSum -= nums[i-k]
            maxSum=max(maxSum,currSum)
        return float(maxSum)/k

        