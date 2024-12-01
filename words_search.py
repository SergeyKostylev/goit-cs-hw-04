from pathlib import Path
import re
import math

SRC_FOLDER = './src'


def search_words_in_file(file_name: str, word_list: list):
    search_result = []
    try:
        with open(f"{SRC_FOLDER}/{file_name}", 'r', encoding='utf-8') as file:
            text = file.read()
            for word in word_list:
                search = re.search(fr"\b{word}\b", text, flags=re.IGNORECASE)
                if search is not None:
                    search_result.append(word)
    except Exception as e:
        print(f"Opening file '{file_name}' problem: {e}")

    return search_result


def search():
    word_list = get_words_to_search()
    res = {}
    for file in get_file_names():
        found_words = search_words_in_file(file, word_list)
        res[file] = found_words
    return res


def get_words_to_search():
    return ['parents', 'as', 'it', ]


def get_file_names():
    return [f.name for f in Path(SRC_FOLDER).glob('*.txt')]


def separate_by_chunks(file_list, process_amount=3):
    chunk_size = math.ceil(len(file_list) / process_amount)
    return [file_list[i:i + chunk_size] for i in range(0, len(file_list), chunk_size)]
