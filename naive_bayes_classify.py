from sys import argv
from sys import maxint
import json, math

def naive_bayes_classify(probs_file, probs_given_file, vocabulary_file, doc):
    probs = {}
    with open(probs_file) as f:
        probs = json.loads(f.read())

    probs_given = {}
    with open(probs_given_file) as f:
        probs_given = json.loads(f.read())

    vocabulary = []
    with open(vocabulary_file) as f:
        vocabulary = json.loads(f.read())

    pred = {}
    for c in probs.keys():
        pred_prob = math.log(probs[c])

        for word in doc.split():
            if word in vocabulary:
                pred_prob += math.log(probs_given[c][word])

        pred[c] = pred_prob

    print(pred)
    mx = -maxint
    mxc = None
    for key, value in pred.iteritems():
        if value > mx:
            mxc = key
            mx = value
    return mxc

with open(argv[4]) as f:
    doc = f.read()

print naive_bayes_classify(argv[1], argv[2], argv[3], doc)
