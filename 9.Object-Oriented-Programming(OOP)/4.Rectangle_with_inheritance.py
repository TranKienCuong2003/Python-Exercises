class HinhChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    
    def tinh_dien_tich(self):
        return self.dai * self.rong
    
    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

class Rectangle(HinhChuNhat):
    def __init__(self, dai, rong):
        super().__init__(dai, rong)

    def tinh_dien_tich(self):
        return super().tinh_dien_tich()

rect = Rectangle(4, 6)
print("Dien Tich Rectangle:", rect.tinh_dien_tich())
