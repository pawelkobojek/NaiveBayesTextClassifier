#!/usr/bin/env python3

import json

def read_dataset(dataset_file):
    with open(dataset_file) as f:
        dataset = [d.split('\t') for d in f.read().splitlines()]
    return dataset


def extract_vocabulary(dataset):
    vocabulary = []
    for row in dataset:
        for word in row[1].split():
            if not word in vocabulary:
                vocabulary.append(word)

    return vocabulary


def learn_naive_bayes(gui_object, dataset_file):
    gui_object.setNewStatus('Reading file \'%s\'...' % dataset_file.split('/')[-1])
    dataset = read_dataset(dataset_file)

    gui_object.setNewStatus('Creating vocabulary...')
    vocabulary = extract_vocabulary(dataset)
    classes = list(set([c[0] for c in dataset]))

    prob_of_classes = {}
    probs_of_word_given_classes = {}
    total_examples_count = len(dataset)

    gui_object.setNewStatus('Creating database...')

    j = 0
    for c in classes:
        gui_object.setNewCalculationInfo('Computing probability for class: %s' % c)

        class_docs = [row[1] for row in dataset if row[0] == c]
        prob_of_classes[c] = len(class_docs) / total_examples_count

        # count all words in docs for given class
        total_words_in_class = sum([len(w.split()) for w in class_docs])

        if not c in probs_of_word_given_classes:
            probs_of_word_given_classes[c] = {}

        i = 0
        for word in vocabulary:
            given_word_count = sum([len([w for w in wz.split() if w == word]) for wz in class_docs])
            probs_of_word_given_classes[c][word] = (given_word_count + 1) / (total_words_in_class + len(vocabulary))
            i += 1
            gui_object.updateCalculationStatus((j * len(vocabulary) + i) * 10000 / (len(vocabulary) * len(classes)), i * 10000 / len(vocabulary))

        j += 1

    gui_object.setNewStatus('')

    return {
        'classes': classes,
        'prob_of_classes': prob_of_classes,
        'probs_of_word_given_classes': probs_of_word_given_classes,
        'vocabulary': vocabulary
    }

def serialize_to_file(obj, file_name):
    with open(file_name, 'w') as f:
        json.dump(obj, f)