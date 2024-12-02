import os
import threading
import fnmatch
import time

results = []
lock = threading.Lock()

def find_files(directory, pattern):

    for root, _, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            filepath = os.path.join(root, filename)
            with lock:
                results.append(filepath)


if __name__ == "__main__":
    directories_to_search = [
        "/path/to/directory1",
        "/path/to/directory2",
        "/path/to/directory3",
    ]
    file_pattern = "*.txt"
    max_threads = 3

    threads = []
    start_time = time.time()

    for directory in directories_to_search:
        thread = threading.Thread(target=find_files, args=(directory, file_pattern))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    print("\nНайденные файлы:")
    for file_path in results:
        print(file_path)

