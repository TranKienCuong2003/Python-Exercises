class Employee:
    def __init__(self, ten, tuoi, luong):
        self.ten = ten
        self.tuoi = tuoi
        self.luong = luong
    
    def tinh_luong_thuong(self):
        return self.luong + 500

emp = Employee("Nguyen Minh", 30, 1000)
print("Luong thuc nhan:", emp.tinh_luong_thuong())
