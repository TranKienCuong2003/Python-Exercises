import os
filename = input()
if os.path.exists(filename):
    os.remove(filename)
    print("Tep da bi xoa")
else:
    print("Tep khong ton tai")
