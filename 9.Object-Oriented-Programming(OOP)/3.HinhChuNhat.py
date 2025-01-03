class HinhChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    
    def tinh_dien_tich(self):
        return self.dai * self.rong
    
    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

hcn = HinhChuNhat(5, 3)
print("Dien Tich:", hcn.tinh_dien_tich())
print("Chu Vi:", hcn.tinh_chu_vi())
