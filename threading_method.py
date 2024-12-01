from threading import Thread, RLock
from words_search import search_words_in_file, get_file_names, get_words_to_search, separate_by_chunks


def worker(file_names, words, result, lock):
    lock.acquire()
    for file_name in file_names:
        result[file_name] = search_words_in_file(file_name, words)
    lock.release()


def run_threading():
    threads = []
    result = {}
    lock = RLock()

    words = get_words_to_search()

    for chunk in separate_by_chunks(get_file_names()):
        thread = Thread(target=worker, args=(chunk, words, result, lock))
        thread.start()
        threads.append(thread)

    [thread.join() for thread in threads]

    return result
