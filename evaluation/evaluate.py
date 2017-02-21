#!/usr/bin/python

from __future__ import print_function
import sys
import csv
import os
from metrics import precision, recall, f1score, ndcg, average_precision, nnt1, nnt2
import numpy
import matplotlib.pyplot as plt


def read_dataset(filename):
    dataset = {}
    with open(filename, 'rb') as fin:
        reader = csv.reader(fin)
        for row in reader:
            fullid = row[0]
            category = row[1]
            subcategory = row[2]
            dataset[fullid] = (category, subcategory)
    return dataset


def load_result(path, filename, queries, targets):
    fullpath = os.path.join(path, filename)
    cutoff = 1000
    r = []
    q = queries[filename]
    with open(fullpath, 'rb') as fin:
        for line in fin.readlines()[:cutoff]:
            if line.strip() and not line.startswith('#'): # line is not empty
                retrieved, distance = line.split()
                try:
                    r.append(targets[retrieved])
                except KeyError:
                    continue
    return q, r


def load_results(path, queries, targets):
    results = []
    for filename in os.listdir(path):
        try:
            q = queries[filename]
        except KeyError:
            continue
        q, r = load_result(path, filename, queries, targets)
        results.append((q, r))
    return results


def freq_count(dataset):
    freqs = {}
    for k, v in dataset.items():
        if v[0] in freqs:
            freqs[v[0]] += 1
        else:
            freqs[v[0]] = 1
    return freqs


def categories_to_rel(queried, retrieved):
    x = []
    for r in retrieved:
        if queried[0] == r[0]:
            x.append(1.0)
        else:
            x.append(0.0)
    return x


def evaluate(path):
    queries = read_dataset('queries.csv')
    targets = read_dataset('targets.csv')
    freqs = freq_count(targets)
    results = load_results(path, queries, targets)
    cutoff = 1000
    precisions = []
    recalls = []
    f1scores = []
    aps = []
    gains = []
    nnt1s = []
    nnt2s = []
    for (queried, retrieved) in results:
        x = categories_to_rel(queried, retrieved)[:freqs[queried[0]]]
        p = precision(x)
        r = recall(x, freqs[queried[0]])
        f = f1score(x, freqs[queried[0]])
        g = ndcg(x)
        ap = average_precision(x, freqs[queried[0]])
        t1 = nnt1(x, freqs[queried[0]])
        t2 = nnt2(x, freqs[queried[0]])
        precisions.append(p)
        recalls.append(r)
        f1scores.append(f)
        gains.append(g)
        aps.append(ap)
        nnt1s.append(t1)
        nnt2s.append(t2)
    print('mean precision:', numpy.mean(precisions))
    print('mean recall:', numpy.mean(recalls))
    print('mean F1 score:', numpy.mean(f1scores))
    print('mAP:', numpy.mean(aps))
    print('mean NDCG:', numpy.mean(gains))
    print('mean nearest neighbor:', numpy.mean(nnt1s), numpy.mean(nnt2s))

    # plot precision-recall curve
    mean_precisions = numpy.zeros(cutoff, numpy.float64)
    mean_recalls = numpy.zeros(cutoff, numpy.float64)
    for (queried, retrieved) in results:
        x = categories_to_rel(queried, retrieved)[:cutoff]
        x = numpy.pad(x, (0, cutoff - len(x)), 'constant', constant_values=(0))
        precisions = []
        recalls = []
        for k, _ in enumerate(x):
            p = precision(x[:k+1])
            r = recall(x[:k+1], freqs[queried[0]])
            precisions.append(p)
            recalls.append(r)
        mean_precisions += precisions
        mean_recalls += recalls
    mean_precisions /= len(results)
    mean_recalls /= len(results)
    plt.plot(mean_recalls, mean_precisions)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.axis([0, 1, 0, 1.05])
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
        stats = evaluate(path)
    else:
        print('Usage: evaluate.py <path_to_results>')
