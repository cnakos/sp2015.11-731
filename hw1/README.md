11-731 Machine Translation
Homework 1
cnakos

My first attempt at this homework involved implementing Model 1.  My original version had a flaw: rather than weighting all possible alignments by their probabilities and taking the sum, I drew a sample alignment for each sentence and used these as the observed counts, allowing missed word alignments that were then removed from the running.  A closer examination of the IBM Models 1 and 2 paper cleared this up and turned into the version of the code that got my submission over the baseline.

From there I stalled for a while under the limits of my laptop and creativity.  I implemented a bare-bones version of Model 2, but the alignment dictionary exceeded the 2 GB of RAM Python is allowed on 32-bit Linux when run on the full set of training data.  I took a look at Chris's diagonalization approach, but I gave up when I ran into optimization I wasn't sure how to do in Python.  I tried a "dumb" version of EM that involved updating the parameters on the fly, but this produced worse results, as expected.  I also tried to generate synthetic data by matching phrases in pairs of source- and target-side sentences, but the logistics were difficult and the results were poor.

I eventually reached a breakthrough when I hijacked Chris's diagonal function and used it as a straight replacement for the implied uniform distribution in Model 1.  The fixed alignment probability produced better results than I previously had.  Shortly after that, I got my desktop up and running, which improved running time and allowed me to run IBM Model 2 to completion.  IBM Model 2 had slightly worse scores than the diagonalized version of Model 1; tweaking lambda and p0 only had minimal effect on AER, and eventually I settled on the paper's value of these parameters as a near-enough-to-optimal result.  Using the diagonal function for the initial alignment probabilities in Model 2 produced slightly better results than either Model 2 or Model 1.  I improved these results slightly by initializing the translation probabilities to numbers inversely proportional to difference in word length, rather than a uniform value.  These were the results I ultimately submitted.

Near the end of the assignment, I tried adding a Markov parameter to Model 2 (the alignment of the previous target word), but the number of paramters grew too high.  I also briefly tried symmetrization, but this produced worse results than diagonalized Model 2 alone.

Approaches I did not try include HMMs, CRFs, a proper implementation of fast_align, sampling, or any sort of pre- or post-processing, aside from lower-casing the input.  My phrase-matching approach might have worked properly with part-of-speech tagging or syntax parsing: each sentence pair could be broken into a series of aligned chunks, thereby reducing the number of possibilities for each alignment.  Stemming, compound splitting, part-of-speech tagging, etc., would likely have helped any approach as well.  


