import threading
import time

def thr_name(name):
    print(f"{name}: Запущен")
    time.sleep(2)
    print(f"{name}: Завершен")

if __name__ == "__main__":
    threads = []
    for i in range(5):
        thread = threading.Thread(target=thr_name, args=(f"thr-{i+1}",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
