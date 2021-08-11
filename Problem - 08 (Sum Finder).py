n = int(input("Enter the number of terms: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + (1 / i)
print("The sum of series is", round(sum, 2))