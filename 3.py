import threading

def factorial_part(start, end, num, results, lock):
    res = 1
    for i in range(start, end + 1):
        res *= i
    with lock:
        results.append(res)


def calculate_factorial(num, num_threads):
    if num == 0:
        return 1
    if num == 1:
        return 1

    results = []
    lock = threading.Lock()
    chunk_size = num // num_threads
    threads = []

    for i in range(num_threads):
        start = 1 + i * chunk_size
        end = 1 + (i + 1) * chunk_size -1 if i < num_threads -1 else num
        thread = threading.Thread(target=factorial_part, args=(start, end, num, results, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_result = 1
    for res in results:
        final_result *= res
    return final_result


if __name__ == "__main__":
    number = int(input('Число, для которого ищем факториал: '))
    num_threads = int(input('Количество потоков: '))
    result = calculate_factorial(number, num_threads)
    print(f"Факториал {number} равен: {result}")