'''My solution'''
# class Solution:
#   def isPalindrome(self, x: int) -> bool:

#     if x < 0: return False

#     units = []
#     units.append( x % 10 )

#     divider = 10
#     while x % divider != x:
#       units.append( (int(x / divider) % 10) )
#       divider *= 10

#     j = (len(units) - 1)
#     for i, v in enumerate(units):
#       if j < i or j == i and v == units[j]:
#         return True
      
#       if v != units[j]:
#         return False
      
#       j -= 1


'''Faster Solution'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
    
          
      

sol = Solution()
print(sol.isPalindrome(-121))

# number = 121

# print(int(121 % 1000))

# ¿Que tengo?
# Cuando el numero se divide por una cantidad más grande que este, el reciduo del modulo es el mismo numero
# Para incrementar el valor del divisor es un x10


# 1,10,100, 1000
        