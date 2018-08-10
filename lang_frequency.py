from collections import Counter
import sys
import re


def load_data(filepath):
    with open(filepath) as file:
        try:
            text_string = file.read()
            return text_string
        except UnicodeDecodeError:
            return None


def get_most_frequent_words(text):
    count_to_output = 10
    list_words = re.findall(r'\w+', text.lower())
    return Counter(list_words).most_common(count_to_output)


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        txt = load_data(filepath)
        most_frequent_words = get_most_frequent_words(txt)
        for word, count in most_frequent_words:
            print('{} {}'.format(word, count))
    except FileNotFoundError:
        exit('Файл не найден')
    except IndexError:
        exit('Не указан путь до файла')
