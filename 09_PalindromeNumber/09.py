import sys

nums = sys.argv[1]
print (nums)

def isPalindrome(l):
    inn = []
    for i in nums[1:-1].split(','):
        inn.append(i)
    print (inn)
    
    for i in inn:
        dat = int(i)
        res = {}
        if dat < 0:
            res[inn] = False
        if dat == 0:
            res[inn] = True
        temp = 0
        data = dat
        while data != 0:
            temp = data % 10 + temp * 10
            data = data / 10
        if temp == data:
            res[inn] = True 
        else:
            res[inn] = False
    return res 
print(isPalindrome(nums))

