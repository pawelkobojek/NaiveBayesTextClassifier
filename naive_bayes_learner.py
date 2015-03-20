from __future__ import division
from sys import argv

def learn_naive_bayes(dataset_file):
    dataset, classes = create_training_dictionary(dataset_file)

    vocabulary = []
    for key, value in dataset.iteritems():
        for doc in value:
            for v in doc.split():
                if not v in vocabulary:
                    vocabulary.append(v)

    total_examples_count = sum(len(val) for val in dataset.itervalues())

    prob_of_classes = {}
    probs_of_word_given_classes = {}
    for c in classes:
        prob_of_classes[c] = len(dataset[c]) / total_examples_count

        total_number_of_words_in_class = sum(len(l) for l in [w.split() for w in dataset[c]])
        for word in vocabulary:
            word_count = sum(len(l) for l in [w.split() for w in dataset[c]] if l == word)

            if not c in probs_of_word_given_classes:
                probs_of_word_given_classes[c] = {}

            probs_of_word_given_classes[c][word] = (word_count + 1) / (total_number_of_words_in_class + len(vocabulary))

    # TODO - save probabilities to file for classifier


def create_training_dictionary(dataset_file):
    with open(dataset_file) as f:
        tset = f.read().splitlines()

    training_dict = {}
    classes = []
    for s in tset:
        pair = s.split('\t')
        if not pair[0] in classes:
            classes.append(pair[0])

        if pair[0] in training_dict:
            training_dict[pair[0]].append(pair[1])
        else:
            training_dict[pair[0]] = [pair[1]]

    return training_dict, classes


learn_naive_bayes(argv[1])
