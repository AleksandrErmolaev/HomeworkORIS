import threading
import random

def merge_sort(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def sort_subarray(sub_array, results, lock):
    sub_array.sort()
    with lock:
        results.append(sub_array)


if __name__ == "__main__":
    array_size = int(input('Размер массива: '))
    num_threads = int(input('Количество потоков: '))

    data = [random.randint(1, 1000000) for _ in range(array_size)]

    chunk_size = array_size // num_threads
    sub_arrays = []
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else array_size
        sub_arrays.append(data[start:end])

    results = []
    threads = []
    lock = threading.Lock()

    for sub_array in sub_arrays:
        thread = threading.Thread(target=sort_subarray, args=(sub_array, results, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    merged_array = results[0]
    for i in range(1, len(results)):
        merged_array = merge_sort(merged_array, results[i])

    print(f"Отсортированный массив: {merged_array}")