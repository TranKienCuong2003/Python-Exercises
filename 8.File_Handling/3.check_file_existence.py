import os
filename = input()
if os.path.exists(filename):
    print("Tep ton tai")
else:
    print("Tep khong ton tai")
