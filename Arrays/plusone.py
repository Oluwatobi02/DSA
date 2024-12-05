
def plusOne(digits):
    i = len(digits) -1
    c = 0
    output = ""
    while i > -1:
        print(output)
        if i == len(digits)-1:
            val = digits[i] + 1
            if val > 9:
                c = 1
                output = str(val%9) + output
                i-=1
                continue
            else:
                output = str(val) + output
                i-=1
                continue
        else:
            val = c + digits[i]
            if val > 9:
                c = val-9
                output = str(val-9) + output
            else:
                output = str(val) + output
            i-=1
    return list(str(int(output)))
            
nums = [9]
# print(plusOne(nums))










