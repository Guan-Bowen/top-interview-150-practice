'''
给你一个整数，将其转为罗马数字。
'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        while True:
            if num >= 1000: 
                tmp = num // 1000; num %= 1000
                for i in range(tmp): res += 'M'
            elif num >= 900: res += 'CM'; num -= 900
            elif num >= 500:
                tmp = num // 500; num %= 500
                for i in range(tmp): res += 'D'
            elif num >= 400: res += 'CD'; num -= 400
            elif num >= 100:
                tmp = num // 100; num %= 100
                for i in range(tmp): res += 'C'
            elif num >= 90: res += 'XC'; num -= 90
            elif num >= 50:
                tmp = num // 50; num %= 50
                for i in range(tmp): res += 'L'
            elif num >= 40: res += 'XL'; num -= 40
            elif num >= 10:
                tmp = num // 10; num %= 10
                for i in range(tmp): res += 'X'
            elif num == 9: res += 'IX'; num -= 9
            elif num >= 5:
                tmp = num // 5; num %= 5
                for i in range(tmp): res += 'V'
            elif num == 4: res += 'IV'; num -= 4
            else: 
                for i in range(num): res += 'I'
                break
            if num == 0: break
        
        return res