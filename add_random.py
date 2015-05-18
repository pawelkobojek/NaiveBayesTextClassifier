#!/usr/bin/env python3

from sys import argv, exit

if __name__ == '__main__':
    if len(argv) != 8:
        print('Usage: %s <random_words> <train> <test> <train_count> <test_count> <new_train> <new_test>' % argv[0])
        exit(0)

    random_file = argv[1]

    train_file = argv[2]
    test_file = argv[3]

    train_count = int(argv[4])
    test_count = int(argv[5])

    new_train = argv[6]
    new_test = argv[7]

    with open(random_file, 'r') as f:
        random_lines = [l.strip() for l in f.readlines() if len(l.strip()) > 1]

    if len(random_lines) < train_count + test_count:
        print('ERROR: train_count + test_count too big.')
        exit(1)

    with open(train_file, 'r') as f:
        train_lines = [l.strip() for l in f.readlines() if len(l.strip()) > 1]

    with open(test_file, 'r') as f:
        test_lines = [l.strip() for l in f.readlines() if len(l.strip()) > 1]

    train_lines.extend(random_lines[:train_count])
    test_lines.extend(random_lines[train_count:train_count + test_count])

    with open(new_train, 'w') as f:
        for l in train_lines:
            f.write(l)
            f.write('\n')

    with open(new_test, 'w') as f:
        for l in test_lines:
            f.write(l)
            f.write('\n')