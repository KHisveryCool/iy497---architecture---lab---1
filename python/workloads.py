n=10
def sum_to_n(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total

print(sum_to_n())

nums=[1,2,3,4,5,6,7,8,9]

def count_positives(nums):
    count=0
    for x in nums:
        if x>0:
            count+=1
    return count

print(count_positives(nums))

def max_value(nums):
    if not nums:
        raise ValueError("Empty list")
    current_max=nums[0]
    for x in nums[1:]:
        if x> current_max:
            current_max=x
    return current_max

print(max_value(nums))
