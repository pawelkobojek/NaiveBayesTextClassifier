#!/usr/bin/env python3

from sys import argv, exit
from hashlib import sha512
from math import log

NUMBER_OF_FEATURES = 2048

def hash(word):
    return int.from_bytes(sha512(word.encode('ascii')).digest(), 'little') % NUMBER_OF_FEATURES

def read_dataset(dataset):
    with open(dataset) as f:
        sets = f.read().splitlines()

    data_dict = {}

    for l in sets:
        pair = l.split('\t')

        if pair[0] in data_dict:
            data_dict[pair[0]].append(pair[1])
        else:
            data_dict[pair[0]] = [pair[1]]

    return len(sets), len(data_dict.keys()), data_dict


def learn(dataset, save):
    no_sets, no_classes, data_dict = read_dataset(dataset)

    vectors = {}
    for c in data_dict.keys():
        vectors[c] = []
        for s in data_dict[c]:
            vec = [1] * NUMBER_OF_FEATURES
            for w in s.split():
                vec[hash(w)] += 1
            vectors[c].append(vec)

    p_di = {}
    max_feat = [0] * NUMBER_OF_FEATURES
    p_di_vjk = {}

    print('Calculating P(Di)...')
    for c in vectors:
        p_di[c] = len(vectors[c]) / no_sets

    print('Calculating features max values...')
    for c in vectors:
        for d in vectors[c]:
            for i in range(NUMBER_OF_FEATURES):
                if d[i] > max_feat[i]:
                    max_feat[i] = d[i]

    print('Calculating P(Vjk|Di)...')
    for c in vectors:
        p_di_vjk[c] = [[]] * NUMBER_OF_FEATURES
        for f in range(NUMBER_OF_FEATURES):
            for v in range(max_feat[f]):
                count = 0
                for d in vectors[c]:
                    if d[f] == v + 1:
                        count += 1
                x = (count / no_sets)# / p_di[c]
                x = None if x == 0 else log(x)
                p_di_vjk[c][f].append(x) # TODO: len(vector[c]) zamiast no_sets?

    print('OK!')

    errors = 0
    for c in vectors:
        for v in vectors[c]:
            p = {}
            for d in vectors:
                p[d] = log(p_di[d])
                for i in range(NUMBER_OF_FEATURES):
                    if v[i] < max_feat[i] and p_di_vjk[d][i][v[i]] != None:
                        p[d] += p_di_vjk[d][i][v[i]]
            m = max(p, key=(lambda key: p[key]))
            if m != c:
                errors += 1

    print((no_sets - errors) / no_sets)

def test(dataset, save):
    pass

options = {
    'learn': learn,
    'test': test
}

if __name__ == '__main__':
    if len(argv) != 4:
        print('Usage: %s <learn|test> <dataset.txt> <out.dat>' % argv[0])
        exit(1)

    try:
        options[argv[1]](argv[2], argv[3])
    except KeyError:
        print('Invalid command \'%s\'!' % argv[1])
        exit(1)