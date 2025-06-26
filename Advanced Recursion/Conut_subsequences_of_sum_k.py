# count the subsequences of with k sum :--->
# T.C = O(2**n) ,S.C = O(n) where n is stack space
def backtrack_sub(index, subset):
    global result
    global nums
    global target
    if index >= len(nums):
        if sum(subset) == target:
            result.append(subset.copy())
            return 1
        else:
            return 0
    subset.append(nums[index])
    pick = backtrack_sub(index + 1, subset)
    subset.pop()
    not_pick = backtrack_sub(index + 1, subset)
    return pick + not_pick


nums = [5, 9, 4, 0]
result = []
target = 9
print(backtrack_sub(index=0, subset=[]))


# method 2:-->
# T.C = O(2**n) ,S.C = O(n) where n is stack space
def backtrack(index, total):
    global target
    global nums
    global result
    if total == target:
        return 1

    elif total > target:
        return 0

    if index >= len(nums):
        return 0
    sum = total + nums[index]
    pick = backtrack(index + 1, sum)
    sum = total
    not_pick = backtrack(index + 1, sum)
    return pick + not_pick


target = 9
result = []
nums = [5, 9, 4, 0]
print(backtrack(index=0, total=0))
