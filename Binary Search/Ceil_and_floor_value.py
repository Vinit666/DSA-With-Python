# ceil :---> smallest element of array >=target
# floor :---> largest element of array <=target

# method 1 --->
nums = [3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15]
target = 11
ceil = -1
floor = -1
if target in nums:
    print(f"ceil is : {target} , floor is : {target}")
elif target < nums[0]:
    print(f"ceil is : {nums[0]} , floor is : {floor}")
elif target > nums[len(nums) - 1]:
    print(f"ceil is : {ceil} , floor is : {nums[len(nums)-1]}")

else:
    for i in range(0, len(nums) - 1):
        if nums[i] >= target:
            ceil = nums[i]
            floor = nums[i - 1]
            break
    print(f"ceil is : {ceil} , floor is : {floor}")


# method 2 ---> optimal solution
def binary_s(nums, target):
    low = 0
    high = len(nums) - 1
    floor = -1
    ceil = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        elif nums[mid] > target:
            ceil = nums[mid]
            high = mid - 1
        else:
            floor = nums[mid]
            low = mid + 1
    return [floor, ceil]


print(binary_s(nums=[3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15], target=100))
