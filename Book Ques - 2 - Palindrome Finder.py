def Palindrome(s):
    return s == s[::-1]


s = input("Enter your String : ")
ans = Palindrome(s)
if ans:
    print("Given string is a palindrome")


    def my_function(x):
        return x[::-1]


    x = s

    print(x)
else:
    print("Given string is not a palindrome")
    print(s[::-1])
