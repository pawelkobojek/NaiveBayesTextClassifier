from __future__ import division
from sys import argv
from sys import maxint
import json, math

def learn_naive_bayes(dataset_file):
    dataset, classes = create_training_dictionary(dataset_file)

    vocabulary = []
    for key, value in dataset.iteritems():
        for doc in value:
            for v in doc.split():
                if not v in vocabulary:
                    vocabulary.append(v)

    # TODO - save vocabulary
    #with open("vocabulary.dat", 'w') as f:
    #    f.write(json.dumps(vocabulary))

    total_examples_count = sum(len(val) for val in dataset.itervalues())

    prob_of_classes = {}
    probs_of_word_given_classes = {}
    for c in classes:
        print "%s..." % c
        prob_of_classes[c] = len(dataset[c]) / total_examples_count

        total_number_of_words_in_class = sum(len(l) for l in [w.split() for w in dataset[c]])
        for word in vocabulary:

            word_count = len([w for w in list(traverse([w.split() for w in dataset[c]])) if w == word])

            if not c in probs_of_word_given_classes:
                probs_of_word_given_classes[c] = {}

            probs_of_word_given_classes[c][word] = (word_count + 1) / (total_number_of_words_in_class + len(vocabulary))


    # TODO - save probabilities to file for classifier
    #with open("probs.dat", 'w') as f:
    #     f.write(json.dumps(prob_of_classes))

    #with open("probs_given.dat", 'w') as f:
    #    f.write(json.dumps(probs_of_word_given_classes))

    errors = 0
    for key, value in dataset.iteritems():
        for doc in value:
            if not naive_bayes_classify(prob_of_classes, probs_of_word_given_classes, vocabulary, doc) == key:
                errors += 1

    print(100 * errors / total_examples_count)

def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value):
                yield subvalue
    else:
        yield o

def naive_bayes_classify(probs, probs_given, vocabulary, doc):
    pred = {}
    for c in probs.keys():
        pred_prob = math.log(probs[c])

        for word in doc.split():
            if word in vocabulary:
                pred_prob += math.log(probs_given[c][word])

        pred[c] = pred_prob

    mx = -100000
    mxc = None
    for key, value in pred.iteritems():
        if value > mx:
            mxc = key
            mx = value
    return mxc

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
