class Solution:

    def minimumSum(self, num: int) -> int:
        numS = list(str(num))
        numS.sort()
        num1S = ""
        num2S = ""
        flag = True
        for i in numS:
            if flag:
                num1S += i
            else:
                num2S += i
            flag = not flag

        return int(num1S) + int(num2S)
