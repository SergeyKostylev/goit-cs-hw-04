from multiprocessing import Queue, Process, current_process
from words_search import search_words_in_file, get_file_names, separate_by_chunks, get_words_to_search


def worker(queue: Queue, chunk, words):
    for file_name in chunk:
        words_found = search_words_in_file(file_name, words)
        queue.put([file_name, words_found])


def run_multiprocessing():
    q = Queue()
    words = get_words_to_search()
    file_names = get_file_names()
    processes = []

    for chunk in separate_by_chunks(file_names):
        process = Process(target=worker, args=(q, chunk, words))
        process.start()
        processes.append(process)

    [process.join() for process in processes]

    results = {}

    while not q.empty():
        data = q.get()
        results[data[0]] = data[1]

    return results
