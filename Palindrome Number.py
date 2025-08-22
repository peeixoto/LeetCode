class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # Um palíndromo não pode ser um número negativo
             return False
        else:
            x = str(x) # Transformo o número em string para fcar mais fácil de manipular
            invert = x[::-1] # Inverto a string
            if x == invert:
                return True
            else:
                return False

# Soluções dos desafios
sol = Solution()
print(sol.isPalindrome(121))   # Retorna True
print(sol.isPalindrome(-121))  # Retorna False
print(sol.isPalindrome(10))    # Retorna False

# Também podemos testar Imputando um número
# print(sol.isPalindrome(int(input("Número: "))))
