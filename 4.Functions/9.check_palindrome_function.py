def check_palindrome(s):
    return s == s[::-1]
s = input()
if check_palindrome(s):
    print("La chuoi palindrome")
else:
    print("Khong phai chuoi palindrome")
