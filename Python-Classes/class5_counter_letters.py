def counter_letters(list_words):
    counter = []
    for x in list_words:
        amount = len(x)
        counter.append(amount)
    return counter


def test():
    return 'test'


if __name__ == '__main__':
    list = ['dog', 'cat']
    print(counter_letters(list))
