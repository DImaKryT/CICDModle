import re

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