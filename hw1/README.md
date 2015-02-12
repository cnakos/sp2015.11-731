11-731 Machine Translation
Homework 1
cnakos

My first attempt at this homework involved implementing Model 1.  My original version had a flaw: rather than weighting all possible alignments by their probabilities and taking the sum, I drew a sample alignment for each sentence and used these as the observed counts, allowing missed word alignments that were then removed from the running.  A closer examination of the IBM Models 1 and 2 paper cleared this up and turned into the version of the code that got my submission over the baseline.

From there I stalled for a while under the limits of my laptop and creativity.  I implemented a bare-bones version of Model 2, but the alignment dictionary exceeded the ~2 GB of RAM Python is allowed on 32-bit Linux.  I took a look at Chris's diagonalization approach, but I gave up when I ran into optimization I wasn't sure how to do in Python.  My attempts to generate synthetic data by looking at same-language phrases fell somewhat flat, ballooning run time to c*n^2 in the amount of training data and performing worse than IBM Model 1 alone.  

I eventually reached a breakthrough when I hijacked Chris's diagonal function and used it as a straight replacement for the implied uniform distribution in Model 1.  Even with this fixed alignment probability, it produced better results than I had.  Shortly after, I got my desktop up and running, which improved  


Approaches I did not try include HMMs, CRFs, any training 
symmetrization



First I tried to implement IBM Model 1, but I had poor results until I stopped sampling the alignments and instead weighted them with the proportion outlined in the Model 1 paper.
Debugging this and running it on the full training set pushed me past the baseline.
From there I 

