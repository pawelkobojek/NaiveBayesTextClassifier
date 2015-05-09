#!/usr/bin/env python3

import wikipedia
from nltk import PorterStemmer
from nltk.corpus import stopwords

def create(n):
    wikipedia.set_lang('en')
    stemmer = PorterStemmer()
    stops = stopwords.words('english')

    for i in range(n):
        page_name = wikipedia.random()

        page = None
        try:
            page = wikipedia.page(page_name)
        except wikipedia.DisambiguationError as e:
            page_name = e.options[0]
            page = wikipedia.page(page_name)

        print(page_name)
        text = page.summary
        text = ''.join(c for c in text if c.lower() in 'qwertyuiopasdfghjklzxcvbnm ')

        tokens = [stemmer.stem(t.lower()) for t in text.split() if len(t) >= 3 and t not in stops]
        new_text = ' '.join(tokens)

        print(new_text)

if __name__ == '__main__':
    create(50)