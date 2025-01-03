class Car:
    def __init__(self, mau_sac, toc_do):
        self.mau_sac = mau_sac
        self.toc_do = toc_do
    
    def chay(self):
        print(f"Xe co mau {self.mau_sac} dang chay voi toc do {self.toc_do} km/h")

car = Car("Red", 120)
car.chay()
