'''Optimal solution'''
# rom_int = {'I':1, 'V': 5, 'IX':9, 'X': 10, 
#            'L':50, 'C':100, 'D':500, 'M':1000}  

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
#         s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
#         s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')

#         number = 0
#         for letter in s:
#             number += rom_int[letter]
#         return number

'''My solution'''
class Solution:
  def romanToInt(self, s: str) -> int:
    v = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }

    sum = 0
    i = 0

    if len(s) == 1: return v[s]
    while i < len(s) :

      if i + 1 < len(s) and v[s[i]] > v[s[i + 1 ]]:
        sum = sum + v[s[i]]
        i += 1
      elif i + 1 < len(s) and v[s[i]] < v[s[i + 1]]:
        sum = sum + (v[s[i + 1]] - v[s[i]])
        i += 2
      else:
        sum += v[s[i]]
        i += 1
        
        
    return sum

sol = Solution()
print(sol.romanToInt('MCMXCIV'))
