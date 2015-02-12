#!/usr/bin/env python
import argparse # optparse is deprecated
from itertools import islice # slicing for iterators
from collections import Counter

def har_mean(p, r, a):
    den = (a * p + (1 - a) * r)
    if den == 0: return 0.0
    return p * r / den

def simple_meteor(h, ref, alpha):
    m = float(sum((Counter(h) & Counter(ref)).viewvalues()))
    p = m / len(h)
    r = m / len(ref)
    return har_mean(p, r, alpha)
 
def main():
    parser = argparse.ArgumentParser(description='Evaluate translation hypotheses.')
    # PEP8: use ' and not " for strings
    parser.add_argument('-i', '--input', default='data/train-test.hyp1-hyp2-ref',
            help='input file (default data/train-test.hyp1-hyp2-ref)')
    parser.add_argument('-n', '--num_sentences', default=None, type=int,
            help='Number of hypothesis pairs to evaluate')
    parser.add_argument('-a', '--alpha', default=0.5, type=float, help='meteor weight')
    # note that if x == [1, 2, 3], then x[:None] == x[:] == x (copy); no need for sys.maxint
    opts = parser.parse_args()
 
    # we create a generator and avoid loading all sentences into a list
    def sentences():
        with open(opts.input) as f:
            for pair in f:
                yield [sentence.strip().split() for sentence in pair.split(' ||| ')]
 
    # note: the -n option does not work in the original code
    for h1, h2, ref in islice(sentences(), opts.num_sentences):
        h1_val = simple_meteor(h1, ref, opts.alpha)
        h2_val = simple_meteor(h2, ref, opts.alpha)
        print(-1 if h1_val > h2_val else # \begin{cases}
                (0 if h1_val == h2_val
                    else 1)) # \end{cases}
 
# convention to allow import of this file as a module
if __name__ == '__main__':
    main()
