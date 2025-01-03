import re
s = input()
if re.match(r"^\d{10}$", s):
    print("So dien thoai hop le")
else:
    print("So dien thoai khong hop le")
