import timeit

from search import boyer_moore_search, knuth_morris_pratt_search, rabin_karp_search

with open('data/task3-1.txt', 'r') as file:
    text1 = file.read()

with open('data/task3-2.txt', 'r') as file:
    text2 = file.read()

test_cases = [
    {
      'name': 'стаття 1',
      'text': text1,
      'substring': 'цей алгоритм від двійкового пошуку відрізняється'
    },
    {
      'name': 'стаття 1',
      'text': text1,
      'substring': 'Думаю, в статтях точно нема подібного рядка'
    },
    {
      'name': 'стаття 2',
      'text': text2,
      'substring': 'це структура даних представлена збалансованим, сильно розгалудженим деревом пошуку.'
    },
    {
      'name': 'стаття 2',
      'text': text2,
      'substring': 'Думаю, в статтях точно нема подібного рядка'
    }
]

algorithms = [
    ('Boyer-Moore', boyer_moore_search),
    ('Knuth-Morris-Pratt', knuth_morris_pratt_search),
    ('Rabin-Karp', rabin_karp_search)
]

fastest_algorithm_per_text = {}
overall_performance = {name: 0 for name, _ in algorithms}

for test_case in test_cases:
    name, text, substring = test_case.values()

    fastest_time = float('inf')
    fastest_algorithm = None

    for algo_name, search_algorithm in algorithms:
        time_taken = timeit.timeit(lambda: search_algorithm(text, substring), number=100)
        overall_performance[algo_name] += time_taken

        if time_taken < fastest_time:
            fastest_time = time_taken
            fastest_algorithm = algo_name

    fastest_algorithm_per_text[name] = (fastest_algorithm, fastest_time)

fastest_overall = min(overall_performance, key=overall_performance.get)
fastest_overall_time = overall_performance[fastest_overall]

for text_name, (algorithm, time) in fastest_algorithm_per_text.items():
    print(f"Найшвидший алгоритм для '{text_name}' = {algorithm}, час: {time:.6f}")

print(f"Найшвидший загально {fastest_overall}, час {fastest_overall_time:.6f}")
