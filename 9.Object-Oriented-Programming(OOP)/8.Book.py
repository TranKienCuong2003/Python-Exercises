class Book:
    def __init__(self, ten_sach, tac_gia):
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
    
    def in_thong_tin(self):
        print(f"Ten sach: {self.ten_sach}, Tac gia: {self.tac_gia}")

book = Book("Lap Trinh Python", "Nguyen Hoang")
book.in_thong_tin()
