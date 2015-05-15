#!/usr/bin/env python3

import wikipedia
from nltk import PorterStemmer
from nltk.corpus import stopwords
from sys import argv, exit
from socket import gaierror
from requests.exceptions import ConnectionError

def create(n):
    wikipedia.set_lang('en')
    stemmer = PorterStemmer()
    stops = stopwords.words('english')
    text_list = []

    for i in range(n):
        page_name = wikipedia.random()

        page = None
        while True:
            try:
                try:
                    page = wikipedia.page(page_name)
                except wikipedia.DisambiguationError as e:
                    page_name = e.options[0]
                    try:
                        page = wikipedia.page(page_name)
                    except wikipedia.DisambiguationError:
                        continue
                break
            except (wikipedia.PageError, KeyboardInterrupt, gaierror, ConnectionError, ValueError, wikipedia.WikipediaException) as e:
                print('EXCEPTION!', e)
                page_name = wikipedia.random()
                continue

        print(page_name)
        text = page.summary
        text = ''.join(c for c in text if c.lower() in 'qwertyuiopasdfghjklzxcvbnm ')

        tokens = [stemmer.stem(t.lower()) for t in text.split() if len(t) >= 3 and t not in stops]
        new_text = ' '.join(tokens)
        text_list.append(new_text)

        print(i, '/', n, '\n')

    return text_list

if __name__ == '__main__':
    if len(argv) != 4:
        print('Usage: %s <count> <dataset> <new_dataset>' % argv[0])
        exit(0)

    count = int(argv[1])
    dataset_file = argv[2]
    new_dataset_file = argv[3]

    texts = create(count)
    old = []

    with open(dataset_file, 'r') as f:
        old = [l.strip() for l in f.readlines() if len(l.strip()) > 1]

    with open(new_dataset_file, 'w') as f:
        for l in old:
            f.write(l)
            f.write('\n')

        for l in texts:
            f.write('other\t')
            f.write(l)
            f.write('\n')