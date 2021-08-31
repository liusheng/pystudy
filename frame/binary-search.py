# 查找目标
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) / 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left += mid + 1
        elif target < nums[mid]:
            right = mid - 1
    return -1


# 寻找左边界
def left_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) / 2
        if target > nums[mid]:
            left += mid + 1
        elif target < nums[mid]:
            right = mid - 1
        elif nums[mid] == target:
            right = mid - 1
    if left > len(nums) or nums[left] != target:
        return -1
    return left


# 寻找右边界
def right_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) / 2
        if target > nums[mid]:
            left += mid + 1
        elif target < nums[mid]:
            right = mid - 1
        elif nums[mid] == target:
            left = mid - 1
    if right > len(nums) or nums[right] != target:
        return -1
    return right
