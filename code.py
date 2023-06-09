import re
import os
from count import count_words_and_sentences

def count_words_and_sentences(filename):
    # ��������� ���� ��� ����������
    with open(filename, "r") as file:
        # ������� ���� �����
        text = file.read()

    # ��������� ����������
    separators = [",", " ", ":", ";"]

    # �������� �� �������-���������� �� ������
    for sep in separators:
        text = text.replace(sep, " ")

    # ��������� �������, �� ��������� �������
    end_of_sentences = ["\.", "\!", "\?", "\..."]

    # ������ ������� ��� � �����
    words = len(text.split())

    # ������ ������� ������ � �����
    sentences = sum([len(re.findall(eos, text)) for eos in end_of_sentences])

    # ��������� ��������� � ������ ��������
    return {"words": words, "sentences": sentences}

# ������������ �������
result = count_words_and_sentences("Text.txt")
def output():
    print(f"ʳ������ ���: {result['words']}")
    print(f"ʳ������ ������: {result['sentences']}")
output()
# unit-�����
def test_count_words_and_sentences():
    # ��������� ���������� ���� ��� ����������
    with open("test_file.txt", "w") as file:
        file.write("�� �������� ����. � ����� �� ���� 5 ��� �� 2 �������.")

    # ������� �������
    assert count_words_and_sentences("test_file.txt") == (5, 2)

    # ��������� ���������� ����
    os.remove("test_file.txt")