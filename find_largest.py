 give_max(nums):
    largest = nums [0]
    for n in nums:
        if n>largest:
            largest = n
    return largest
    
print(give_max([3,10,7,4,2,9]))