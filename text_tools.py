"""Text tools."""


def clean(sentence):
    return sentence.strip().lower()


def count_words(sentence):
    return len(sentence.split())
