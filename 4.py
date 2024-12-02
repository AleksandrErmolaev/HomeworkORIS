import threading
import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def calculate_fibonacci_part(numbers, results, thread_index):

    for num in numbers:
        results[thread_index].append((num, fibonacci(num)))


if __name__ == "__main__":
    num_threads = int(input("Введите количество потоков: "))
    numbers_to_calculate = list(range(30)) #Задаем числа, на которых нужно произвести вычисления

    chunk_size = len(numbers_to_calculate) // num_threads
    ranges = []
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(numbers_to_calculate)
        ranges.append(numbers_to_calculate[start:end])


    results = [[] for _ in range(num_threads)]
    threads = []
    start_time = time.time()

    for i, numbers_chunk in enumerate(ranges):
        thread = threading.Thread(target=calculate_fibonacci_part, args=(numbers_chunk, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    all_results = {}
    for thread_results in results:
        all_results.update(dict(thread_results))

    print("Результаты:")
    for num, fib_num in all_results.items():
        print(f"Число Фибоначчи для {num}: {fib_num}")
