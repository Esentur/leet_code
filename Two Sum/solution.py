nums =[4,2,0,6,5]
target =7
answer =[]
def twoSum(nums, target):
    check={}
    for i in range(len(nums)):
        if target-nums[i] in check:
            return [i,check[target-nums[i]]]
        else:
            check[nums[i]]=i
print(twoSum(nums,target))        
