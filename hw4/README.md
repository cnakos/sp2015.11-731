11-731 Homework 4
cnakos

TL;DR: My final implementation was a stochastic gradient descent implementation of the baseline.
       I trained it on 5 iterations of the training data.
       Working on my desktop, the program took 8-10 hours to run.
       Alpha was 0.1 and gamma was 2.0.  The initial weights were 0.0.

That was an ordeal.  Let's see how much of it I can constructively recount.

My initial approach was the baseline with stochastic gradient descent and dicts for feature vectors.
The result was slow enough that I never finished running it.  I switched to scipy sparse csr matrices.
My implementaion was still slow, but to the tune of hours rather than days, so I continued.
My results were typically in the 0.37-0.39 range, even when I used only the default features.

From testing with only the default features, I found out that the sign was wrong on the descent algorithm.
Flipping the sign caused the default features only MRR to jump from ~0.08 to ~0.38.
The change in sign had little impact on the full implementation.
Presumably this is because the sign for the remaining features was internally consistent.

Talks with Austin, Eva, and Vivian convinced me that I needed to modify my implementation.
Rather than create a vector for each training instance, I used a single, large matrix.
The discussion also turned me on to batch updating, as well as the need to iterate over the training data.
Batch updating proved proved much faster.
I would multiply the n*f training matrix by the f*1 weight vector.
All examples with nonzero loss would be selected for updating.
I would sum the features of these examples, multiply by alpha, and update the weights.
As stochastic update would require fresh multiplication each time, I abandoned it for the time being.

The faster version of the script took minutes to run, allowing iteration.
Judicious use of pickling sped this up, allowing me to reuse training matrices and weights.
I tried various settings of gamma and alpha, various starting weights, and various numbers of iterations.
None of these got me past the low 0.39's, not even automated random weight initialization.

I briefly tried other simple features, such as length of left vs. right context.
These didn't seem to help.
I toyed with stochastic updates again, but these took a long time and didn't help my scores.

The new training data didn't seem to help either; my scores got worse.
My attempts at word co-occurrence frequency features ran into the millions of features and memory issues.
Eventually I finally barely beat the default using log_prob_tgs and a variant on the baseline binary features.
The variant extended the previous/next words to the left and right contexts, taken as sets.
My batch implementation of the baseline was able to best this by using only log_prob_tgs from the default features.
Neither of these were at the baseline's score yet.

The stochastic version eventually worked.  Apparently the new data was enough to fix it.
The drawback was that it took 8-10 hours to run, making it difficult to experiment with.
If I come back to this assignment for the extended period, I'll try 10 iterations, using only log_prob_tgs, etc.

Phew.

rerank_fastest -- Batch update version of baseline; subject of the most testing.
	       	  Successor to the tragically misnamed rerank_fast and rerank_faster.
rerank_stochastic -- The stochastic version of the baseline what did it.
rerank_stretch -- Extension of binary baseline features to include left and right contexts.
rerank_* -- Not worth uploading.  Not even I know what they all were supposed to do.
onedef.txt -- Output for rerank_fastest with other default features taken out.
stochastic.txt -- Output for rerank_stochastic.
stretch.txt -- Output for rerank_stretch.

