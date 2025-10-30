#Given an integer array nums find the subarray with largest sum and return its sum
#Output=6

nums=[-2,1,-3,4,-1,2,1,-5,4]
max=nums[0]
Csum=0
for num in nums:
    Csum+=num
    if Csum>max:
        max=Csum
    if Csum<0:
        Csum=0
print(max)