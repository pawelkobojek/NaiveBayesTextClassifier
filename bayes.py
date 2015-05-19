#!/usr/bin/env python3

import json
import math
import decimal
from datetime import datetime


def read_dataset(dataset_file):
    with open(dataset_file) as f:
        dataset = [d.split('\t') for d in f.read().splitlines() if len(d.split('\t')) == 2]
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
    docs_per_class = {}
    words_count = 0

    j = 0
    for c in classes:
        gui_object.setNewCalculationInfo('Computing probability for class: %s' % c)

        class_docs = [row[1] for row in dataset if row[0] == c]
        prob_of_classes[c] = len(class_docs) / total_examples_count
        docs_per_class[c] = len(class_docs)

        # count all words in docs for given class
        total_words_in_class = sum([len(w.split()) for w in class_docs])
        words_count += total_words_in_class

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
        'time_created': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'created_from': dataset_file.split('/')[-1],
        'total_examples': total_examples_count,
        'total_words': words_count,
        'unique_words': len(vocabulary),
        'classes': classes,
        'docs_per_class': docs_per_class,
        'prob_of_classes': prob_of_classes,
        'probs_of_word_given_classes': probs_of_word_given_classes,
        'vocabulary': vocabulary
    }


def nb_classify_max(doc, prob_of_classes, probs_of_word_given_classes, vocabulary):
    pred = nb_classify(doc, prob_of_classes, probs_of_word_given_classes, vocabulary)

    max_value = max(pred.values())
    return [key for key, value in pred.items() if value == max_value][0]


def nb_classify_all(doc, prob_of_classes, probs_of_word_given_classes, vocabulary):
    pred = nb_classify(doc, prob_of_classes, probs_of_word_given_classes, vocabulary)

    s = decimal.Decimal(0)

    for c in pred.keys():
        pred[c] = (decimal.Decimal(math.e) ** decimal.Decimal(pred[c]))
        s += pred[c]

    for c in pred.keys():
        pred[c] = (pred[c] / s) * 100

    return pred


def nb_classify(doc, prob_of_classes, probs_of_word_given_classes, vocabulary):
    pred = {}
    for c in prob_of_classes.keys():
        pred[c] = math.log(prob_of_classes[c])
        for word in doc.split():
            if word in vocabulary:
                pred[c] += math.log(probs_of_word_given_classes[c][word])

    return pred


def serialize_to_file(obj, file_name):
    with open(file_name, 'w') as f:
        json.dump(obj, f)


def read_from_file(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)


def get_data_from_db(database):
    return database['prob_of_classes'], database['probs_of_word_given_classes'], database['vocabulary']


def compute_error(dataset, prob_of_classes, probs_of_word_given_classes, vocabulary, clbk):
    error = 0
    n = 0
    l = len(dataset)

    results = {}
    acc_all = {}
    acc_err = {}

    for c in prob_of_classes.keys():
        results[c] = {
            'accuracy': 0,
            'no_errors': 0,
            'p_errors': 0
        }
        acc_all[c] = 0
        acc_err[c] = 0

    for i, row in enumerate(dataset):
        v = int(i / l * 100)
        if v > n:
            n = v
            clbk(n)

        acc_all[row[0]] += 1
        if not nb_classify_max(row[1], prob_of_classes, probs_of_word_given_classes, vocabulary) == row[0]:
            error += 1
            acc_err[row[0]] += 1

    for c in prob_of_classes.keys():
        results[c]['accuracy'] = 100 * (1 - acc_err[c] / acc_all[c])
        results[c]['no_errors'] = acc_err[c]
        results[c]['p_errors'] = 100 * (acc_err[c] / error)

    return error / len(dataset), results