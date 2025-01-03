import time

def measure_time():
    start_time = time.time()
    time.sleep(2)
    end_time = time.time()
    return end_time - start_time

print("Thoi gian chay cua doan ma la:", measure_time(), "giay")
