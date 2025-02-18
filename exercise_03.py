a = 10
b = 5
c = 3

result1 = a + b * c  # Multiplication before addition
print("Result of a + b * c:", result1)

result2 = (a + b) * c  # Addition within parentheses first
print("Result of (a + b) * c:", result2)

result3 = a - b
print("Result of a - b:", result3)

result4 = a / b  # Standard division
result5 = a // b  # Floor division
print("Result of a / b:", result4)
print("Result of a // b (floor division):", result5)

result6 = a % b  # Modulus
result7 = a ** c  # Exponentiation
print("Result of a % b (modulus):", result6)
print("Result of a ** c (exponentiation):", result7)

result8 = (a + b - c) * (a / b)  # Combination of operators and parentheses
print("Result of (a + b - c) * (a / b):", result8)