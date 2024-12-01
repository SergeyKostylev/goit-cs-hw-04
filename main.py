from words_search import search
from threading_method import run_threading
from multiprocessing_method import run_multiprocessing
import time


if __name__ == '__main__':
    # sync
    start_time = time.time()
    sync_res = search()
    print(f"sync                time: {(time.time() - start_time):.6f} >>>>>>  {sync_res}")

    # threading
    start_time = time.time()
    threading_res = run_threading()
    print(f"threading_res       time: {(time.time() - start_time):.6f} >>>>>>  {threading_res}")

    # multiprocessing
    start_time = time.time()
    multiprocessing_res = run_multiprocessing()
    print(f"multiprocessing_res time: {(time.time() - start_time):.6f} >>>>>>  {multiprocessing_res}")
