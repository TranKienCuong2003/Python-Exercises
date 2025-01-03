num = int(input())
if num < 2:
    print("Khong phai so nguyen to")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Khong phai so nguyen to")
            break
    else:
        print("La so nguyen to")
