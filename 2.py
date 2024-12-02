import threading

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(start, end, results):
    """Находит простые числа в заданном диапазоне и сохраняет их в списке results."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    results.append(primes)


if __name__ == "__main__":
    start_range = int(input('Нижняя граница поиска: '))
    end_range = int(input('Верхняя граница поиска: '))
    num_threads = int(input('Количество потоков: '))

    chunk_size = (end_range - start_range) // num_threads
    ranges = []
    for i in range(num_threads):
        start = start_range + i * chunk_size
        end = start_range + (i + 1) * chunk_size - 1 if i < num_threads - 1 else end_range
        ranges.append((start, end))

    results = []
    threads = []
    lock = threading.Lock()

    for start, end in ranges:
        thread = threading.Thread(target=find_primes_in_range, args=(start, end, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    all_primes = []
    for prime_list in results:
        all_primes.extend(prime_list)


    print(f"Простые числа в диапазоне от {start_range} до {end_range}: {all_primes}")
    print(f"Найдено простых чисел: {len(all_primes)}")