import re
import os
from count import count_words_and_sentences

def count_words_and_sentences(filename):
    # відкриваємо файл для зчитування
    with open(filename, "r") as file:
        # зчитуємо вміст файлу
        text = file.read()

    # визначаємо розділювачі
    separators = [",", " ", ":", ";"]

    # замінюємо всі символи-розділювачі на пробіли
    for sep in separators:
        text = text.replace(sep, " ")

    # визначаємо символи, що закінчують речення
    end_of_sentences = ["\.", "\!", "\?", "\..."]

    # рахуємо кількість слів у тексті
    words = len(text.split())

    # рахуємо кількість речень у тексті
    sentences = sum([len(re.findall(eos, text)) for eos in end_of_sentences])

    # повертаємо результат у вигляді словника
    return {"words": words, "sentences": sentences}

# використання функції
result = count_words_and_sentences("Text.txt")
def output():
    print(f"Кількість слів: {result['words']}")
    print(f"Кількість речень: {result['sentences']}")
output()
# unit-тести
def test_count_words_and_sentences():
    # створюємо тимчасовий файл для тестування
    with open("test_file.txt", "w") as file:
        file.write("Це тестовий файл. В ньому має бути 5 слів та 2 речення.")

    # тестуємо функцію
    assert count_words_and_sentences("test_file.txt") == (5, 2)

    # видаляємо тимчасовий файл
    os.remove("test_file.txt")