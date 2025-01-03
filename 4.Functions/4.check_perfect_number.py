def check_perfect_number(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num
num = int(input())
if check_perfect_number(num):
    print("La so hoan hao")
else:
    print("Khong phai so hoan hao")
