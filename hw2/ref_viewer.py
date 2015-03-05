#!/usr/bin/python

import sys

sents_file = 'data/train-test.hyp1-hyp2-ref'
labels_file = 'data/train.gold'

with open(sents_file) as fin:
    sents = [[s.strip() for s in pair.split(' ||| ')] for pair in fin]
with open(labels_file) as fin:
    labels = [int(line.strip()) for line in fin]

BOLD = '\033[1m'
ENDC = '\033[0m'

curr = 0
line = sys.stdin.readline()
while len(line) > 0:
    nums = [x for x in line.strip().split(':') if x]
    try:
        if len(nums) == 3:
            i, j, k = [int(x) for x in nums]
            r = range(i, k, j)
        elif len(nums) == 2:
            i, j = [int(x) for x in nums]
            r = range(i, j)
        elif len(nums) == 1:
            i = int(nums[0])
            r = range(i, i+1)
        else:
            r = range(curr, curr+1)
        if r[-1] >= len(sents) or r[0] < 0:
            raise IndexError('list index out of range')
        print r
    except Exception as e:
        sys.stderr.write('Error with input\n')
        print e
        line = sys.stdin.readline()
        continue
    for curr in r:
        sent = sents[curr]
        if labels[curr] < 0:
            sent[0] = BOLD + sent[0] + ENDC
        elif labels[curr] > 0:
            sent[1] = BOLD + sent[1] + ENDC
        sys.stdout.write('%iH1: %s\n' % (curr, sent[0]))
        sys.stdout.write('%iH2: %s\n' % (curr, sent[1]))
        sys.stdout.write('%iRF: %s\n' % (curr, sent[2]))
    curr += 1
    line = sys.stdin.readline()
