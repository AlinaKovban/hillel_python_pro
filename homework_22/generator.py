import random
from nltk.corpus import words


def random_word(quantity_of_words):
    english_words = words.words()
    counter = 0
    max_words = 10000

    if quantity_of_words > max_words:
        return f"Must be less words than 10000 but {quantity_of_words} were given"
    else:
        while counter < quantity_of_words:
            yield random.choice(english_words)
            counter += 1


result = random_word(10)
for i in result:
    print(i)
