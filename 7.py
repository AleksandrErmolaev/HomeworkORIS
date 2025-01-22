import threading
import time
import re

def count_word_frequency(text, results, lock, thread_id):
  word_counts = {}
  words = re.findall(r'\b\w+\b', text.lower())
  for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
  with lock:
    results[thread_id] = word_counts

def process_file(filename, num_threads):
  try:
    with open(filename, 'r', encoding='utf-8') as file:
      text = file.read()
  except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
    return None

  chunk_size = len(text) // num_threads
  chunks = []
  for i in range(num_threads):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < num_threads - 1 else len(text)
    chunks.append(text[start:end])

  results = [{} for _ in range(num_threads)]
  threads = []
  lock = threading.Lock()
  start_time = time.time()

  for i, chunk in enumerate(chunks):
    thread = threading.Thread(target=count_word_frequency, args=(chunk, results, lock, i))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  end_time = time.time()

  final_counts = {}
  for counts in results:
    for word, count in counts.items():
      final_counts[word] = final_counts.get(word, 0) + count

  return final_counts, end_time - start_time


if __name__ == "__main__":
  filename = "text_file.txt"
  num_threads = 4

  results, elapsed_time = process_file(filename, num_threads)

  if results:
    print("Итоговая статистика:")
    sorted_counts = sorted(results.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_counts:
      print(f"{word}: {count}")