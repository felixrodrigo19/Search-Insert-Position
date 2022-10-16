import random
from traceback import print_exception


def search_insert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target == nums[0]:
        return 0
    if target == nums[-1]:
        return nums.index(nums[-1])
    if target not in nums:
        if target > nums[-1]:
            return nums.index(nums[-1]) + 1
        elif target < nums[0]:
            return 0
        else:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i

    len_nums = len(nums)
    start = 0
    end = len_nums - 1
    while start <= end:
        m = (start + end) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            start = m + 1
        else:
            end = m - 1

if __name__ == "__main__":
    nums: list = sorted(random.sample(range(200), 100))

    try:
        target: int = int(input('Insert the target(integer): '))
        print(f"index of {target}= {search_insert(nums, target)}")
    except ValueError as value_error:
        print_exception(value_error)