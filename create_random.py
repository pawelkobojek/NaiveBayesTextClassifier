#!/usr/bin/env python3

import wikipedia
from nltk import PorterStemmer
from nltk.corpus import stopwords
from sys import argv, exit
from socket import gaierror
from requests.exceptions import ConnectionError

def create(stemmer, stops):
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

    return new_text

def save_to_file(filename, n):
    stemmer = PorterStemmer()
    stops = stopwords.words('english')

    for i in range(n):
        text = create(stemmer, stops)

        with open(filename, 'a') as f:
            f.write('other\t')
            f.write(text)
            f.write('\n')

        print(i + 1, '/', n, '\n')

if __name__ == '__main__':
    if len(argv) != 3:
        print('Usage: %s <count> <filename>' % argv[0])
        exit(0)

    count = int(argv[1])
    new_dataset_file = argv[2]

    save_to_file(new_dataset_file, count)
