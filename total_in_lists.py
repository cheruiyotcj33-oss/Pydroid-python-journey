def count_numbers(nums):
    total = 0    
    for n in nums:
        total += 1
    return total
  
results = count_numbers([3,4,6,8])
print(results)