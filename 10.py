import threading
import time
import random

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_vehicles = 0
        self.lock = threading.Semaphore(capacity)

    def enter(self, car_id):
        print(f"Автомобиль {car_id} ожидает заезда...")
        self.lock.acquire()
        with threading.Lock():
            self.current_vehicles += 1
            print(f"Автомобиль {car_id} заехал на парковку. Текущее количество автомобилей: {self.current_vehicles}")

    def exit(self, car_id):
        with threading.Lock():
            self.current_vehicles -= 1
            print(f"Автомобиль {car_id} покинул парковку. Текущее количество автомобилей: {self.current_vehicles}")
        self.lock.release()

def car(parking_lot, car_id):
    parking_lot.enter(car_id)
    parking_time = random.randint(1, 10)
    time.sleep(parking_time)
    parking_lot.exit(car_id)

def main():
    parking_lot_capacity = 5
    parking_lot = ParkingLot(parking_lot_capacity)

    threads = []

    for car_id in range(10):
        thread = threading.Thread(target=car, args=(parking_lot, car_id))
        threads.append(thread)
        thread.start()
        time.sleep(random.uniform(0.1, 1))

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()