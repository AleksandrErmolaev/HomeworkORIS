import threading
import math
import numpy as np

def factorial(n, results, index):
    if n < 0:
        results[index] = f"Ошибка: факториал не определен для отрицательных чисел."
    else:
        results[index] = math.factorial(n)


def power(base, exponent, results, index):
    results[index] = base ** exponent


def integrate(func, a, b, num_points, results, index):
    x = np.linspace(a, b, num_points)
    y = func(x)
    results[index] = np.trapz(y, x)

def main():
    numbers_for_factorial = [5, 7, 10]
    base_and_exponents = [(2, 10), (3, 5), (5, 3)]
    integration_function = lambda x: x ** 2
    a, b = 0, 1

    results = [None] * (len(numbers_for_factorial) + len(base_and_exponents) + 1)
    threads = []

    for i, n in enumerate(numbers_for_factorial):
        thread = threading.Thread(target=factorial, args=(n, results, i))
        threads.append(thread)
        thread.start()

    for i, (base, exp) in enumerate(base_and_exponents):
        thread = threading.Thread(target=power, args=(base, exp, results, len(numbers_for_factorial) + i))
        threads.append(thread)
        thread.start()

    integration_thread = threading.Thread(target=integrate, args=(integration_function, a, b, 1000, results, len(numbers_for_factorial) + len(base_and_exponents)))
    threads.append(integration_thread)
    integration_thread.start()

    for thread in threads:
        thread.join()

    for index, result in enumerate(results):
        print(f"Результат {index + 1}: {result}")

if __name__ == "__main__":
    main()