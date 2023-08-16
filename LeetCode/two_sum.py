class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}
        for i in range(len(nums)):
            print()
            print(target-nums[i])
            if indices.get(target-nums[i]):
                print(target-nums[i])
                return (indices[target-nums[i]],i)
            print("Arrived")
            indices[nums[i]] = i
            print(indices.get(i))

solution = Solution()

print(solution.twoSum([2,3,1,11,7],9))
