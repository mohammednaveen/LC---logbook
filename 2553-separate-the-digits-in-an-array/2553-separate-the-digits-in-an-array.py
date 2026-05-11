class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(digit) for num in nums for digit in str(num)]
        # one liner python code
        

        # another version with str of my technique
        # res = []
        # for num in nums:
        #     if num>9:
        #         for digit in str(num):
        #             res.append(int(digit))
        #     else:
        #         res.append(num)
        # return res


        
        # my First approach using
        # answer = []
        # for num in nums:
        #     res = []
        #     while num>0:
        #         d = int(num % 10)
        #         num = num//10
        #         res.append(d)
        #     res.reverse()
        #     answer += res
        # return answer