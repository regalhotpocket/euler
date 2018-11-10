nums = [1]
for x in range(2,1001,2):
    base = nums[-1]
    for y in range(1,5):
        nums.append(base+x*y)
print(sum(nums))