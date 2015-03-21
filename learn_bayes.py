from sys import argv
import json, math

def learn_naive_bayes(dataset_file, test_set_file=""):
    dataset = read_dataset(dataset_file)
    vocabulary = extract_vocabulary(dataset)
    classes = list(set([c[0] for c in dataset]))

    prob_of_classes = {}
    probs_of_word_given_classes = {}
    total_examples_count = len(dataset)
    for c in classes:
        print("Computing probability for class: %s...\r" % (c), end="")

        class_docs = [row[1] for row in dataset if row[0] == c]
        prob_of_classes[c] = len(class_docs) / total_examples_count

        # count all words in docs for given class
        total_words_in_class = sum([len(w.split()) for w in class_docs])

        if not c in probs_of_word_given_classes:
            probs_of_word_given_classes[c] = {}
        for word in vocabulary:
            given_word_count = sum([len([w for w in wz.split() if w == word]) for wz in class_docs])
            probs_of_word_given_classes[c][word] = (given_word_count + 1) / (total_words_in_class + len(vocabulary))

        print('')

    print('')
    test_set = read_dataset(test_set_file)
    print("Accuracy on training set: %.3f%%" % (100 * (1 - compute_error(dataset, prob_of_classes, probs_of_word_given_classes, vocabulary))))
    print("Accuracy on test set: %.3f%%" % (100 * (1 - compute_error(test_set, prob_of_classes, probs_of_word_given_classes, vocabulary))))

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

def serialize_to_file(obj, file_name):
    with open(file_name, 'w') as f:
        f.write(json.dumpls(obj))

def compute_error(dataset, prob_of_classes, probs_of_word_given_classes, vocabulary):
    error = 0

    for row in dataset:
        if not nb_classify(row[1], prob_of_classes, probs_of_word_given_classes, vocabulary) == row[0]:
            error += 1

    return error / len(dataset)

def nb_classify(doc, prob_of_classes, probs_of_word_given_classes, vocabulary):
    pred = {}
    for c in prob_of_classes.keys():
        pred[c] = math.log(prob_of_classes[c])
        for word in doc.split():
            if word in vocabulary:
                pred[c] += math.log(probs_of_word_given_classes[c][word])

    max_value = max(pred.values());
    return [key for key, value in pred.items() if value == max_value][0]


learn_naive_bayes(argv[1], argv[2])
