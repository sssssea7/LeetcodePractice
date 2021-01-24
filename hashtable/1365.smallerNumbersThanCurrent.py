# 1365. How Many Numbers Are Smaller Than the Current Number
nums = [8,1,2,2,3]

def smallerNumbersThanCurrent(nums):
    myarr = []
    for i in nums:
        n = 0
        for j in range(len(nums)):
            if nums[j]<i:
                n += 1
        myarr.append(n) 
    return myarr


def ht(nums):
    ht = {}
    for idx, num in enumerate(sorted(nums)):
        #print(idx, num)
        if num not in ht:
            ht[num]=idx
    return [ht[n] for n in nums]

print(smallerNumbersThanCurrent(nums))
print(ht(nums))