
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]  # return indices in any order
            
nums = [1, 2, 3, 4, 5, 6,]            
target = 10
print(f"{two_sum(nums, target)}")